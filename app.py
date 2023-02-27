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


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route("/logout", methods=["GET"])
def logout():
    session['email'] = None 
    return redirect(url_for("index"))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        print(request.form)
        data = request.form.to_dict()
        email = data.get('Email')
        password = data.get('Password')
        print(f"{email}:{password}")
        x = db.users.find_one({"email":email})
        if x and check_password_hash(x.get('password'), password):
            session['email'] = x.get('email')
            return redirect(url_for('index'))
        else:
            print("Wrong pass")
    return render_template('login.html')

@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        print(request.form)
        data = request.form.to_dict()
        name = data.get("Name")
        email = data.get('Email')
        password = data.get('Password')
        print(f"{email}:{password}")
        x = db.users.find_one({"email":email})
        if x:
            # alredy exists message and redirect to login

            return redirect(url_for('login'))
        
        db.users.insert_one({"name":name, "email":email.lower(), "password":generate_password_hash(password, method='sha256')})
        return redirect(url_for('login'))
    return render_template('login.html') # register.html here

@app.route('/refer')
def refer():
    return render_template('referalP.html')

@app.route('/broker')
def broker():
    return render_template('brokerP.html')

@app.route('/creditform', methods=["GET","POST"])
def creditform():
    if request.method == 'POST':
        print(request.form)

    return render_template('creditform.html')


@app.route('/orders/1')
def order_credit_repair():
    # if session.get('logged_in'):
        return render_template('order_credit_repair.html')
    # else:
    #     return render_template('login.html')



if __name__ == '__main__':
    app.run(debug=True)
