# Define allowed values
LEAVE_STATUSES = {"approved", "pending", "rejected"}
LEAVE_TYPES = {"sick", "annual", "compensatory", "leave without pay"}
ROLE = {"ADMIN": "admin", "EMPLOYEE": "employee", "MANAGER": "manager"}

DEPARTMENT_AND_DESIGNATIONS = [
    {
        "department": "Engineering",
        "designations": [
            "Software Engineer",
            "Senior Software Engineer",
            "Lead Software Engineer",
            "Software Architect",
            "Full-Stack Developer",
            "Systems Engineer",
            "Senior Systems Engineer",
            "Systems Administrator",
            "Network Engineer",
            "Senior Network Engineer",
            "Network Administrator",
            "DevOps Engineer",
            "Senior DevOps Engineer",
            "DevOps Lead",
            "Cloud Engineer",
            "Cloud Architect",
            "Cloud Operations Engineer",
            "QA Engineer",
            "Senior QA Engineer",
            "QA Lead",
            "Test Automation Engineer",
        ],
    },
    {
        "department": "IT Operations",
        "designations": [
            "IT Support Specialist",
            "IT Support Manager",
            "Help Desk Technician",
            "Infrastructure Engineer",
            "Senior Infrastructure Engineer",
            "IT Operations Manager",
        ],
    },
    {
        "department": "Product Management",
        "designations": [
            "Product Manager",
            "Senior Product Manager",
            "Product Owner",
            "Product Director",
            "UX/UI Designer",
            "Product Designer",
            "User Researcher",
        ],
    },
    {
        "department": "Project Management",
        "designations": [
            "Project Manager",
            "Senior Project Manager",
            "Program Manager",
            "Project Coordinator",
            "Scrum Master",
            "Agile Coach",
        ],
    },
    {
        "department": "Business Analysis",
        "designations": [
            "Business Analyst",
            "Senior Business Analyst",
            "Systems Analyst",
            "Data Analyst",
            "Data Scientist",
            "Data Engineer",
        ],
    },
    {
        "department": "Customer Support",
        "designations": [
            "Technical Support Specialist",
            "Technical Support Manager",
            "Customer Success Manager",
            "Customer Success Specialist",
            "Help Desk Analyst",
            "Help Desk Manager",
        ],
    },
    {
        "department": "Human Resources (HR)",
        "designations": [
            "HR Manager",
            "Senior HR Manager",
            "HR Director",
            "Talent Acquisition Specialist",
            "Recruitment Manager",
            "Employee Relations Specialist",
            "Learning and Development Manager",
        ],
    },
    {
        "department": "Finance",
        "designations": [
            "Accountant",
            "Senior Accountant",
            "Accounting Manager",
            "Financial Analyst",
            "Senior Financial Analyst",
            "Finance Manager",
        ],
    },
    {
        "department": "Marketing",
        "designations": [
            "Digital Marketing Specialist",
            "Digital Marketing Manager",
            "Content Strategist",
            "Content Marketing Manager",
            "SEO Specialist",
            "SEM Manager",
        ],
    },
    {
        "department": "Research and Development (R&D)",
        "designations": [
            "R&D Engineer",
            "Research Scientist",
            "Innovation Manager",
            "Technical Research Scientist",
            "Research Engineer",
        ],
    },
]

DEPARTMENT_DESIGNATION_MAP = {
    item["department"]: item["designations"] for item in DEPARTMENT_AND_DESIGNATIONS
}
