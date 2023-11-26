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


@app.route('/categories')
def back():
    return render_template('categories.html')


@app.route('/category_name')
def category_name():
    return render_template('recipe_page.html')


@app.route('/favorites')
def favorites():
    return render_template('favorites.html')
    

@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/edit')
def edit():
        return render_template('edit.html')


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

'''
#PASSWORD VALIDATION
import string
punc_marks =string.punctuation
lower_case = string.ascii_lowercase
upper_case = string.ascii_uppercase
digits = string.digits


# print(punc_marks, lower_case, upper_case, digits, sep='\n')

username = input("Enter your username: ")
password = input("Enter your password: ")
print(password)

mycounts_p = []
mycounts_l = []
mycounts_u = []
mycounts_d = []
# check if the password length is >= 8 characters
if len(password) >=8:
  for x in punc_marks:
    if x in userpass:
        mycount_p = 1
        mycounts_p.append(mycount_p)
    else:
      mycount_p = 0
      mycounts_p.append(mycount_p)
      
  for y in lower_case:
    if y in userpass:
      mycount_l = 1
      mycounts_l.append(mycount_l)
    else:
      mycount_l = 0
      mycounts_l.append(mycount_l)
      
  for z in upper_case:
    if z in userpass:
      mycount_u = 1
      mycounts_u.append(mycount_u)
    else:
      mycount_u = 0
      mycounts_u.append(mycount_u)
      
  for m in digits:
    if m in userpass:
      mycount_d = 1
      mycounts_d.append(mycount_d)
    else:
      mycount_d = 0
      mycounts_d.append(mycount_d)

#     print(mycounts_p, mycounts_l, mycounts_d, mycounts_u, sep="\n")
#     final_list = max(mycounts_p) + max(mycounts_l) + max(mycounts_d) + max(mycounts_u)
#     print(final_list)
#     if final_list >=4:
#         print("You've logged in successfully")
#     else:
#         print("Invalid password")
# else:
#   print("Password must be 8 characters or more!!!")
'''
