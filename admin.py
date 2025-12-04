from flask import*
from database import*

admin=Blueprint('admin',__name__)

@admin.route('/admin_home')
def admin_home():
    return render_template('admin_home.html')

@admin.route('/admin_manage_place',methods=['GET','POST'])
def admin_manage_place():
    data={}
    if 'add_place' in request.form:
        place=request.form['place']
        details=request.form['details']
        i="insert into place values(null,'%s','%s')"%(place,details)
        insert(i)
        return redirect(url_for('admin.admin_manage_place'))
    if 'action' in request.args:
        place_id=request.args['place_id']
        action=request.args['action']
    else: action=None
    if action=='delete':
        d="delete from place where place_id='%s'"%(place_id)
        delete(d)
        return redirect(url_for('admin.admin_manage_place'))
    if action=='update':
        q="select * from place where place_id='%s'"%(place_id)
        data['upd']=select(q)
    if 'up' in request.form:
        place=request.form['place']
        details=request.form['details']
        j="update place set place='%s',details='%s' where place_id='%s'"%(place,details,place_id)
        update(j)
        return redirect(url_for('admin.admin_manage_place'))
    s="select * from place"
    data['resource']=select(s)
    return render_template('admin_manage_place.html',data=data)


@admin.route('/admin_view_volunteer')
def admin_view_volunteer():
    data={}
    s="select * from volunteer"
    data['volunteer']=select(s)
    return render_template('admin_view_volunteer.html',data=data)


@admin.route('/admin_view_counselors')
def admin_view_counselors():
    data={}
    s="select * from counselors"
    data['counselors']=select(s)
    return render_template('admin_view_counselors.html',data=data)




@admin.route('/admin_manage_emergency',methods=['GET','POST'])
def admin_manage_emergency():
    data={}
    if 'add_emergency' in request.form:
        name=request.form['name']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        s="select * from login where username='%s'"%(username)
        check=select(s)
        if check:
            flash('Username already exist')
        else:
            a="insert into login values(null,'%s','%s','emergency')"%(username,password)
            login_id=insert(a)
            i="insert into emergency values(null,'%s','%s','%s','%s')"%(login_id,name,phone,email)
            insert(i)
            return redirect(url_for('admin.admin_manage_emergency'))
        
    if 'action' in request.args:
        emergency_id=request.args['emergency_id']
        action=request.args['action']
        log_id=request.args['lid']

    else: action=None
    if action=='delete':
        d="delete from emergency where emergency_id='%s'"%(emergency_id)
        delete(d)
        f="delete from login where login_id='%s'"%(log_id)
        delete(f)
        return redirect(url_for('admin.admin_manage_emergency'))
    if action=='update':
        q="select * from emergency where emergency_id='%s'"%(emergency_id)
        data['upd']=select(q)
    if 'up' in request.form:
        name=request.form['name']
        phone=request.form['phone']
        email=request.form['email']
        j="update emergency set emergency_name='%s',phone='%s',email='%s' where emergency_id='%s'"%(name,phone,email,emergency_id)
        update(j)
        return redirect(url_for('admin.admin_manage_emergency'))
    s="select * from emergency"
    data['resource']=select(s)
    return render_template('admin_manage_emergency.html',data=data)




@admin.route('/admin_view_user')
def admin_view_user():
    data={}
    s="select * from user"
    data['user']=select(s)
    return render_template('admin_view_user.html',data=data)







@admin.route('/admin_view_disaster')
def admin_view_disaster():
    data={}
    s="select * from disasters"
    data['disaster']=select(s)
    return render_template('admin_view_disaster.html',data=data)


@admin.route('/home')
def home():
    return render_template('home.html')


@admin.route('/admin_view_issues')
def admin_view_issues():
    data={}
    s="select * from issues inner join place using(place_id)"
    data['issues']=select(s)
    return render_template('admin_view_issues.html',data=data)



@admin.route('/admin_view_complaint')
def admin_view_complaint():
    data={}
    s="select * from complaint inner join user using(user_id) where complaint.reply='pending'"
    data['complaint']=select(s)
    return render_template('admin_view_complaint.html',data=data)



