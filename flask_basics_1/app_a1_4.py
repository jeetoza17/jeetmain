from flask import Flask


app = Flask(__name__)

@app.route('/page1/<city>')
def hello_world(city):
    return 'Hello %s'%city

@app.route('/page2/<name>')
def hello_world1(name):
    return 'Hello %s'%name


if __name__ == '__main__':

    app.run(debug=False)
