from database.exts import db

"""
 class Employee:
     email:string foreign key
     password:text
 """


class Employee(db.Model):
    __tablename__ = "employee"

    email = db.Column(db.String(), db.ForeignKey("user.email"), primary_key=True)
    password = db.Column(db.Text(), nullable=False)

    # Relationship with User model
    user = db.relationship(
        "User", backref=db.backref("employee", uselist=False, passive_deletes=True)
    )

    def save(self):
        db.session.add(self)
        db.session.commit()
