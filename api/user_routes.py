from flask import request
from models.user import User
from validation.parser import user_parser
from utils.custom_decorator import expect
from validation.validator import validate_designation
from flask_restx import Resource, Namespace, fields, abort

user_ns = Namespace("users", description="A namespace for Users")

user_api_model = user_ns.model(
    "User",
    {
        "id": fields.Integer(),
        "name": fields.String(),
        "email": fields.String(),
        "department": fields.String(),
        "designation": fields.String(),
        "contact": fields.String(),
        "role": fields.String(),
        "manager_id": fields.Integer(),
    },
)


@user_ns.route("/")
class UsersResource(Resource):
    # @expect → Validates the input
    # @marshal_with → Formats the output
    @user_ns.marshal_list_with(user_api_model)
    def get(self):
        """Get all users"""
        employees = User.query.all()
        return employees

    @user_ns.marshal_with(user_api_model)
    # @user_ns.expect(user_api_model)
    @expect(user_ns, user_api_model, ["id"])  # using my own custom decorator
    def post(self):
        """Create a new user"""
        # Parse and validate request data
        args = user_parser.parse_args()

        # Validate designation
        designation = validate_designation(args["department"], args["designation"])
        if not designation:
            abort(400, "Invalid designation")

        user_data = {key: value for key, value in args.items() if value is not None}
        new_user = User(**user_data)
        new_user.save()
        return new_user


@user_ns.route("/<int:id>")
class UserResource(Resource):

    @user_ns.marshal_with(user_api_model)
    def get(self, id):
        """Get a user details by id"""
        user = User.query.get_or_404(id)
        return user

    @expect(user_ns, user_api_model, ["id"])
    def put(self, id):
        """Update a user by id"""
        user_detail = User.query.get_or_404(id)
        args = user_parser.parse_args()

        # Validate designation
        designation = validate_designation(args["department"], args["designation"])
        if not designation:
            abort(400, "Invalid designation")

        updated_data = {key: value for key, value in args.items() if value is not None}
        user_detail.update(**updated_data)
        return {"message": "User updated successfully."}

    def delete(self, id):
        """Delete a user by id"""
        user_to_delete = User.query.get_or_404(id)
        user_to_delete.delete()
        return {"message": "User deleted successfully."}
