# project/users/views.py


#################
#### imports ####
#################

from flask import flash, redirect, render_template, request, \
    session, url_for, Blueprint
from sqlalchemy.exc import IntegrityError
from forms import RegisterForm, LoginForm
from project import db, bcrypt
from project.views import login_required
from project.models import User


################
#### config ####
################

users_blueprint = Blueprint(
    'users', __name__,
    url_prefix='/users',
    template_folder='templates',
    static_folder='static'
)


################
#### routes ####
################

@users_blueprint.route('/logout/')
@login_required
def logout():
    session.pop('logged_in', None)
    session.pop('user_id', None)
    session.pop('role', None)
    session.pop('name', None)
    flash('You are logged out.')
    return redirect(url_for('users.login'))

# user login
@users_blueprint.route('/', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            u = User.query.filter_by(name=request.form['name']).first()
            if u is None:
                error = 'Invalid username or password.'
                return render_template(
                    "login.html",
                    form=form,
                    error=error
                )
            elif bcrypt.check_password_hash(
                u.password, request.form['password']
            ):
                session['logged_in'] = True
                session['user_id'] = u.id
                session['role'] = u.role
                session['name'] = u.name
                flash('You are logged in.')
                return redirect(url_for('tasks.tasks'))
        else:
            return render_template(
                "login.html",
                form=form,
                error=error
            )
    if request.method == 'GET':
        return render_template('login.html', form=form)

# user registration
@users_blueprint.route('/register/', methods=['GET', 'POST'])
def register():
    error = None
    form = RegisterForm(request.form)
    if request.method == 'POST':
        if form.validate_on_submit():
            new_user = User(
                form.name.data,
                form.email.data,
                bcrypt.generate_password_hash(form.password.data) # password hashing
            )
            try:
                db.session.add(new_user)
                db.session.commit()
                flash('Thanks for registering. Please login.')
                return redirect(url_for('users.login'))
            except IntegrityError:
                error = 'Sorry that username and/or email already exist.'
                return render_template('register.html', form=form, error=error)
        else:
            return render_template('register.html', form=form, error=error)
    if request.method == 'GET':
        return render_template('register.html', form=form)