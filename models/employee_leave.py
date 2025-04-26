from database.exts import db


class EmployeeLeave(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    employee_id = db.Column(db.Integer(), nullable=False)
    status = db.Column(db.String(), nullable=False)
    type = db.Column(db.String(), nullable=False)
    duration_from = db.Column(db.String(), nullable=False)
    duration_to = db.Column(db.String(), nullable=False)
    reason = db.Column(db.String(), nullable=False)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def update(self, status, type, duration_from, duration_to, reason):
        self.status = status
        self.type = type
        self.duration_from = duration_from
        self.duration_to = duration_to
        self.reason = reason

        db.session.commit()
