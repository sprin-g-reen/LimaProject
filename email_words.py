register_words_for_email = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <meta name="format-detection" content="telephone=no">
    <title>Registration Confirmed</title>
    <style>
        @import url("https://fonts.googleapis.com/css?family=Varela+Round");

        * {
            margin: 0;
            padding: 0;
            font-family: Varela Round, "Segoe UI", "Arial", "san serif";
        }

        img {
            display: inline-block;
        }

        .container {
            max-width: 500px;
            margin: 20px auto;
            border-radius: 4px;
            border: 1px solid rgba(0, 0, 0, 0.1);
            min-height: 100px;
            position: relative;
        }

        .container::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 3px;
            background: linear-gradient(to right, #0267C1, #D65108);
        }

        .logo {
            display: flex;
            margin: 30px auto 0;
            align-items: center;
            justify-content: center;
        }

        .logo a {
            display: block;
            width: 30px;
            height: 30px;
        }

        .logo img {
            width: 180px;
        }

        .logo .c-name {
            display: inline-block;
            font-weight: 600;
        }

        .thumbs {
            width: 100px;
            margin: auto;
            height: 136px;
        }

        .thumbs img {
            width: 100%;
        }

        .illustration {
            width: 100%;
            text-align: center;
            box-shadow: 0 10px 20px -5px rgba(0, 0, 0, 0.05);
            border-radius: 0 0 50% 50%/1%;
            text-align: center;
        }

        .illustration img {
            width: 70%;
            margin: 50px auto;
        }

        .separator {
            display: block;
            height: 3px;
            width: 70%;
            margin: 10px auto;
            background-color: rgba(0, 0, 0, 0.05);
            border-radius: 10px;
            position: relative;
            overflow: hidden;
        }

        .separator::before,
        .separator::after {
            content: "";
            position: absolute;
            left: 0;
            top: 0;
            height: 100%;
            width: 33%;
            border-radius: inherit;
            opacity: 0.05;
        }

        .separator::before {
            left: 0;
            background: #EFA00B;
        }

        .separator::after {
            left: initial;
            right: 0;
            background: #D65108;
        }

        .hgroup {
            text-align: center;
            padding: 50px 30px 30px;
        }

        .name {
            display: block;
            color: #0267C1;
            font-weight: 600;
            font-size: 1.1rem;
        }

        .hgroup h1 {
            font-size: 20px;
            font-weight: 600;
            color: #333;
        }

        .hgroup h2 {
            font-size: 19px;
        }

        .hgroup p {
            font-size: 15px;
            color: slategrey;
            margin-top: 15px;
            text-align: justify;
            line-height: 25px;
        }

        .items {
            padding: 30px;
            display: grid;
            grid-template-columns: repeat(2, 1fr);
        }

        .item {
            margin-bottom: 10px;
            text-align: center;
            width: 100%;
            margin: 0 auto 50px;
        }

        .item .icon {
            margin-bottom: 10px;
        }

        .item .icon img {
            width: 80px;
        }

        .item .title {
            margin-bottom: 5px;
            font-size: 16px;
            font-weight: 600;
        }

        .item .subtitle {
            font-size: 13px;
            color: slategrey;
            padding: 1rem;
        }

        .button-wrap {
            text-align: center;
            padding: 2rem;
        }

        button.explore {
            padding: 15px 25px;
            font: inherit;
            background: linear-gradient(to right, #0267C1, #0280EF);
            border-radius: 50px;
            border: 0;
            color: #fff;
            margin: auto;
            display: inline-block;
            transition: all 0.2s ease-in-out;
            cursor: pointer;
            box-shadow: 0 5px 10px rgba(0, 0, 0, 0.1);
        }

        button.explore:hover {
            transform: translateY(-5px);
            box-shadow: 0 15px 10px -7px rgba(0, 0, 0, 0.1);
        }

        footer {
            font-size: 12px;
            color: slategrey;
            text-align: center;
            padding: 30px;
        }

        .rad {
            margin: 0 !important;
            text-align: center !important;
            font-size: 18px !important;
        }

        .raised {
            font-size: 16px;
            color: #777;
            display: block;
            color: steelblue;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="logo"><img src="https://te.legra.ph/file/73e88627291b407a14f8c.jpg" alt="cc-logo" border="0">
        </div>
        <div class="illustration">
            <div class="hgroup">
                <span class="name">Hello, {}</span>
                <h1>Thank you for Signing Up</h1>
                <div class="thumbs">
                    <a href="https://imgbb.com/"><img src="https://i.ibb.co/2g7tS2d/good.png" alt="good" border="0"></a>
                </div>
                <p class="rad">You're in, now with a part of Ameco Capitals</p>
            </div>
        </div>

        <div class="hgroup">
            <p>
                We feel Very happy that you've trusted us, and made a acount with us, to enjoy our services. we hope we
                will
                keep you exceptions come true. please let us know if you've any questions
                <br><br>
            <p>
                <span class="raised">Hold up, there's more!</span>
                We feel so proud on giving our products cheap.
            </p>
            <p>If you have any questions, kindly reach out to our team on admin@amecocapital.com.</p>

            <p>Have an AWESOME day! <br>
                Brought to you by your friends at Ameco Capital.
            </p>
            </p>

        </div>
        <div class="hgroup">
            <h2>What we offer</h2>
        </div>
        <div class="items">
            <div class="item">
                <div class="icon">
                    <img src="https://te.legra.ph/file/bbdfee8f3ca627f96f8a2.jpg" alt="desktop" border="0">
                </div>
                <div class="title">Credit Repair</div>
                <div class="subtitle">
                    Credit Repair, is what all you're finance speaks up. so if you're not satisified with your Credit
                    Score,
                    we will help you out to fix that score.
                </div>
            </div>
            <div class="item">
                <div class="icon">
                    <img src="https://te.legra.ph/file/1e86f6049cb6bdd0ccd4e.jpg" alt="smartphone" border="0">
                </div>
                <div class="title">Loans</div>
                <div class="subtitle">
                    Sometimes, Finance is the only thing stops us. we got your back, Don't Worry we are here to help you
                    out.
                </div>
            </div>
        </div>
        <div class="button-wrap">
            <a href="https://amecocapital.com/letsgooo" target="_blank">
                <button class="explore">
                    Explore
                </button>
            </a>
        </div>
        <footer>
            Ameco Capital Inc © 2019
            <br>
            Atlanta Georgia USA.
            <br>
            Tel: +1 470 452-1921
        </footer>
    </div>
</body>

</html>
"""

payment_recved = """

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<html style="-moz-osx-font-smoothing: grayscale; -webkit-font-smoothing: antialiased; background-color: #464646; margin: 0; padding: 0;">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
        <meta name="format-detection" content="telephone=no">
        <title>Payment Confirmed</title>
        
    </head>
    <body bgcolor="#d7d7d7" class="generic-template" style="-moz-osx-font-smoothing: grayscale; -webkit-font-smoothing: antialiased; background-color: #d7d7d7; margin: 0; padding: 0;">
        <!-- Header Start -->
        <div class="bg-white header" bgcolor="#ffffff" style="background-color: white; width: 100%;">
            <table align="center" bgcolor="#ffffff" style="border-left: 10px solid white; border-right: 10px solid white; max-width: 600px; width: 100%;">
                <tr height="80">
                    <td align="left" class="vertical-align-middle" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: middle;">
                        <a href="https://www.amecocapital.com/" target="_blank" style="-webkit-text-decoration-color: #F16522; color: #F16522; text-decoration: none; text-decoration-color: #F16522;">
                            <img src="https://te.legra.ph/file/73e88627291b407a14f8c.jpg" alt="Ameco Capital" width="70" style="border: 0; font-size: 0; margin: 0; max-width: 100%; padding: 0;">
                        </a>
                    </td>
                </tr>
            </table>
        </div>
        <!-- Header End -->

        <!-- Content Start -->
        <table cellpadding="0" cellspacing="0" cols="1" bgcolor="#d7d7d7" align="center" style="max-width: 600px;">
            <tr bgcolor="#d7d7d7">
                <td height="50" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
            </tr>

            <!-- This encapsulation is required to ensure correct rendering on Windows 10 Mail app. -->
            <tr bgcolor="#d7d7d7">
                <td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;">
                    <!-- Seperator Start -->
                    <table cellpadding="0" cellspacing="0" cols="1" bgcolor="#d7d7d7" align="center" style="max-width: 600px; width: 100%;">
                        <tr bgcolor="#d7d7d7">
                            <td height="30" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                        </tr>
                    </table>
                    <!-- Seperator End -->

 <!-- Generic Pod Left Aligned with Price breakdown Start -->
                    <table align="center" cellpadding="0" cellspacing="0" cols="3" bgcolor="white" class="bordered-left-right" style="border-left: 10px solid #d7d7d7; border-right: 10px solid #d7d7d7; max-width: 600px; width: 100%;">
                        <tr height="50"><td colspan="3" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td></tr>
                        <tr align="center">
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                            <td class="text-primary" style="color: #F16522; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;">
                                <img src="http://dgtlmrktng.s3.amazonaws.com/go/emails/generic-email-template/tick.png" alt="GO" width="50" style="border: 0; font-size: 0; margin: 0; max-width: 100%; padding: 0;">
                            </td>
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                        </tr>
                        <tr height="17"><td colspan="3" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td></tr>
                        <tr align="center">
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                            <td class="text-primary" style="color: #F16522; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;">
                                <h1 style="color: #F16522; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 30px; font-weight: 700; line-height: 34px; margin-bottom: 0; margin-top: 0;">Payment received</h1>
                            </td>
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                        </tr>
                        <tr height="30"><td colspan="3" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td></tr>
                        <tr align="left">
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                            <td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;">
                                <p style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; margin: 0;">
                                    Hi {}, 
                                </p>
                            </td>
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                        </tr>
                        <tr height="10"><td colspan="3" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td></tr>
                        <tr align="left">
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                            <td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;">
                                <p style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; margin: 0;">Your transaction was successful!</p>
                                <br>
                                <p style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; margin: 0; "><strong>Payment Details:</strong><br/>

Amount: ${} <br/>
Order ID: {}. [If You Choose Monthly Payment, This Is The Subscription ID] <br/></p> 
You can now login to your secure dashboard,
we advise you not to share the credentials to anyone.
Please check another email from our department. for your dashboard, username,password
Your Login URL: https://www.secureclientaccess.com/login <br/>
                                    <br>
                                <p style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; margin: 0;">We advise to keep this email for future reference.&nbsp;&nbsp;&nbsp;&nbsp;<br/></p>
                            </td>
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                        </tr>
                        <tr height="30">
                            <td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                            <td style="border-bottom: 1px solid #D3D1D1; color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                            <td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                        </tr>
                        <tr height="30"><td colspan="3" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td></tr>
                        <tr align="center">
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                            <td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;">
                                <p style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; margin: 0;"><strong>Transaction reference: {}</strong></p>
                                <p style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; margin: 0;">Order date: {}</p>
                                <p style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; margin: 0;"></p>
                            </td>
                            <td width="36" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                        </tr>

                        <tr height="50">
                            <td colspan="3" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                        </tr>

                    </table>
                    <!-- Generic Pod Left Aligned with Price breakdown End -->

                    <!-- Seperator Start -->
                    <table cellpadding="0" cellspacing="0" cols="1" bgcolor="#d7d7d7" align="center" style="max-width: 600px; width: 100%;">
                        <tr bgcolor="#d7d7d7">
                            <td height="50" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td>
                        </tr>
                    </table>
                    <!-- Seperator End -->

                </td>
            </tr>
        </table>
        <!-- Content End -->

        <!-- Footer Start -->
        <div class="bg-gray-dark footer" bgcolor="#464646" height="165" style="background-color: #464646; width: 100%;">
            <table align="center" bgcolor="#464646" style="max-width: 600px; width: 100%;">
                
                <tr height="15"><td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td></tr>

                <tr>
                    <td align="center" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;">
                        <img src="https://te.legra.ph/file/73e88627291b407a14f8c.jpg" alt="Ameco Capital" width="50" style="border: 0; font-size: 0; margin: 0; max-width: 100%; padding: 0;">
                    </td>
                </tr>
                
                <tr height="2"><td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td></tr>

                <tr>
                    <td align="center" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;">
                        <p class="text-white" style="color: white; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; margin: 0;">Copyright © AMECO CAPITAL INC 2022. All rights reserved.</p>
                        <p class="text-primary" style="color: #F16522; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 22px; margin: 0;">
                        </p>
                    </td>
                </tr>
                
                <tr height="15"><td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td></tr>

                <tr>
                    <td align="center" style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;">
                        <a href="#!" style="-webkit-text-decoration-color: #464646; color: #F16522; text-decoration: none; text-decoration-color: #464646;"><img width="25" htight="25" src="http://dgtlmrktng.s3.amazonaws.com/go/emails/generic-email-template/fb.png" target="_blank" alt="Facebook" style="border: 0; font-size: 0; margin: 0; max-width: 100%; padding: 0;"></a>&nbsp;
                        <a href="#!" style="-webkit-text-decoration-color: #464646; color: #F16522; text-decoration: none; text-decoration-color: #464646;"><img width="25" htight="25" src="http://dgtlmrktng.s3.amazonaws.com/go/emails/generic-email-template/youtube.png" target="_blank" alt="Youtube" style="border: 0; font-size: 0; margin: 0; max-width: 100%; padding: 0;"></a>&nbsp;
                        <a href="#!" style="-webkit-text-decoration-color: #464646; color: #F16522; text-decoration: none; text-decoration-color: #464646;"><img width="25" htight="25" src="http://dgtlmrktng.s3.amazonaws.com/go/emails/generic-email-template/linkedin.png" target="_blank" alt="LinkedIn" style="border: 0; font-size: 0; margin: 0; max-width: 100%; padding: 0;"></a>&nbsp;
                    </td>
                </tr>
                <tr height="10"><td style="color: #464646; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; font-size: 14px; line-height: 16px; vertical-align: top;"></td></tr>

            </table>
        </div>
        <!-- Footer End -->
    </body>
</html>
"""

aprved_emai = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<!doctype html>
<html lang="en-US">

<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <title>Wohoo !! Order Is approved.</title>
    <meta name="description" content="Reset Password Email Template.">
</head>

<body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">
    <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8"
        style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
        <tr>
            <td>
                <table style="background-color: #f2f3f8; max-width:670px;  margin:0 auto;" width="100%" border="0"
                    align="center" cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="height:80px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td style="text-align:center;">
                          <a href="https://amecocapital.com" title="logo" target="_blank">
                            <img width="60" src="https://te.legra.ph/file/73e88627291b407a14f8c.jpg" title="logo" alt="logo">
                          </a>
                        </td>
                    </tr>
                    <tr>
                        <td style="height:20px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td>
                            <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0"
                                style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                <tr>
                                    <td style="height:40px;">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td style="padding:0 35px;">
                                        <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">Hey {}, You're Credit Repair Order For {}, Is Approved.</h1>
                                        <span
                                            style="display:inline-block; vertical-align:middle; margin:29px 0 26px; border-bottom:1px solid #cecece; width:100px;"></span>
                                        <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">
                                            We cannot simply send you your requested service via email. A unique link to view your data has been generated for you. please click the following link and follow the instructions.
                                        </p>
                                        <a href="https://amecocapital.com/dashbaord/2/status"
                                            style="background:#20e277;text-decoration:none !important; font-weight:500; margin-top:35px; color:#fff;text-transform:uppercase; font-size:14px;padding:10px 24px;display:inline-block;border-radius:50px;">My Dashboard
                                       </a>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="height:40px;">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    <tr>
                        <td style="height:20px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td style="text-align:center;">
                            <p style="font-size:14px; color:rgba(69, 80, 86, 0.7411764705882353); line-height:18px; margin:0 0 0;">&copy; <strong>www.amecocapital.com</strong></p>
                        </td>
                    </tr>
                    <tr>
                        <td style="height:80px;">&nbsp;</td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>

</html>
"""

rejct_emai = """
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">
<!doctype html>
<html lang="en-US">
<head>
    <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
    <title>Wohoo !! Order Is approved.</title>
    <meta name="description" content="Reset Password Email Template.">
</head>

<body marginheight="0" topmargin="0" marginwidth="0" style="margin: 0px; background-color: #f2f3f8;" leftmargin="0">
    <table cellspacing="0" border="0" cellpadding="0" width="100%" bgcolor="#f2f3f8"
        style="@import url(https://fonts.googleapis.com/css?family=Rubik:300,400,500,700|Open+Sans:300,400,600,700); font-family: 'Open Sans', sans-serif;">
        <tr>
            <td>
                <table style="background-color: #f2f3f8; max-width:670px;  margin:0 auto;" width="100%" border="0"
                    align="center" cellpadding="0" cellspacing="0">
                    <tr>
                        <td style="height:80px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td style="text-align:center;">
                          <a href="https://amecocapital.com" title="logo" target="_blank">
                            <img width="60" src="https://te.legra.ph/file/73e88627291b407a14f8c.jpg" title="logo" alt="logo">
                          </a>
                        </td>
                    </tr>
                    <tr>
                        <td style="height:20px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td>
                            <table width="95%" border="0" align="center" cellpadding="0" cellspacing="0"
                                style="max-width:670px;background:#fff; border-radius:3px; text-align:center;-webkit-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);-moz-box-shadow:0 6px 18px 0 rgba(0,0,0,.06);box-shadow:0 6px 18px 0 rgba(0,0,0,.06);">
                                <tr>
                                    <td style="height:40px;">&nbsp;</td>
                                </tr>
                                <tr>
                                    <td style="padding:0 35px;">
                                        <h1 style="color:#1e1e2d; font-weight:500; margin:0;font-size:32px;font-family:'Rubik',sans-serif;">Hey {}, You're Order For {}, Is Not Approved.</h1>
                                        <span
                                            style="display:inline-block; vertical-align:middle; margin:29px 0 26px; border-bottom:1px solid #cecece; width:100px;"></span>
                                        <p style="color:#455056; font-size:15px;line-height:24px; margin:0;">
                                            You're Order Has Been Cancelled, Refunds Will be issued in 2-3 Bussiness Days.. {}.
                                        </p>
                                        <a href="https://amecocapital.com/dashbaord/2/status"
                                            style="background:#20e277;text-decoration:none !important; font-weight:500; margin-top:35px; color:#fff;text-transform:uppercase; font-size:14px;padding:10px 24px;display:inline-block;border-radius:50px;">My Dashboard
                                       </a>
                                    </td>
                                </tr>
                                <tr>
                                    <td style="height:40px;">&nbsp;</td>
                                </tr>
                            </table>
                        </td>
                    <tr>
                        <td style="height:20px;">&nbsp;</td>
                    </tr>
                    <tr>
                        <td style="text-align:center;">
                            <p style="font-size:14px; color:rgba(69, 80, 86, 0.7411764705882353); line-height:18px; margin:0 0 0;">&copy; <strong>www.amecocapital.com</strong></p>
                        </td>
                    </tr>
                    <tr>
                        <td style="height:80px;">&nbsp;</td>
                    </tr>
                </table>
            </td>
        </tr>
    </table>
</body>

</html>
"""
