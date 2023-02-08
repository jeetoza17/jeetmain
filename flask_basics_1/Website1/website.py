from flask import *
app = Flask(__name__) 



@app.route('/')
def message():
    return render_template('frontpage.html') 


@app.route('/deals')
def message1():
    return render_template('dealspage.html') 

@app.route('/error')
def message2():
    return render_template('errorpage.html') 



if __name__ == '__main__':

    app.run(debug=False)