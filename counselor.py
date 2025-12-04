from flask import*
from database import*
counselor=Blueprint('counselor',__name__)

@counselor.route('/counselor_home')
def counselor_home():
    
    return render_template('counselor_home.html')


@counselor.route('/home')
def home():
    return render_template('home.html')


@counselor.route('/counselor_manage_volunteer_head',methods=['GET','POST'])
def counselor_manage_volunteer_head():
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
            a="insert into login values(null,'%s','%s','volunteer_head')"%(username,password)
            login_id=insert(a)
            i="insert into volunteer_head values(null,'%s','%s','%s','%s','%s','%s','%s')"%(login_id,place_id,fname,lname,place,phone,email)
            insert(i)
            return redirect(url_for('counselor.counselor_manage_volunteer_head'))
        
    if 'action' in request.args:
        vhead_id=request.args['vhead_id']
        action=request.args['action']
        log_id=request.args['lid']
    else: action=None
    if action=='delete':
        d="delete from volunteer_head where vhead_id='%s'"%(vhead_id)
        delete(d)
        awd="delete from login where login_id='%s'"%(log_id)
        delete(awd)
        return redirect(url_for('counselor.counselor_manage_volunteer_head'))
    if action=='update':
        q="select * from volunteer_head where vhead_id='%s'"%(vhead_id)
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
        j="update volunteer_head set place_id='%s', fname='%s',lname='%s', place='%s',phone='%s',email='%s' where vhead_id='%s'"%(place_id,fname,lname,place,phone,email,vhead_id)
        update(j)
        return redirect(url_for('counselor.counselor_manage_volunteer_head'))
    s="select * from volunteer_head"
    data['resource']=select(s)
    return render_template('counselor_manage_volunteer_head.html',data=data)





@counselor.route('/counselor_view_issues')
def counselor_view_issues():
    data={}
    s="select * from issues inner join place using(place_id) where status ='need help'"
    data['issues']=select(s)
    return render_template('counselor_view_issues.html',data=data)



@counselor.route('/counselor_add_help',methods=['GET','POST'])
def counselor_add_help():
    data={}
    issues_id=request.args['issue_id']
    s="select * from issues inner join place using(place_id) where issue_id='%s'"%(issues_id)
    data['issue']=select(s)
    if 'submit' in request.form:
        helpfulness=request.form['helpfulness']
        i="insert into helpfulness values(null,'%s','%s') "%(issues_id,helpfulness)
        insert(i)
        u="update issues set status='help added' where issue_id='%s'"%(issues_id)
        update(u)
        flash('help added successfully')
        return redirect(url_for('counselor.counselor_view_issues'))
    return render_template('counselor_add_help.html',data=data)

