from flask import Flask,render_template

app = Flask(__name__)
app.secret_key ='itsmysecretkey'
@app.route('/login')
def login():
    return render_template('sign-in.html')


@app.route('/register')
def register():
    return render_template('register.html')


if(__name__=='__main__'):
    app.run(host='0.0.0.0',debug=True)
