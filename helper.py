import imp
from email_words import *
from smtplib import SMTP
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import requests
from authorizenet import apicontractsv1
from authorizenet.apicontrollers import createTransactionController
from authorizenet.apicontrollers import *
from decimal import *
from datetime import *
from collections.abc import MutableSequence


def register_send_email(email, username):
    me = "no-reply@amecocapital.com"
    you = email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Welcome to AmeCo Capital {username}"
    msg['From'] = me
    msg['To'] = you
    html = register_words_for_email
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    server = SMTP('smtp.siteprotect.com', 587)
    server.starttls()
    server.login("no-reply@amecocapital.com", "BillGates2004@")
    server.sendmail(me, you, msg.as_string())
    server.quit()
    return True


def pyment_rcved(email, username, amount, order_id, trx, date):
    me = "no-reply@amecocapital.com"
    you = email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Payment Received"
    msg['From'] = me
    msg['To'] = you
    html = payment_recved.format(
        username, amount, order_id, trx, date)
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    server = SMTP('smtp.siteprotect.com', 587)
    server.starttls()
    server.login("no-reply@amecocapital.com", "BillGates2004@")
    server.sendmail(me, you, msg.as_string())
    server.quit()
    return True


def order_failed(email, username, order_id, body):
    me = "no-reply@amecocapital.com"
    you = email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Order Failed"
    msg['From'] = me
    msg['To'] = you
    html = rejct_emai.format(username, order_id, body)
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    server = SMTP('smtp.siteprotect.com', 587)
    server.starttls()
    server.login("no-reply@amecocapital.com", "BillGates2004@")
    server.sendmail(me, you, msg.as_string())
    server.quit()
    return True


def order_verifeied(email, username, order_id):
    me = "no-reply@amecocapital.com"
    you = email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Order Verified and Deliverd"
    msg['From'] = me
    msg['To'] = you
    html = aprved_emai.format(username, order_id)
    part2 = MIMEText(html, 'html')
    msg.attach(part2)
    server = SMTP('smtp.siteprotect.com', 587)
    server.starttls()
    server.login("no-reply@amecocapital.com", "BillGates2004@")
    server.sendmail(me, you, msg.as_string())
    server.quit()
    return True


"""
    # if not session.get('logged_in_by_admin'):
    #     return redirect(url_for('admin_login'))

    /reject/{{dat[i][0]}}/{{dat[i][1]}}
"""


def credit_repair_cloud_add_data(fname, lname, email, mobilenumber, mailing_addy, city, state, zip_s, lastfour,dib):
    data = f"""
<crcloud>
  <lead>
    <type>Client</type>
    <firstname>{fname}</firstname>
    <lastname>{lname}</lastname>
    <email>{email}</email>
    <phone_mobile>{mobilenumber}</phone_mobile>
    <street_address>{mailing_addy}</street_address>
    <city>{city}</city>
    <state>{state}</state>
    <zip>{zip_s}</zip>
    <ssno>{lastfour}</ssno>
    <birth_date>{dib}</birth_date>
    <client_assigned_to>Carlos Corbin</client_assigned_to>
    <client_portal_access>on</client_portal_access>
    <client_userid>{email}</client_userid>
    <client_agreement>ameco-capital-site</client_agreement>
    <send_setup_password_info_via_email>yes</send_setup_password_info_via_email>
  </lead>
</crcloud>
    """
    x = requests.post(f'https://app.creditrepaircloud.com/api/lead/insertRecord?apiauthkey=np+kn6GlzLC/scyun7rMwJ+unw==&secretkey=359033231347C326DFB1CECAC8104516&xmlData={data}')
    print(x.text)
    return True

CONSTANTS = imp.load_source('modulename', 'constants.py')

def charge_credit_card(amount, cc_num, expiry, cvv, inv_id, fname, lname, baddy, caity, sts, zp, cunty):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = CONSTANTS.apiLoginId
    merchantAuth.transactionKey = CONSTANTS.transactionKey
    creditCard = apicontractsv1.creditCardType()
    creditCard.cardNumber = cc_num
    creditCard.expirationDate = expiry
    creditCard.cardCode = cvv
    payment = apicontractsv1.paymentType()
    payment.creditCard = creditCard
    order = apicontractsv1.orderType()
    order.invoiceNumber = f"{inv_id}"
    order.description = "Payment of Invoice"
    customerAddress = apicontractsv1.customerAddressType()
    customerAddress.firstName = fname
    customerAddress.lastName = lname
    customerAddress.address = baddy
    customerAddress.city = caity
    customerAddress.state = sts
    customerAddress.zip = zp
    customerAddress.country = "US"
    transactionrequest = apicontractsv1.transactionRequestType()
    transactionrequest.transactionType = "authCaptureTransaction"
    transactionrequest.currencyCode = "USD"
    transactionrequest.amount = amount
    transactionrequest.payment = payment
    transactionrequest.order = order
    createtransactionrequest = apicontractsv1.createTransactionRequest()
    createtransactionrequest.merchantAuthentication = merchantAuth
    createtransactionrequest.refId = "MerchantID-0001"
    createtransactionrequest.transactionRequest = transactionrequest
    createtransactioncontroller = createTransactionController(createtransactionrequest)
    # createtransactioncontroller.setenvironment(CONSTANTS.PRODUCTION)
    createtransactioncontroller.execute()
    response = createtransactioncontroller.getresponse()
    if response is not None:
        if response.messages.resultCode == "Ok":
            if hasattr(response.transactionResponse, 'messages') is True:
                return [response.transactionResponse.transId, response.transactionResponse.responseCode, response.transactionResponse.messages.message[0].code, response.transactionResponse.messages.message[0].description]
            else:
                print(response.transactionResponse.errors.error[0].errorCode, response.transactionResponse.errors.error[0].errorText)
                if hasattr(response.transactionResponse, 'errors') is True:
                    return [response.transactionResponse.errors.error[0].errorCode, response.transactionResponse.errors.error[0].errorText]
        else:
            print('Failed Transaction. 2')
            if hasattr(response, 'transactionResponse') is True and hasattr(
                    response.transactionResponse, 'errors') is True:
                return [response.transactionResponse.errors.error[0].errorCode, response.transactionResponse.errors.error[0].errorText]
            else:
                return [response.messages.message[0]['code'].text, response.messages.message[0]['text'].text]
    else:
        return ['Error Response 3']

