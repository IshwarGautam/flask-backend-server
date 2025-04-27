from database.exts import db


class User(db.Model):
    __tablename__ = "user"

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    department = db.Column(db.String(), nullable=False)
    designation = db.Column(db.String(), nullable=False)
    contact = db.Column(db.String(), nullable=False)
    role = db.Column(db.String(), nullable=False)
    manager_id = db.Column(db.Integer(), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def update(self, name, email, department, designation, contact, role, manager_id):
        self.name = name
        self.email = email
        self.department = department
        self.designation = designation
        self.contact = contact
        self.role = role
        self.manager_id = manager_id

        db.session.commit()


# ---------------  To solve the issue "Constraint must have a name" ---------------------
# Add uq_user_email to the upgrade script (Go to migration folder -> latest version ->)
# Remove duplicate email if already there in db
# Also need to remove _alembic_tmp_user from the table if exists
# ---------------------------------------------------------------------------------------
