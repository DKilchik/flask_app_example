from app.main import bp
from flask_login import login_required
from flask import render_template
from app.models import Subjects


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    subjects = Subjects.query.all()
    print(subjects)
    return render_template('index.html', subjects=subjects)


@bp.route('subjects/<subject>')
@login_required
def subject_tests(subject):
    return render_template('subject.html', subject=subject)