def charge_credit_card_monthly(amount, invid, ccnum, exp, cvv, fname, lname, baddy, caity, sate, zp):

    # Setting the merchant details
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = CONSTANTS.apiLoginId
    merchantAuth.transactionKey = CONSTANTS.transactionKey
    # Setting payment schedule
    paymentschedule = apicontractsv1.paymentScheduleType()
    paymentschedule.interval = apicontractsv1.paymentScheduleTypeInterval() #apicontractsv1.CTD_ANON() #modified by krgupta
    paymentschedule.interval.length = 5
    paymentschedule.interval.unit = apicontractsv1.ARBSubscriptionUnitEnum.months
    year, month, dae = datetime.now().year, datetime.now().month, datetime.now().day
    paymentschedule.startDate = datetime(year, month, dae)
    paymentschedule.totalOccurrences = 5
    paymentschedule.trialOccurrences = 0
    # Giving the credit card info
    creditcard = apicontractsv1.creditCardType()
    creditcard.cardNumber = ccnum
    creditcard.expirationDate = exp
    creditcard.cardCode = cvv
    payment = apicontractsv1.paymentType()
    payment.creditCard = creditcard
    # Setting billing information
    billto = apicontractsv1.nameAndAddressType()
    billto.firstName = fname
    billto.lastName = lname
    billto.address = baddy
    billto.city = caity
    billto.state = sate
    billto.zip = zp
    billto.country = "US"
    # Setting subscription details
    subscription = apicontractsv1.ARBSubscriptionType()
    subscription.name = f"Credit Report Subscription {invid}"
    subscription.paymentSchedule = paymentschedule
    subscription.amount = amount
    subscription.trialAmount = Decimal('0.00')
    subscription.billTo = billto
    subscription.payment = payment
    # Creating the request
    request = apicontractsv1.ARBCreateSubscriptionRequest()
    request.merchantAuthentication = merchantAuth
    request.subscription = subscription
    # Creating and executing the controller
    controller = ARBCreateSubscriptionController(request)
    controller.execute()
    # Getting the response
    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print ("SUCCESS:")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % str(response.messages.message[0]['text'].text))
        print ("Subscription ID : %s" % response.subscriptionId)
        response = ["Success", 1, response.subscriptionId]
    else:
        print ("ERROR:")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)
        response = ["Error", 2,response.messages.message[0]['text'].text]

    print("Check: ",response)
    return response

#print(charge_credit_card_monthly("50", "SSH", ("6011000000000012"), "12/25", "345", "DFH", "LFH", "23, CA, SAN", "SAN", "CA", "10080"))
# print(charge_credit_card("90", "4111111111111111", "12/23","900", "900", "Joahn", "SKSK", "SJD, SKKS, LL", "SLM", "KKS", "10080", "USA"))


def cancel_subscription(subscriptionId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = CONSTANTS.apiLoginId
    merchantAuth.transactionKey = CONSTANTS.transactionKey

    request = apicontractsv1.ARBCancelSubscriptionRequest()
    request.merchantAuthentication = merchantAuth
    request.refId = "Credit Report Subscription"
    request.subscriptionId = subscriptionId

    controller = ARBCancelSubscriptionController(request)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print ("SUCCESS")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)
    else:
        print ("ERROR")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)

    return response



def update_subscription(subscriptionId):
    merchantAuth = apicontractsv1.merchantAuthenticationType()
    merchantAuth.name = constants.apiLoginId
    merchantAuth.transactionKey = constants.transactionKey

    creditcard = apicontractsv1.creditCardType()
    creditcard.cardNumber = "4111111111111111"
    creditcard.expirationDate = "2035-12"

    payment = apicontractsv1.paymentType()
    payment.creditCard = creditcard

    #set profile information
    profile = apicontractsv1.customerProfileIdType()
    profile.customerProfileId = "121212"
    profile.customerPaymentProfileId = "131313"
    profile.customerAddressId = "141414"

    subscription = apicontractsv1.ARBSubscriptionType()
    subscription.payment = payment
    #to update customer profile information
    #subscription.profile = profile

    request = apicontractsv1.ARBUpdateSubscriptionRequest()
    request.merchantAuthentication = merchantAuth
    request.refId = "Sample"
    request.subscriptionId = subscriptionId
    request.subscription = subscription

    controller = ARBUpdateSubscriptionController(request)
    controller.execute()

    response = controller.getresponse()

    if (response.messages.resultCode=="Ok"):
        print ("SUCCESS")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)
    else:
        print ("ERROR")
        print ("Message Code : %s" % response.messages.message[0]['code'].text)
        print ("Message text : %s" % response.messages.message[0]['text'].text)

    return response

