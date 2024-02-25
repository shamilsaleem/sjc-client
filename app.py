from flask import Flask, request, make_response, render_template 
import requests
from bs4 import BeautifulSoup

app = Flask(__name__) 
  
@app.route('/', methods = ['GET']) 
async def home(): 
   if(request.cookies.get('username') and request.cookies.get('password')):
       web_data = get_attendance(request.cookies.get('username'), request.cookies.get('password'))
       return web_data
   else:
       return render_template('home.html') 
  
@app.route('/', methods = ['POST']) 
def login(): 
    if request.method == 'POST': 
        username = request.form['username'] 
        password = request.form['password']
        resp = app.redirect('/')
        resp.set_cookie('username', username)
        resp.set_cookie('password', password)
    return resp

@app.route('/logout', methods = ['GET']) 
def logout():
    resp = app.redirect('/')
    resp.set_cookie('username', '', expires=0)
    resp.set_cookie('password', '', expires=0)
    return resp

def get_attendance(username, password):
    session = requests.Session()
    session.post('https://devagiricollege.net/sjc/Home/student', {'username':username, 'password':password}
                 )
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