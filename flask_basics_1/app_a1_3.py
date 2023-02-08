from flask import Flask


app = Flask(__name__)


@app.route('/page1')
def hello_world():
    return 'Hello World'


@app.route('/page2')
def hello_world2():
    return '<h1>Hello its a header</h1>'


@app.route('/page3')
def hello_world3():
    return '<p>Hello its a para</p>'


if __name__ == '__main__':
    app.run(debug=False)

