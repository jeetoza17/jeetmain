from flask import *
app = Flask(__name__)



@app.route('/about')
def about():
    return "This is about page"
app.add_url_rule("/about","about",about)


@app.route('/about/<text>')
def about1(text):
    return "This is about page %s"%text
app.add_url_rule("/about/<text>","about",about)


@app.route('/admin')
def admin():
    return "admin"
app.add_url_rule("/admin","admin",admin)


@app.route('/librarion')
def librarion():
    return "librarion"
app.add_url_rule("/librarion","librarion",librarion)


@app.route('/student')
def student():
    return "student"
app.add_url_rule("/student","student",student)


@app.route('/ceo')
def ceo():
    return "Welcome CEO"
app.add_url_rule("/ceo","ceo",ceo)


@app.route('/clients')
def clients():
    return "Welcome Clients"
app.add_url_rule("/clients","clients",clients)

@app.route('/employees')
def employees():
    return "Welcome Employees"
app.add_url_rule("/employees","employees",employees)



#@app.route('/ceo')
def ceo_loggedin():
    return "You are officially logged in for viewing classified info."
app.add_url_rule("/ceo_loggedin","ceo_loggedin",ceo_loggedin)


#@app.route('/clients')
def clients_loggedin():
    return "Welcome to Stratacent."
app.add_url_rule("/clients_loggedin","clients_loggedin",clients_loggedin)


#@app.route('/employees')
def employees_loggedin():
    return "Welcome to your CRM"
app.add_url_rule("/employees_loggedin","employees_loggedin",employees_loggedin)

if __name__ == '__main__':
    app.run(debug=False)



@app.route('/login/<role>/<int:id>')
def login(role,id):
    if role == 'clients' and (9000<id<9999):
        return redirect(url_for('clients_loggedin'))
    if role == 'employees':
        return redirect(url_for('employees_loggedin'))


    if __name__ == "__main__":
        app.run(debug = True)            















