from flask import *
app = Flask(__name__)


#@app.route('/employees')
def employees_loggedin():
    return "Welcome to your CRM"
app.add_url_rule("/employees_loggedin","employees_loggedin",employees_loggedin)

#@app.route('/clients')
def clients_loggedin():
    return "Welcome to Stratacent."
app.add_url_rule("/clients_loggedin","clients_loggedin",clients_loggedin)



@app.route('/login/<role>/<int:id>')
def login(role,id):    
    if role == 'clients' and (9000<id<9999):
        return redirect(url_for('clients_loggedin'))       
    if role == 'employees':
        return redirect(url_for('employees_loggedin'))

if __name__ == "__main__":
    app.run(debug=False)