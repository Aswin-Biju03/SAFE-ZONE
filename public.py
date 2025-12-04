from flask import *
from database import*
from flask_mail import Mail, Message
import random
import string
import smtplib
from email.mime.text import MIMEText
public=Blueprint('public',__name__)
@public.route('/')
def home():
    return render_template('home.html')

@public.route('/login',methods=['GET','POST'])
def login():
    if 'submit' in request.form:
        username=request.form['username']
        password=request.form['password']
        a="select * from login where username='%s' and password='%s'"%(username,password)
        a1=select(a)

        if a1:
            session['login_id']=a1[0]['login_id']
            if a1[0]['usertype']=='admin':
                # flash("Welcome admin")
                """<script>alert("Welcome Admin");window.location='/admin_home'</scrpit>"""
                return redirect(url_for('admin.admin_home'))
            if a1[0]['usertype']=='counselor':
                s="select * from counselors where login_id='%s'"%(session['login_id'])
                a2=select(s)
                if a2:
                    session['counselors_id']=a2[0]['counselors_id']
                return redirect(url_for('counselor.counselor_home'))
            if a1[0]['usertype']=='volunteer_head':
                d="select*from volunteer_head where login_id='%s'"%(session['login_id'])
                d2=select(d)
                if d2:
                    session['vhead_id']=d2[0]['vhead_id']
                return redirect(url_for('volunteer_head.volunteer_head_home'))
            if a1[0]['usertype']=='shop':
                return redirect(url_for('shop.shop_home'))
        else:
            flash("Invalid username or password.")
            return redirect(url_for('public.login'))
    return render_template('login.html')
def generate_otp():
    return ''.join(random.choices(string.digits, k=6))



@public.route('/counselor_register',methods=['GET','POST'])
def counselor_register():
    if 'counselor_register' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        place=request.form['place']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        s="select * from login where username='%s'"%(username)
        check=select(s)
        if check:
            flash('Username already exist')
        else:
            a="insert into login values(null,'%s','%s','counselor')"%(username,password)
            login_id=insert(a)
            b="insert into counselors values(null,'%s','%s','%s','%s','%s','%s')"%(login_id,fname,lname,place,phone,email)
            insert(b)
            flash('Registerd Sucessfully')
            return redirect(url_for('public.login'))
    return render_template('counselor_register.html')
