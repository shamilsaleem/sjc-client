from flask import Flask, request, make_response, render_template 
import requests
from bs4 import BeautifulSoup

app = Flask(__name__) 
  
@app.route('/', methods = ['GET']) 
def home():
  resp = render_template('loading.html')
  return resp
 
@app.route('/home', methods = ['GET']) 
def home1():
    if(request.cookies.get('username') and request.cookies.get('password')):
        web_data = get_attendance(request.cookies.get('username'), request.cookies.get('password'))
        return web_data
    else:
        return render_template('home.html', message = '') 
  
@app.route('/', methods = ['POST']) 
def login(): 
    if request.method == 'POST': 
        username = request.form['username'] 
        password = request.form['password']
        auth_data = requests.post('https://devagiricollege.net/sjc/Home/student', {'username':username, 'password':password})
        if(auth_data.url=='https://devagiricollege.net/sjc/student/student/dashboard'):
            resp = app.redirect('/')
            resp.set_cookie('username', username, max_age=31536000)
            resp.set_cookie('password', password, max_age=31536000)
        else:
            resp = render_template('home.html',message = 'invalid username or password.')
    return resp

@app.route('/logout', methods = ['GET']) 
def logout():
    resp = app.redirect('/')
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp

def get_attendance(username, password):
    session = requests.Session()
    session.post('https://devagiricollege.net/sjc/Home/student', {'username':username, 'password':password})
    #getting student data

    page1 = session.get('https://devagiricollege.net/sjc/student/student/dashboard')
    soup1 = BeautifulSoup(page1.text, "html.parser")
    student_data = soup1.find_all("div", class_="box-body box-profile")

    #getting attendance_daywise

    page2 = session.get('https://devagiricollege.net/sjc/student/student/attendance_daywise')
    soup2 = BeautifulSoup(page2.text, "html.parser")
    student_attendance_daywise = soup2.find_all("div", class_="box-body")

    #getting abscence_details

    page3 = session.get('https://devagiricollege.net/sjc/student/student/abscence_details')
    soup3 = BeautifulSoup(page3.text, "html.parser")
    student_abscence_details = soup3.find_all("div", class_="box box-primary")

    return head_tag + '\n' + str(student_data[0]) + '\n' +str(student_attendance_daywise[0]) + '\n' + str(student_abscence_details[0]) + '\n' + '''
    <div class="text-center">
    <a href="/logout">
    <button type="button" class="btn btn-danger" style="margine-bottom:3px;">Logout</button>
    </a>
    <br>
    <p class="login-box-msg" style="margin-bottom: 0px; margin-top: 5px;">Your login credentials are
                        stored within your browser.</p>
                      <p class="login-box-msg" style="margin-bottom: 0px; margin-top: 0px;"><a
                          href="https://devagiricollege.net/sjc/Home/student">Official Site</a> • <a
                          href="https://github.com/shamilsaleem/sjc-client">Source Code</a></p>
                      <p class="login-box-msg" style="margin-bottom: 0px; margin-top: 0px;">Made with ❤️ by <a
                          href="https://www.instagram.com/shamil.saleem">🫠</a></p>
                    
    </div>
    <body>'''


head_tag ="""
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <title>ST. JOSEPH'S COLLEGE (AUTONOMOUS), DEVAGIRI, CALICUT</title>

  <meta content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" name="viewport">
  <link rel="shortcut icon" href="https://devagiricollege.net/sjc/asset/admin/img/logo.png">
  
  
  
  <link rel="manifest" href="/static/manifest.json" />
  <!-- ios support -->
  <link rel="apple-touch-icon" sizes="57x57"
    href="https://devagiricollege.net/sjc/asset/admin/img/favicon/apple-icon-57x57.png">
  <link rel="apple-touch-icon" sizes="60x60"
    href="https://devagiricollege.net/sjc/asset/admin/img/favicon/apple-icon-60x60.png">
  <link rel="apple-touch-icon" sizes="72x72"
    href="https://devagiricollege.net/sjc/asset/admin/img/favicon/apple-icon-72x72.png">
  <link rel="apple-touch-icon" sizes="76x76"
    href="https://devagiricollege.net/sjc/asset/admin/img/favicon/apple-icon-76x76.png">
  <link rel="apple-touch-icon" sizes="114x114"
    href="https://devagiricollege.net/sjc/asset/admin/img/favicon/apple-icon-114x114.png">
  <link rel="apple-touch-icon" sizes="120x120"
    href="https://devagiricollege.net/sjc/asset/admin/img/favicon/apple-icon-120x120.png">
  <link rel="apple-touch-icon" sizes="144x144"
    href="https://devagiricollege.net/sjc/asset/admin/img/favicon/apple-icon-144x144.png">
  <link rel="apple-touch-icon" sizes="152x152"
    href="https://devagiricollege.net/sjc/asset/admin/img/favicon/apple-icon-152x152.png">
  <link rel="apple-touch-icon" sizes="180x180"
    href="https://devagiricollege.net/sjc/asset/admin/img/favicon/apple-icon-180x180.png">
  <link rel="icon" sizes="192x192" href="/static/android-chrome-192x192.png">
  <link rel="icon" sizes="512x512" href="/static/android-chrome-512x512.png">

  <meta name="apple-mobile-web-app-status-bar" content="#db4938" />
  <meta name="theme-color" content="#db4938" />
  
  <script src="/static/app.js"></script>
  


  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/imag_privew/neon-forms.css">

  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/bootstrap.min.css">

  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/language/l_one.css">

  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/data_table/dataTables.bootstrap.css">

  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/datepicker/datepicker3.css"> <!-- need -->
  <!-- bootstrap datepicker -->

  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/fullcalendar/fullcalendar.min.css">

  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/fullcalendar/fullcalendar.print.css" media="print">

  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/select2/select2.min.css">

  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/dist/AdminLTE.min.css">

  <link rel="stylesheet" href="https://devagiricollege.net/sjc/asset/admin/css/tholi/_all-skins.min.css">
  <script src="https://devagiricollege.net/sjc/asset/admin/js/jQuery/jquery-2.2.3.min.js"></script>
</head>

<body style="height: auto;">
<style>
    .cls {
        background-color: #e5ec75;
        margin-left: 10px;
        font-weight: bold;
    }

    .clstwo {
        color: green;

    }
    td{
        border: 1px solid black;
    }
    #absenceSubs th ,#absenceSubs td{
        border: 1px solid black;
        font-size: 16px;
    }
    #lastRow td{
        border: none;
    }
    .text-md{
        font-size: medium;
    }
    a.btn.btn-primary.btn-block {
    display: none;
    }
    label.form-control-label {
    display: none;
    }
    button.btn.btn-default {
    display: none;
    }
</style>
"""
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=8080)