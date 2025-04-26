from flask import request
from models.user import User
from utils.custom_decorator import expect
from models.employee_leave import EmployeeLeave
from validation.parser import employee_leave_parser
from flask_restx import Resource, Namespace, fields, abort

employee_leave_ns = Namespace(
    "employee", description="A namespace for Employees Leaves Request"
)

employee_leave_api_model = employee_leave_ns.model(
    "EmployeeLeave",
    {
        "id": fields.Integer(),
        "employee_id": fields.Integer(),
        "status": fields.String(),
        "type": fields.String(),
        "duration_from": fields.String(),
        "duration_to": fields.String(),
        "reason": fields.String(),
    },
)


@employee_leave_ns.route("/<int:id>/apply-leave")
class EmployeeLeavesResource(Resource):
    @employee_leave_ns.marshal_list_with(employee_leave_api_model)
    def get(self, id):
        """Get all leave requests for a particular employee by employee id"""
        # Check if the employee exists
        employee = User.query.get(id)
        if not employee:
            abort(404, "Employee not found")

        # Query for all leave requests for the employee
        employee_leaves = EmployeeLeave.query.filter_by(employee_id=id).all()
        return employee_leaves

    @employee_leave_ns.marshal_with(employee_leave_api_model)
    @expect(employee_leave_ns, employee_leave_api_model, ["id", "employee_id"])
    @employee_leave_ns.response(200, "Employee leave requested successfully")
    @employee_leave_ns.response(404, "Employee not found")
    def post(self, id):
        """Apply a leave"""
        # Check if the employee exists
        employee = User.query.get(id)
        if not employee:
            abort(404, "Employee not found")

        # Parse and validate request data
        args = employee_leave_parser.parse_args()
        leave_data = {key: value for key, value in args.items() if value is not None}
        leave_info = EmployeeLeave(**{"employee_id": id, **leave_data})
        leave_info.save()
        return leave_info


@employee_leave_ns.route("/<int:employee_id>/apply-leave/<int:leave_id>")
class EmployeeLeaveResource(Resource):
    @employee_leave_ns.marshal_with(employee_leave_api_model)
    @expect(employee_leave_ns, employee_leave_api_model, ["id", "employee_id"])
    def put(self, employee_id, leave_id):
        """Update a leave status by id"""
        leave_data = EmployeeLeave.query.filter_by(
            employee_id=employee_id, id=leave_id
        ).first()

        if not leave_data:
            abort(404, "No leave request found.")

        leave_data = employee_leave_ns.marshal(leave_data, employee_leave_api_model)
        data = request.get_json()

        updated_leave_data = {
            key: value for key, value in data.items() if value is not None
        }
        new_leave_data = {**leave_data, **updated_leave_data}

        leave_data.update(**new_leave_data)
        return leave_data
