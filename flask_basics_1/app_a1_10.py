from flask import *
app = Flask(__name__)


@app.route('/home')
def home():
    return "<h1>This is my home</h1>"


@app.route('/location')
def location():
    return "<h1>This is my location</h1>"


def chef_welcome():
    return "<h1>Welcome to this chef page</h1>"
app.add_url_rule("/chef_welcome_link", "chef_welcome_endpoint", chef_welcome)


def cust_welcome():
    return "<h1>Welcome to this customer page</h1>"
app.add_url_rule("/cust_welcome", "cust_welcome", cust_welcome)


@app.route('/login/<role>')
def login(role):
    if role == "chef":
        return redirect(url_for('chef_welcome_endpoint'))

    elif role == "customers":
        return redirect(url_for('cust_welcome'))


if __name__ == "__main__":
    app.run(debug=False)
