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


@app.route('/back')
def back():
    return render_template('categories.html')


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


#Password validation
def password_check(password):
     
    SpecialSym =['$', '@', '#', '%']
    val = True
     
    if len(password) < 6:
        print('length should be at least 6')
        val = False
         
    if len(password) > 20:
        print('length should be not be greater than 8')
        val = False
         
    if not any(char.isdigit() for char in password):
        print('Password should have at least one numeral')
        val = False
         
    if not any(char.isupper() for char in password):
        print('Password should have at least one uppercase letter')
        val = False
         
    if not any(char.islower() for char in password):
        print('Password should have at least one lowercase letter')
        val = False
         
    if not any(char in SpecialSym for char in password):
        print('Password should have at least one of the symbols $@#')
        val = False
    if val:
        return val
 
# Main method
def main():
    password = 'Geek12@'
     
    if (password_check(password)):
        print("Password is valid")
    else:
        print("Invalid Password !!")
         
# Driver Code        
if __name__ == '__main__':
    main()



