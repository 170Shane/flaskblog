from flaskblog.models import User, Post
from flask import render_template, url_for, flash, redirect
from flaskblog.forms import RegisterForm, LoginForm
from flaskblog import app, bcrypt, db

dummy_data = [
    {
        'author': 'Shane Clark',
        'title': 'Blog Post 1',
        'content': 'Blog Content 1',
        'date_posted': 'March 25, 2021'
    },
    {
        'author': 'Julie Clark',
        'title': 'Blog Post 2',
        'content': 'Blog Content 2',
        'date_posted': 'March 26, 2021'
    }
]


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', dummy_data=dummy_data, title="Test title")  # Can pass in data to route here


@app.route('/about')
def about_page():
    return render_template('about.html')


@app.route('/register', methods=['GET', 'POST'])  # ensure that route also accepts POST requests
def register_page():
    #  create an instance of the Registration Form
    register_form = RegisterForm()

    # The validate_on_submit() method returns True when the form is submitted using the POST request and data is valid.
    if register_form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(register_form.password.data).decode('utf-8')
        user = User(
                    username=register_form.username.data,
                    email=register_form.email.data,
                    password=register_form.password.data
                    )
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {register_form.username.data}! You are now able to log in.', category='success')
        return redirect(url_for('login_page'))

    # pass the form to the template in the same way as variables and data are passed to the template
    return render_template('register.html', title='Registration Page', register_form=register_form)


@app.route('/login', methods=['GET', 'POST'])  # ensure that route also accepts POST requests)
def login_page():
    #  create an instance of the Login Form
    login_form = LoginForm()

    # The validate_on_submit() method returns True when the form is submitted using the POST request and data is valid.
    if login_form.validate_on_submit():
        flash(f'Login successful for {login_form.email.data}!', category='success')
        return redirect(url_for('home'))

    # pass the form to the template in the same way as variables and data are passed to the template
    return render_template('login.html', title='Login Page', login_form=login_form)
