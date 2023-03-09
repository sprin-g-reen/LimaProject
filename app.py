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

#login 
@app.route('/login', methods=["GET"])
def login():
    return redirect("https://www.secureclientaccess.com/")


@app.route('/becomeaffiliate', methods=["GET", "POST"])
@app.route('/becomeaffiliate.html', methods=["GET", "POST"])
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

@app.route('/Login-static/<path:path>')
def send_static_files(path):
    return send_from_directory('Login-static', path)

@app.route("/static/<path:path>")
def static_files_static_folder(path):
    return send_from_directory(os.path.join("Login-static", "static"), path)

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
        print(request.form)

    return render_template('creditform.html')

@app.route('/creditform/2', methods=["GET","POST"])
def credit_form():
    if request.method == 'POST':
        # TODO this accet one input, then set coupon to session and redirect to final payment page
        print(request.form)

    return render_template('request-credit.html')

# final-preview
@app.route('/final-preview', methods=["GET","POST"])
def final_preview():
    if request.method == 'POST':
        # TODO
        print(request.form)

    return render_template('final-preview.html') # username, phoneNumber, prixzse, price_final, price_final_tax, promos(t/f)


# apply_coupon post
@app.route('/apply_coupon', methods=["POST"])
def apply_coupon():
    if request.method == 'POST':
        # validate and return status code as output... 200 is success
        # also add it to session if success
        return jsonify({'status': 'success'})
    

    return render_template('final-preview.html')


@app.route('/cc', methods=['GET'])
def cc():
    return render_template('cc.html')

#success
@app.route('/success', methods=["GET"])
def success():

    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
