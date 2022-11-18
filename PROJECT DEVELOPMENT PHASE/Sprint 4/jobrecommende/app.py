import os
from flask import Flask 
from flask import url_for ,render_template,request,redirect
import db
from db import ibm_db
app = Flask(__name__)
app.secret_key ='AAnbb123--++'
@app.route('/')
def home():
    return render_template("index.html")

@app.route('/about')
def about_us():
    return render_template("about.html")
@app.route('/category')
def category():
    return render_template("category.html")
@app.route('/joblist')
def joblist():
    return render_template("job-list.html")
@app.route('/jobdetail')
def jobdetail():
    return render_template("job-detail.html")
@app.route('/testimonial')
def testimonial():
    return render_template("testimonial.html")
@app.route('/404')
def fourohfour():
    return render_template("404.html")
def contact():
    return render_template("contact.html")
    
@app.route('/login',methods = ['GET'])
def login():
    global userid
    msg = ''
    if request.method == 'GET':
        email = request.args.get("email")
        password = request.args.get("password")
        
        sql = "SELECT * FROM USERDETAILS WHERE email = ? AND password = ?"
        stmt = ibm_db.prepare(db.conn,sql)
        
        ibm_db.bind_param(stmt,1,email)
        ibm_db.bind_param(stmt,2,password)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            return redirect(url_for("index.html"))
        else:
            msg = 'Invalid details. Please check the Email ID - Password combination.!'
            return render_template("home.html",msg=msg)
        
    
@app.route('/register', methods=['GET','POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        phone = request.form['Phone']
        email = request.form['email']
        password = request.form['password']
        sql = "SELECT * FROM USERDETAILS WHERE email = ?"
        stmt = ibm_db.prepare(db.conn, sql)
        ibm_db.bind_param(stmt,1,email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)
        print(account)
        if account:
            msg='Job Recommender Account Already exist.kindly login!'
            return render_template("home.html",msg=msg)
       
        else:
            sql ="INSERT INTO USERDETAILS(NAME,PHONE,EMAIL,PASSWORD) VALUES('{0}','{1}','{2}','{3}')"
    
            res = ibm_db.exec_immediate(db.conn,sql.format(name,phone,email,password))
            msg='registration successful'
            return render_template("home.html",msg=msg)
            
    
    
            
    return render_template("register.html")
 
if(__name__=='__main__'):
     port = os.environ.get("PORT",5000)
     app.run(debug=True)
    
