from flask import Flask


app = Flask(__name__)


@app.route('/contactus')
def hello_world():
    return 'Hello this is Contact Us'


@app.route('/home')
def hello_world2():
    return '<h1>Hello its our Home</h1>'

@app.route('/age/<age>')
def hello_world5(age):
    return '<h1>okay your age is %s</h1>'%age


@app.route('/aboutus')
def hello_world3():
    return '<p>Hello its About Us</p>'

@app.route('/location')
def hello_world4():
    return '<p>Hello its Location</p>'


if __name__ == '__main__':
    app.run(debug=False)
