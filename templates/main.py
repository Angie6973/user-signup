from flask import Flask, request, redirect
import cgi
import os
import jinja2
import re

template_dir= os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app= Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")



def index():
    template = jinja_env.get_template('user_signup.html')
   
    return template.render()
      

username_entry= re.compile(r"^[a-zA-Z0-9_-]{3,20}$")    
def valid_username(username):
    return username and username_entry.match(username)

password_entry = re.compile(r"^.{3,20}$")
def valid_password(password):
    return password and password_entry.match(password)

email_entry = re.compile('^[_.0-9a-z-]+@([0-9a-z][0-9a-z-]+.)+[a-z]{2,4}$')
def valid_email(email):
    return  not email or email_entry.match(email)

          





@app.route("/signup", methods=['POST'])
def valid_signup():
    error_username=""
    error_password= ""
    error_verify= ""
    error_email=""
    have_error=False
    username=request.form['username']
    password=request.form['password']
    verify=request.form['verify']
    email=request.form['email']  
    
    
     
    if not valid_username(username): 
        error_username="That's not a valid username."    
        have_error=True
     

    if not valid_password(password):
        error_password= "That wasn't a valid password."
        have_error=True

    if  password=="":
        error_verify= "Your password didn't match."
        have_error=True
    
    if password != verify :
        error_verify= "Your password didn't match."
        have_error=True

    if not valid_email(email):
        error_email= "That's not a valid email."
        have_error=True

    if have_error  :
        template=jinja_env.get_template('user_signup.html') 
        return template.render(username=username, email=email, error_username= error_username, error_password=error_password, error_verify=error_verify, error_email=error_email)
    if have_error== False:
        template=jinja_env.get_template('welcome.html')
        return template.render(username=username)

app.run()