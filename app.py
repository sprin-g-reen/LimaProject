import flask, os, random, string
from flask_mail import Mail, Message
from flask import *
from db import db
from uuid import uuid4
from werkzeug.security import generate_password_hash, check_password_hash
# from helper import charge_credit_card
from pyxb.exceptions_ import *



app = Flask(__name__,
        static_folder = os.path.abspath('assets'),
        template_folder = os.path.abspath('templates')
)


app.config['MAIL_SERVER'] = 'smtp-relay.sendinblue.com'
app.config['MAIL_PORT'] = 587
# app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USERNAME'] = 'xxx@gmail.com'
app.config['MAIL_PASSWORD'] = 'xxx'

mail = Mail(app)

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
        # print(request.form)
        data = request.form.to_dict()
        name = request.form['name']
        message = request.form['message']
        message = f"Email : {data.get('email')} \n"
        message += f"Name : {data.get('name')} \n"
        message += f"Phone : {data.get('phnum')} \n"
        message += f"Message : {data.get('message')} \n"
        msg = Message(subject='New Contact Form Entry!',
                sender="no_reply@contactform.com",
                recipients=['owner@gmail.com'],
                body=message)

        mail.send(msg)
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
        session['id'] = uuid4()
        session['data'] = request.form.to_dict()
        print(request.form)
        return redirect(url_for('credit_form'))
    session["id"] = None
    session["data"] = None
    return render_template('creditform.html')

@app.route('/creditform/2', methods=["GET","POST"])
def credit_form():
    if request.method == 'POST':
        id = session.get('id')
        if not id:
            return redirect(url_for('creditform'))
        

        data = session.get('data')
        # add new data to session data 
        for key, value in request.form.items():
            data[key] = value
        session['data'] = data
        

        return redirect(url_for('final_preview'))
    return render_template('request-credit.html')

# final-preview
@app.route('/final-preview', methods=["GET","POST"])
def final_preview():

    data = session.get('data')
    if not data:
        return redirect(url_for('creditform'))
    
    if request.method == 'POST':
        return redirect(url_for('cc'))
    
    def calculateStateTax(price):
        state_sales_tax = .09
        return price * state_sales_tax
    
    price = 150 # this part is still undone
    final_price = price
    if data['couponcode'] != "none":
        final_price -= 100
    price_final_tax = final_price + calculateStateTax(final_price)
    data['price_final_tax'] = price_final_tax
    data['transc_id'] = ''.join(random.choices(
            string.ascii_uppercase + string.digits, k=16))
    
    # save all to session again
    session['data'] = data
    return render_template('final-preview.html', name=data['fname'], phoneNumber=data['phnum'],
                            prixzse=price,promos=final_price, price_final_tax=price_final_tax) 



@app.route('/apply_coupon', methods=["POST"])
def apply_coupon():
    if request.method == 'POST':
        return Response(
            '', 
            status=200 if db.coupons.find_one({"code":request.json.get('coupon_code', "none")})  else 498
        ) 

    return render_template('final-preview.html')


@app.route('/cc', methods=['GET','POST'])
def cc():
    if request.method == 'POST':
        data = session.get('data')
        if not data:
            return redirect(url_for('creditform'))
        
        print(request.form)
        fname = request.form.get('fname')
        lname = request.form.get('lname')
        ccnum = request.form.get('ccnum')
        exp = request.form.get('exp')
        cvv = request.form.get('cvv')
        addyeres = request.form.get('addyeres')
        city = request.form.get('city')
        zip = request.form.get('zip')
        state = request.form.get('state')
        country = request.form.get('country')
        def remove(string):
            return string.replace(" ", "")
        ccnum = remove(ccnum)
        exp = remove(exp)
        cvv = remove(cvv)

        # jaaa = charge_credit_card(data('price_final_tax'), ccnum, exp, cvv, data['transc_id'], fname, lname, addyeres, city, state, zip, country)
        jaaa = 0 # payment thing is crashing code
        try:
            if jaaa[1] == "1" or jaaa[1] == 1:
                session["payment_done"] = True

                return redirect(url_for('success'))
            elif jaaa[0] == "2" or jaaa[0] == 2:
                return render_template('cc.html', error=jaaa)
            elif "this transaction has been declined" in jaaa:
                return render_template('cc.html', error='Transaction Declined Please Try Again')
            elif jaaa[0] == "Error Response":
                return render_template('cc.html', error='Your Card is Declined')
            else:
                return render_template('cc.html', error=jaaa)
        except IndexError:
            return render_template('cc.html', error="Your card is declined, Transaction Failed.")
        except TypeError:
            return render_template('cc.html', error="Your card is declined, Transaction Failed.")
        except ValueError:
            return render_template('cc.html', error="Your card is declined, Transaction Failed.")
        except pyxb.exceptions_.SimpleFacetValueError:
            return render_template('cc.html', error="Your card/cvv/expiry date is in-correct or declined, Transaction Failed.")
        except Exception as e:
            return render_template('cc.html', error="Transaction Failed: " + str(e))
        
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
