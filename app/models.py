from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin


class Users(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


@login.user_loader
def load_user(id):
    return Users.query.get(int(id))


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    children = db.relationship("Subjects")

    def __repr__(self):
        return '<Category {}>'.format(self.name)



class Subjects(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    category = db.Column(db.Integer, db.ForeignKey('category.id'))
    image = db.Column(db.Text, default='https://i.ibb.co/N6S5H2y/shutterstock-650.jpg')
    children = db.relationship("Tests")

    def __repr__(self):
        return '<Subject ({},{})>'.format(self.id, self.name)


class Tests(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    subject_id = db.Column(db.Integer, db.ForeignKey('subjects.id'))
    children = db.relationship("Questions")

    def __repr__(self):
        return '<Test ({},{})>'.format(self.id, self.name)


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    test_id = db.Column(db.Integer, db.ForeignKey('tests.id'))
    q_text = db.Column(db.String(256))
    correct_ans = db.Column(db.Integer)
    children = db.relationship("Answers")

    def __repr__(self):
        return '<id {},Question {}'.format(self.id, self.q_text)


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    opt_id = db.Column(db.Integer)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'))
    ans_text = db.Column(db.String(256))

    def __repr__(self):
        return '<Option {}'.format(self.ans_text)
