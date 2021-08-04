# flask imports
from flask import Flask # importing Flask
from flask import render_template # importing the ability to render web pages
from flask import url_for #
from flask import flash # importing to allow for a message to display
from flask import redirect # importing for the ability to redirect after a GET/POST request on submit, eg after login

from forms import RegistrationForm, LoginForm

# app config
app = Flask(__name__)
app.config['SECRET_KEY'] = '3ce640eb16424716c5ebbed586dc2b29' # app.config is how you set values on the app
if __name__ == '__main__':
    app.run(debug=True)

# data import

posts = [
    {
        'author' : 'Name 1',
        'title' : 'Post 1',
        'content' : 'First',
        'date_posted' : 'August, 2021'
    },
    {
        'author' : 'Name 2',
        'title' : 'Post 2',
        'content' : 'second',
        'date_posted' : 'August, 2021'
    }
]

# pages routing
@app.route("/")
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts, title='Home')

@app.route('/about')
def about_page():
    return render_template('about.html', title='About')

# forms routing
@app.route('/register', methods=['GET', 'POST']) # methods= is allowing GET and POST as methods when submitting the register form
def register_page():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') # the 'success' category is from bootstrap and is passed into the layout.html when creating a flash message.
        return redirect(url_for('home_page')) # will redirect the user to home_page function (/home_page)
    return render_template('register.html', title='Register', form=form)

@app.route('/login')
def login_page():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)
    
