import flask, os
from flask import *
from db import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__,
        static_folder = os.path.abspath('assets'),
        template_folder = os.path.abspath('templates')
)

app.secret_key = 'ssssss'
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
#app.config["UPLOAD_FOLDER"] = "uploads/"
app.config["DEBUG"] = True

db = db()

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

# subscribe 
@app.route('/subscribe', methods=["POST"])
def subscribe():
    if request.method == 'POST':
        data = request.form.to_dict()
        email = data.get('email')
        db.users.update_one({"email":email}, {"$set":{"email":email}}, upsert=True)
        return jsonify({'status': 'success'})

#login 
@app.route('/login', methods=["GET"])
def login():
    return redirect("https://www.secureclientaccess.com/")


@app.route('/about', methods=["GET"])
def about():
    return render_template('about.html')



@app.route('/fixnflip', methods=["GET", "POST"])
def fixnflip():
    if request.method == 'POST':
        print(request.form)
        data = request.form.to_dict()
        # TODO
    return render_template('fixnflip.html')

    #return redirect("https://lit-cove-35411.herokuapp.com/applications/fix-n-flip/0015w00002nt2oFAAQ")

# line of credit
@app.route('/loc', methods=["GET"])
def loc():
    return redirect("https://lit-cove-35411.herokuapp.com/applications/line-of-credit/0015w00002nt2oFAAQ")

# rental
@app.route('/rental', methods=["GET"])
def rental():
    return redirect("https://lit-cove-35411.herokuapp.com/applications/rental/0015w00002nt2oFAAQ")


@app.route('/contact', methods=["GET", "POST"])
def contact():
    if request.method == 'POST':
        print(request.form)
        data = request.form.to_dict()
        # TODO
        return render_template('contact.html')
  
    return render_template('contact.html')

@app.route('/Login-static/<path:path>')
def send_static_files(path):
    return send_from_directory('Login-static', path)

@app.route("/static/<path:path>")
def static_files_static_folder(path):
    return send_from_directory(os.path.join("Login-static", "static"), path)

@app.route('/becomeaffiliate', methods=["GET"])
@app.route('/refer', methods=["GET"])
def refer():
    return render_template('referalP.html')

@app.route('/broker', methods=["GET"])
def broker():
    return render_template('brokerP.html')


@app.route('/termsandconditions', methods=["GET"])
def termsandconditions():
    return render_template('termsandconditions.html')

@app.route('/creditform', methods=["GET","POST"])
def creditform():
    if request.method == 'POST':
        # TODO.. get data, set it to session, and send to the next page to apply coupon
        session['id'] = uuid4()
        session['data'] = request.form.to_dict()
        # print(request.form)
        return redirect(url_for('credit_form'))
    session["id"] = None
    session["data"] = None
    return render_template('creditform.html')

@app.route('/creditform/2', methods=["GET","POST"])
def credit_form():
    if request.method == 'POST':
        # this accet one input, then set coupon to session and redirect to final payment page
        id = session.get('id')
        data = session.get('data')
        if not id:
            return redirect(url_for('creditform'))
        for key, value in request.form.items():
            data[key] = value
        session['data'] = data
        data = session.get('data')
        return redirect(url_for('final_preview'))

    return render_template('request-credit.html')

# final-preview
@app.route('/final-preview', methods=["GET","POST"])
def final_preview():
    data = session.get('data')
    if request.method == 'POST':
        if not data:
            return redirect(url_for('creditform'))
        
        print(data)
        # print(request.form)


    return render_template('final-preview.html') 
# username, phoneNumber, prixzse, price_final, price_final_tax, promos(t/f)


# apply_coupon post
@app.route('/apply_coupon', methods=["POST"])
def apply_coupon():
    if request.method == 'POST':
        return Response(
            '', 
            status=200 if db.coupons.find_one({"code":request.json.get('coupon_code', "none")})  else 498
        ) 

    return render_template('final-preview.html')


@app.route('/cc', methods=['GET'])
def cc():
    return render_template('cc.html')

#success
@app.route('/success', methods=["GET"])
def success():

    return render_template('success.html')

@app.route('/failed', methods=["GET"])
def failed():

    return render_template('failed.html')

if __name__ == '__main__':
    app.run(debug=True)
