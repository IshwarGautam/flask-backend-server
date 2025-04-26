import re
from constants import LEAVE_STATUSES, LEAVE_TYPES, DEPARTMENT_DESIGNATION_MAP


def validate_email(value):
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(pattern, value):
        raise ValueError("Invalid email format")
    return value


def validate_contact(value):
    if not value.isdigit():
        raise ValueError("Contact must contain only digits.")
    if len(value) != 10:
        raise ValueError("Contact must be exactly 10 digits.")
    return value


def validate_status(value):
    if value not in LEAVE_STATUSES:
        raise ValueError(f"Status must be one of {LEAVE_STATUSES}")
    return value


def validate_leave_type(value):
    if value not in LEAVE_TYPES:
        raise ValueError(f"Type must be one of {LEAVE_TYPES}")
    return value


def validate_department(value):
    if value not in DEPARTMENT_DESIGNATION_MAP:
        raise ValueError(f"Invalid department.")
    return value


def validate_designation(department, designation):
    if designation not in DEPARTMENT_DESIGNATION_MAP[department]:
        return None
    return designation
