from models.user import User
from flask import request, jsonify
from models.employee import Employee
from utils.custom_decorator import expect
from .user_routes import user_ns, user_api_model
from flask_restx import Resource, Namespace, fields, abort
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import (
    get_jwt,
    jwt_required,
    get_jwt_identity,
    create_access_token,
    create_refresh_token,
)

auth_ns = Namespace("auth", description="A namespace for our Authentication")

auth_api_model = auth_ns.model(
    "Auth", {"email": fields.String(), "password": fields.String()}
)


@auth_ns.route("/signup")
class SignUp(Resource):
    @auth_ns.marshal_with(auth_api_model)
    @expect(auth_ns, auth_api_model)
    def post(self):
        data = request.get_json()
        email = data.get("email")
        db_user = User.query.filter_by(email=email).first()
        if not db_user:
            abort(404, "User is not registered. Contact admin for register.")

        employee_detail = db_user.employee
        if employee_detail:
            abort(400, "The user has already signed up. Please log in.")

        new_user = Employee(
            email=email, password=generate_password_hash(data.get("password"))
        )
        new_user.save()
        return new_user


@auth_ns.route("/login")
class Login(Resource):
    @expect(auth_ns, auth_api_model)
    def post(self):
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        employee_obj = Employee.query.filter_by(email=email).first()
        employee_detail = auth_ns.marshal(employee_obj, auth_api_model)

        user_obj = employee_obj.user
        user_detail = user_ns.marshal(user_obj, user_api_model)

        if employee_obj and check_password_hash(employee_detail["password"], password):
            access_token = create_access_token(
                identity=email, additional_claims={"role": user_detail["role"]}
            )
            refresh_token = create_refresh_token(
                identity=email, additional_claims={"role": user_detail["role"]}
            )

            return jsonify(
                {"access_token": access_token, "refresh_token": refresh_token}
            )
        else:
            return {"message": "Email or password incorrect."}, 401


@auth_ns.route("/refresh")
class RefreshToken(Resource):
    @jwt_required(refresh=True)
    def post(self):
        current_user = get_jwt_identity()
        claims = get_jwt()

        new_access_token = create_access_token(
            identity=current_user, additional_claims={"role": claims.get("role")}
        )

        return jsonify({"access_token": new_access_token})
