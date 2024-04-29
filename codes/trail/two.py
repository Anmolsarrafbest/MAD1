from flask import Flask
import flask
app = Flask(__name__)

@app.route("/")
def home():
    return flask.render_template('home.html') 
@app.route("/home")
def home2():
    return 'Welcome'
if __name__=='__main__':
    app.run(debug=True) 

print(5)    