from flask import *
app = Flask(__name__)


def success_func(name):
    return "welcome %s" %name


@app.route('/login',methods = ['POST','GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
app.add_url_rule("/success/<name>","success",success_func)

if __name__ == "__main__":
    app.run(debug=False)
