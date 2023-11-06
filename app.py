from flask import Flask, render_template, request, session, redirect, url_for, flash
from models import *

app = Flask(__name__)
app.secret_key = 'somesecretkey'
users={}

@app.route('/', methods=['GET','POST'])
def signup():
    if request.method == 'POST':
        print(request.data)
        # session.pop('user_id', None)

        fullname = request.form['fullname']
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if username in users:
            flash('user already exists')
        else:
            if password==confirm_password:
                user = User(fullname,username,email,password,confirm_password)
                users[user.username]=user
                print(users[user.username])
                flash('user added successfully')
                return redirect(url_for('login'))
            else:
                flash('the two persons did not match')
    return render_template('signup.html')


@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        if request.form['username'] not in users:
            flash('user not recognised please register')
        else:
            username = request.form['username']
            user = users[username]
            # user = users.get(username)
            if request.form['password'] != user.password:
                flash('incorrect password') 
            else:
                session['username'] = request.form['username']
                session['logged_in'] = True
                return redirect(url_for('categories', username=username))
            
    return render_template('login.html')


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You have logged out.')

    return redirect(url_for('login'))


@app.route('/<username>/categories')
def categories(username):
    user = users[session['username']]
    username = user.username
    return render_template('categories.html', username=username)

@app.route('/recipe_page')
def recipe_page():
    return render_template('recipe_page.html')

@app.route('/view')
def view():
    return render_template('view.html')


