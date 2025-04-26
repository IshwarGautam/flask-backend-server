from flask_restx import reqparse
from .validator import (
    validate_status,
    validate_leave_type,
    validate_department,
    validate_email,
    validate_contact,
)

# Define the parser for employee fields
user_parser = reqparse.RequestParser()
user_parser.add_argument("name", type=str, required=True, help="Name is required.")
user_parser.add_argument(
    "email", type=validate_email, required=True, help="Email is required."
)
user_parser.add_argument(
    "department", type=validate_department, help="Department is required."
)
user_parser.add_argument("designation", type=str, help="Designation is required.")
user_parser.add_argument(
    "contact", type=validate_contact, required=True, help="Contact is required."
)
user_parser.add_argument("role", type=str, required=True, help="Role is required.")
user_parser.add_argument("manager_id", type=int, help="Manager ID is required.")

# Define the parser for leave request
employee_leave_parser = reqparse.RequestParser()
employee_leave_parser.add_argument(
    "status", type=validate_status, required=True, help="Leave status is required."
)
employee_leave_parser.add_argument(
    "type",
    type=validate_leave_type,
    required=True,
    help="Type of leave is required.",
)
employee_leave_parser.add_argument(
    "duration_from",
    type=str,
    required=True,
    help="Start date of leave is required.",
)
employee_leave_parser.add_argument(
    "duration_to",
    type=str,
    required=True,
    help="End date of leave is required.",
)
employee_leave_parser.add_argument(
    "reason",
    type=str,
    required=True,
    help="Reason for leave is required.",
)
