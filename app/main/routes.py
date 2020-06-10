from app.main import bp
from flask_login import login_required
from flask import render_template
from app.models import Subjects, Tests, Questions, Answers


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


@bp.route('/tests/<int:test_id>')
def question(test_id):
    question = Questions.query.filter_by(test_id=test_id).first()
    answer_options = Answers.query.filter_by(question_id=question.id).all()
    return render_template('question.html', question=question, options=answer_options)
