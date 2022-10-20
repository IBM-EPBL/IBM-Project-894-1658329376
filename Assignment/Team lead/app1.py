from flask import Flask,url_for,render_template


app = Flask(__name__)

@app.route('/signup')
def  signup():
    return render_template("signup.html")

if __name__ == '__main__':
   app.run(host='0.0.0.0',port=8080,debug=True)
