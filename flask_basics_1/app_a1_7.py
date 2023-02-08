from flask import *
app = Flask(__name__)


@app.route('/home/<int:age>')
def home(age):
    return "<h1>Age = %d </h1>" %age

@app.route('/home1/<text>/<int:age>')
def home1(text,age):
    return f"<h1>age = {age} and text = {text}</h1>"



if __name__ == "__main__":
    app.run(debug=False)