@admin.route('/admin_send_reply',methods=['GET','POST'])
def admin_send_reply():
    data={}
    complaint_id=request.args['complaint_id']    
    s="select * from complaint inner join user using(user_id) where complaint_id='%s'"%(complaint_id)
    data['complaint']=select(s)
    if 'submit' in request.form:
        replyMessage=request.form['replyMessage']
        i="update complaint set reply='%s' where complaint_id='%s'"%(replyMessage,complaint_id)
        update(i)
        flash('reply sented successfully')
        return redirect(url_for('admin.admin_view_complaint'))
    return render_template('admin_send_reply.html',data=data)



@admin.route('/admin_manage_shop',methods=['GET','POST'])
def admin_manage_shop():
    data={}
    if 'submit' in request.form:
        shop=request.form['shop']
        place=request.form['place']
        email=request.form['email']
        phone=request.form['phone']
        latitude=request.form['latitude']
        longitude=request.form['longitude']
        username=request.form['username']
        password=request.form['password']
        a="insert into login values(null,'%s','%s','shop')"%(username,password)
        login_id=insert(a)
        b="insert into shop values(null,'%s','%s','%s','%s','%s','%s','%s')"%(login_id,shop,place,phone,email,latitude,longitude)
        insert(b)
          
    if 'action' in request.args:
        shop_id=request.args['shop_id']
        action=request.args['action']
    else: action=None
    if action=='delete':
        d="delete from shop where shop_id='%s'"%(shop_id)
        delete(d)
        return redirect(url_for('admin.admin_manage_shop'))
    if action=='update':
        q="select * from shop where shop_id='%s'"%(shop_id)
        data['upd1']=select(q)
    if 'up' in request.form:
        shop=request.form['shop']
        place=request.form['place']
        email=request.form['email']
        phone=request.form['phone']
        latitude=request.form['latitude']
        longitude=request.form['longitude']
        j="update shop set shop='%s',place='%s',phone='%s',email='%s',latitude='%s',longitude='%s' where shop_id='%s'"%(shop,place,phone,email,latitude,longitude,shop_id)
        update(j)
        return redirect(url_for('admin.admin_manage_shop'))
        
    s="select * from shop" 
    data['resource']=select(s)
    return render_template('admin_manage_shop.html',data=data)

@admin.route('/admin_view_booking',methods=['GET','POST'])
def admin_view_booking():
    data={}
    s="select * from ordermaster inner join user using(user_id) inner join login using(login_id)"
    data['booking']=select(s)
    if 'action' in request.args:
        action=request.args['action']
        order_id=request.args['order_id']
    else: action=None
    if action=='details':
        s="select * from items inner join orderdetail using(item_id) where order_id='%s'"%(order_id)
        data['detls']=select(s)
    return render_template('admin_view_booking.html',data=data)

@admin.route('/admin_view_feedback',methods=['GET','POST'])
def admin_view_feedback():
    data={}
    s="select * from feedback inner join user using(user_id)"
    data['feedback']=select(s)
    return render_template('admin_view_feedback.html',data=data)

@admin.route('/index')
def index():
    return render_template('index.html')


@admin.route('/admin_chatmain',methods=['GET','POST'])
def admin_chatmain():
    data={}
    s="select * from user inner join chat on user.login_id=chat.sender_id group by chat.sender_id"
    data['message']=select(s)
    return render_template('admin_chatmain.html',data=data)


@admin.route('/admin_chat',methods=['POST','GET'])
def admin_chat(): 
    data={}
    login_id=request.args['login_id']

    if 'submit' in request.form:
        msg=request.form['reply']
        login_id=request.args['login_id']
        i=" insert into chat values(null,'1','%s',curdate(),'%s')"%(login_id,msg)
        insert(i)
    y="select * from chat where sender_id='1' and reciver_id='%s' or reciver_id='1' and sender_id='%s'"%(login_id,login_id)
    data['msg']=select(y)
    return render_template('admin_chat.html',data=data)

