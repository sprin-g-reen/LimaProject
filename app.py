import flask, os
from flask import *

app = Flask(__name__,
        static_folder = os.path.abspath('assets'),
        template_folder = os.path.abspath('templates')
)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#app.config["UPLOAD_FOLDER"] = "uploads/"
app.config["DEBUG"] = True


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
