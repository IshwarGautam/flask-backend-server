from flask import request
from models.user import User
from utils.custom_decorator import expect
from flask_restx import Resource, Namespace, fields

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
        data = request.get_json()
        new_user = User(
            name=data.get("name"),
            email=data.get("email"),
            department=data.get("department"),
            designation=data.get("designation"),
            contact=data.get("contact"),
            role=data.get("role"),
            manager_id=data.get("manager_id"),
        )
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
        employee_to_update = User.query.get_or_404(id)
        data = request.get_json()
        employee_to_update.update(
            data.get("name"),
            data.get("email"),
            data.get("department"),
            data.get("designation"),
            data.get("contact"),
            data.get("role"),
            data.get("manager_id"),
        )
        return {"message": "User updated successfully."}

    def delete(self, id):
        """Delete a user by id"""
        user_to_delete = User.query.get_or_404(id)
        user_to_delete.delete()
        return {"message": "User deleted successfully."}
