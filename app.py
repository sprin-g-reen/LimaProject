import flask, os
from flask import *
from db import db
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__,
        static_folder = os.path.abspath('assets'),
        template_folder = os.path.abspath('templates')
)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#app.config["UPLOAD_FOLDER"] = "uploads/"
app.config["DEBUG"] = True


@app.route('/', methods=["GET","POST"])
def index():
    if request.method == 'POST': 
        # subcribe to email 
        data = request.form.to_dict()
        email = data.get('email')
        return render_template('index.html')
    return render_template('index.html')

@app.route('/becomeaffiliate', methods=["GET", "POST"])
def becomeaffiliate():
    if request.method == 'POST':
        print(request.form)
        data = request.form.to_dict()
    return render_template('becomeaffiliate.html')

@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')

@app.route('/fixnflip', methods=["GET"])
def fixnflip():
    return redirect("https://lit-cove-35411.herokuapp.com/applications/fix-n-flip/0015w00002nt2oFAAQ")

# line of credit
@app.route('/loc', methods=["GET"])
def loc():
    return redirect("https://lit-cove-35411.herokuapp.com/applications/line-of-credit/0015w00002nt2oFAAQ")

# rental
@app.route('/rental', methods=["GET"])
def rental():
    return redirect("https://lit-cove-35411.herokuapp.com/applications/rental/0015w00002nt2oFAAQ")


# @app.route('/contact', methods=["GET", "POST"])
# def contact():
#     if request.method == 'POST':
#         print(request.form)
#         data = request.form.to_dict()
#         # TODO
#         return render_template('contact.html')
#   
#     return render_template('contact.html')


@app.route('/refer')
def refer():
    return render_template('referalP.html')

@app.route('/broker')
def broker():
    return render_template('brokerP.html')

@app.route('/creditform', methods=["GET","POST"])
def creditform():
    if request.method == 'POST':
        # TODO
        print(request.form)

    return render_template('creditform.html')


'''
@app.route('/orders/1')
def order_credit_repair():
    # if session.get('logged_in'):
        #return render_template('order_credit_repair.html')
    # else:
    #     return render_template('login.html')
'''


if __name__ == '__main__':
    app.run(debug=True)
