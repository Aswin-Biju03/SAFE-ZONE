from flask import*
from database import*
volunteer_head=Blueprint('volunteer_head',__name__)


@volunteer_head.route('/volunteer_head_home')
def volunteer_head_home():
    
    return render_template('volunteer_head_home.html')


@volunteer_head.route('/volunteer_head_update_profile',methods=['GET','POST'])
def volunteer_head_update_profile():
    data={}
    s="select * from volunteer_head inner join login using (login_id) where vhead_id='%s'"%(session['vhead_id'])
    data['upd']=select(s)
    if 'add' in request.form:
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        email=request.form['email']
        i="update volunteer_head set fname='%s',lname='%s',phone='%s',email='%s' where vhead_id='%s'"%(fname,lname,phone,email,session['vhead_id'])
        update(i)
        flash("Your profile has been updated")
        return redirect(url_for('volunteer_head.volunteer_head_home'))
            
    return render_template('volunteer_head_update_profile.html',data=data)


@volunteer_head.route('/volunteer_head_manage_volunteer',methods=['GET','POST'])
def volunteer_head_manage_volunteer():
    data={}
    y="select * from place"
    data['place']=select(y)
    if 'add' in request.form:
        place_id=request.form['place_id']
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        email=request.form['email']
        username=request.form['username']
        password=request.form['password']
        s="select place from place where place_id='%s'"%(place_id)
        p=select(s)
        place=p[0]['place']
        s="select * from login where username='%s'"%(username)
        check=select(s)
        if check:
            flash('Username already exist')
        else:
            a="insert into login values(null,'%s','%s','volunteer')"%(username,password)
            login_id=insert(a)
            i="insert into volunteer values(null,'%s','%s','%s','%s','%s','%s','%s')"%(login_id,place_id,fname,lname,place,phone,email)
            insert(i)
            flash("Volunteer Added")
            return redirect(url_for('volunteer_head.volunteer_head_manage_volunteer'))

    if 'action' in request.args:
        volunteer_id=request.args['volunteer_id']
        action=request.args['action']
        log_id=request.args['lid']
    else: action=None
    if action=='delete':
        d="delete from volunteer where volunteer_id='%s'"%(volunteer_id)
        delete(d)
        ui="delete from login where login_id='%s'"%(log_id)
        delete(ui)
        return redirect(url_for('volunteer_head.volunteer_head_manage_volunteer'))
    if action=='update':
        q="select * from volunteer where volunteer_id='%s'"%(volunteer_id)
        data['upd']=select(q)
    if 'up' in request.form:
        place_id=request.form['place_id']
        fname=request.form['fname']
        lname=request.form['lname']
        phone=request.form['phone']
        email=request.form['email']
        s="select place from place where place_id='%s'"%(place_id)
        p=select(s)
        place=p[0]['place']
        j="update volunteer set place_id='%s', fname='%s',lname='%s', place='%s',phone='%s',email='%s' where volunteer_id='%s'"%(place_id,fname,lname,place,phone,email,volunteer_id)
        update(j)
        return redirect(url_for('volunteer_head.volunteer_head_manage_volunteer'))
    s="select * from volunteer"
    data['resource']=select(s)
    return render_template('volunteer_head_manage_volunteer.html',data=data)


@volunteer_head.route('/volunteer_head_view_issues')
def volunteer_head_view_issues():
    data={}
    s="select * from issues inner join place using(place_id) "
    data['issues']=select(s)
    if 'action' in request.args:
        issue_id=request.args['issue_id']
        action=request.args['action']
    else: action=None
    if action=='update':
        d="update issues set status='need help' where issue_id='%s'"%(issue_id)
        update(d)
        return redirect(url_for('volunteer_head.volunteer_head_view_issues'))
    return render_template('volunteer_head_view_issues.html',data=data)


# @volunteer_head.route('/volunteer_head_view_help',methods=['GET','POST'])
# def volunteer_head_view_help():
#     data={}
#     issues_id=request.args['issue_id']
#     s="select * from helpfulness inner join issues using(issue_id) inner join place using(place_id)  where issue_id='%s' "%(issues_id)
#     if s:
#         data['issue']=select(s)
#     else:
#         s="select * from issues inner join place using(place_id)  where issue_id='%s' "%(issues_id)
#         data['issue']=select(s)
#     return render_template('volunteer_head_view_help.html',data=data)

@volunteer_head.route('/volunteer_head_view_help', methods=['GET', 'POST'])
def volunteer_head_view_help():
    data = {}
    issues_id = request.args.get('issue_id')
    
    # First query
    query1 = """
        SELECT * 
        FROM helpfulness 
        INNER JOIN issues USING(issue_id) 
        INNER JOIN place USING(place_id)  
        WHERE issue_id = %s
    """ % (issues_id)
    
    result = select(query1)  # Assuming `select` is a function that executes the query and returns a result

    if result:  # If the result is not empty
        data['issue'] = result
    else:
        # Fallback query
        query2 = """
            SELECT * 
            FROM issues 
            INNER JOIN place USING(place_id)  
            WHERE issue_id = %s
        """ % (issues_id)
        data['issue'] = select(query2)
    
    return render_template('volunteer_head_view_help.html', data=data)



@volunteer_head.route('/volunteer_head_view_camp')
def volunteer_head_view_camp():
    data={}
    place_id=request.args['place_id']
    s="select * from camps inner join place using(place_id) where place_id='%s'"%(place_id)
    data['issues']=select(s)
    return render_template('volunteer_head_view_camp.html',data=data)


@volunteer_head.route('/home')
def home():
    return render_template('home.html')


@volunteer_head.route('/volunteer_head_view_accomodation')
def volunteer_head_view_accomodation():
    data={}
    camp_id=request.args['camp_id']
    s="select * from accomodation  where camps_id='%s'"%(camp_id)
    data['issues']=select(s)
    return render_template('volunteer_head_view_accomodation.html',data=data)




@volunteer_head.route('/volunteer_head_chatmain',methods=['GET','POST'])
def volunteer_head_chatmain():
    data={}
    s="select * from volunteer_head where login_id !='%s'"%(session['login_id'])
    data['message']=select(s)
    return render_template('volunteer_head_chatmain.html',data=data)



@volunteer_head.route('/volunteer_head_chat',methods=['POST','GET'])
def volunteer_head_chat(): 
    data={}
    login_id=request.args['login_id']

    if 'submit' in request.form:
        msg=request.form['reply']
        login_id=request.args['login_id']
        i=" insert into chat values(null,'%s','%s','%s',curdate())"%(session['login_id'],login_id,msg)
        insert(i)
    y="select * from chat where sender_id='%s' and reciver_id='%s' or reciver_id='%s' and sender_id='%s'"%(session['login_id'],login_id,session['login_id'],login_id)
    data['msg']=select(y)
    print(y)
    print(data['msg'])
    return render_template('volunteer_head_chat.html',data=data)




@volunteer_head.route('/volunteer_head_predict',methods=['GET','POST'])
def volunteer_head_predict():
    
    return render_template('volunteer_head_predict.html')