import flask
from flask import *

app = flask.Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/orders/1')
def order_credit_repair():
    # if session.get('logged_in'):
        return render_template('order_credit_repair.html')
    # else:
    #     return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
