import pyrebase

from flask import Flask, flash, redirect, render_template, \
     request, url_for

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

config = {
"apiKey": "AIzaSyBc2ta_6WXB9s18XcHTud-9DcViA8fdyHU",
"authDomain": "test-658ea.firebaseapp.com",
"databaseURL": "https://test-658ea.firebaseio.com",
"projectId": "test-658ea",
"storageBucket": "test-658ea.appspot.com",
"messagingSenderId": "85272233684",
"appId": "1:85272233684:web:c79c9d4a3d8fff038d5d41"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

auth = firebase.auth()

#authenticate a user
user = auth.sign_in_with_email_and_password("william@hackbrightacademy.com", "mySuperStrongPassword")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/landing/<username>')
def landingPage():
    return render_template('landing.html', username=username)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    unsuccessful = 'Please check your credentials'
    
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        
        try:
             auth.sign_in_with_email_and_password(email, password)
             return render_template('landing.html', username=email)
        except:
             return render_template('login.html', us=unsuccessful)

    return render_template('login.html', error=error)

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    error = None
    mesg = 'Please enter your credentials'
    unsuccessful = 'Username Exist, or password must be 6 characters'
    
    if request.method == 'POST':
        email = request.form['username']
        password = request.form['password']
        
        try:
             user = auth.create_user_with_email_and_password(email, password)
             return render_template('landing.html', username=email)
        except:
             return render_template('signup.html', us=unsuccessful)

    return render_template('signup.html', error=error)

    
if __name__ == '__main__':
      app.run()