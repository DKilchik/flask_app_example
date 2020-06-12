from app.main import bp
from app.main.forms import QsForm
from flask_login import login_required
from flask import render_template, request, redirect, url_for
from app.models import Subjects, Tests, Questions, Answers


@bp.route('/')
@bp.route('/index')
@login_required
def index():
    subjects = Subjects.query.all()
    return render_template('index.html', subjects=subjects)


@bp.route('/subjects/<int:subject_id>')
@login_required
def subject(subject_id):
    tests = Tests.query.filter_by(subject_id=subject_id).all()
    return render_template('subject.html', tests=tests)


@bp.route('/test/<int:test_id>')
def test(test_id):
    first_question = Questions.query.filter_by(test_id=test_id).first_or_404()
    return redirect(url_for('main.question', question_id=first_question.id))


@bp.route('/question/<int:question_id>', methods=['GET', 'POST'])
def question(question_id):
    form = QsForm()
    question = Questions.query.filter_by(id=question_id).first()
    answer_options = Answers.query.filter_by(question_id=question_id).all()
    form.option.choices = [(option.opt_id, option.ans_text) for option in answer_options]
    if request.method == 'POST':
        if int(form.option.data) == int(question.correct_ans):
            print('Correct answer')
        else:
            print('Wrong answer')
        next_question = Questions.query.filter(Questions.id > int(question.id)).first()
        if next_question is None:
            return redirect(url_for('main.index'))
        return redirect(url_for('main.question', question_id=next_question.id))
    else:
        return render_template('question.html', question=question, form=form)
