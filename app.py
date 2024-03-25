from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo
import pandas as pd
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'

@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        email = form.email.data
        password = form.password.data
        if save_credentials_to_excel(username, email, password):
            return redirect(url_for('logged_in'))
        else:
            return render_template('register.html', form=form, message='Username or email already exists.')
    return render_template('register.html', form=form)

def check_existing_credentials(email, password):
    if os.path.exists('user_data.xlsx'):
        df = pd.read_excel('user_data.xlsx')
        print("Existing Emails:", df['Email'].values)
        print("Existing Passwords:", df['Password'].values)
        if (df['Email'] == email).any() or (df['Password'] == password).any():
            return True
    return False

def save_credentials_to_excel(username, email, password):
    if not check_existing_credentials(email, password):
        try:
            if os.path.exists('user_data.xlsx'):
                df = pd.read_excel('user_data.xlsx')
            else:
                df = pd.DataFrame(columns=['Username', 'Email', 'Password'])
            new_data = pd.DataFrame([[username, email, password]], columns=['Username', 'Email', 'Password'])
            df = pd.concat([df, new_data], ignore_index=True)
            df.to_excel('user_data.xlsx', index=False)
            return True
        except Exception as e:
            return False
    else:
        return False


@app.route('/login', methods=['GET', 'POST'])
def login():
  return render_template('login.html')
# 
@app.route('/chatbot')
def chatbot():
    return render_template('chatbot.html')

@app.route('/logged_in', methods=['GET', 'POST'])
def logged_in():
    if request.method == 'POST':
        username = request.form.get("username")
        email = request.form.get("email")
        password = request.form.get("password")
        print(f"Received data - Username: {username}, Email: {email}, Password: {password}")
        if os.path.exists('user_data.xlsx'):
            df = pd.read_excel('user_data.xlsx')
        else:
            df = pd.DataFrame(columns=['Username', 'Email', 'Password'])
        new_data = pd.DataFrame([[username, email, password]], columns=['Username', 'Email', 'Password'])
        df = pd.concat([df, new_data], ignore_index=True)
        df.to_excel('user_data.xlsx', index=False)
        return render_template('logged_in.html', username=username)
    else : 
        return render_template('logged_in.html', teste = request.args.get("email"), username = "pires")



if __name__ == '__main__':
    app.run(debug=True)
