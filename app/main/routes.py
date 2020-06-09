from app.main import bp
from flask_login import login_required
from flask import render_template
from app.models import Subjects, Tests, Questions


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    subjects = Subjects.query.all()
    return render_template('index.html', subjects=subjects)


@bp.route('/subjects/<int:subject_id>')
@login_required
def subject_tests(subject_id):
    tests = Tests.query.filter_by(subject_id=subject_id).all()
    return render_template('subject.html', tests=tests)


@bp.route('/questions/<int:test_id>')
def question(test_id):
    pass
