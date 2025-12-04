from flask import Flask, Blueprint, request
from database import *
import uuid
api = Blueprint('api', __name__)

@api.route('/loginn',methods=['GET', 'POST'])
def loginn():
    data={}
    username=request.args['username']
    password=request.args['password']
    u = """
            SELECT login.login_id, login.usertype, user.user_id 
            FROM login 
            LEFT JOIN user ON login.login_id = user.login_id 
            WHERE login.username = '%s' AND login.password = '%s'
        """ % (username, password)  
    res=select(u)
    print(res)
    print(u)
    if res:
        data['status']="success"
        data['data']=res
    else:
        data['status']="failed"
    return str(data)

@api.route('/registration',methods=['GET','POST'])
def registration():
    data={}
    
    fname=request.args['firstname']
    lname=request.args['lastname']
    place=request.args['place']
    phno=request.args['phonenumber']
    email=request.args['email']
    username=request.args['username']
    password=request.args['password']
    
    u="insert into login values(null,'%s','%s','user')"%(username,password)
    res1=insert(u)
    i="insert into user values (null,'%s','%s','%s','%s','%s','%s')"%(res1,fname,lname,place,phno,email)
    res=insert(i)
    if res:
        data['status']="success"
        data['data']=res
        print('success')
    else:
        data['status']="failed"
        print('fail')
    return str(data)

@api.route('/image',methods=['GET','POST'])
def image():
    data={}
    iss_id=request.form['iss_id']
    img=request.files['image']
    path="static/image/"+str(uuid.uuid4())+img.filename
    img.save(path)
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjj",img)
    q="insert into image values(null,'%s','%s')"%(iss_id,path)
    res=insert(q)
    
    if res:
        data['status'] = "success"
    else:
        data['status'] ="fail"
        
    data['method'] = "add_product"
    
    return str(data)


@api.route('/view_issue',methods=['GET', 'POST'])
def view_issue():
    data={}
    id=request.args['id']
    i="select * from image inner join issues using(issue_id) where issue_id='%s'"%(id)
    res=select(i)
    if res:
        data['status']="success"
        data['data']=res
        data['method']='view_image'
        print('success')
    else:
        data['status']="failed"
        print('fail')
    
    return str(data)




@api.route('/view_images',methods=['GET', 'POST'])
def view_images():
    data={}
    id=request.args['id']
    i="select * from image where issue_id='%s'"%(id)
    res=select(i)
    if res:
        data['status']="Added"
        data['data']=res
        data['method']='product'
        print('success')
    else:
        data['status']="failed"
        print('fail')
    
    return str(data)



@api.route('/delete_image', methods=['GET', 'POST'])
def delete_image():
    data = {}
    id=request.args['id']
    s = "delete from image where image_id='%s'"%(id)
    delete(s) 
    
    return str(data)


@api.route('/view_issues', methods=['GET', 'POST'])
def view_issues():
    data = {}
    q = "SELECT * FROM issues inner join place using(place_id)"
    res = select(q)
    if res:
        data['status'] = "success"
        data['data'] = res
        data['method'] = 'view_issues'
        print('Success: Issues retrieved')
    else:
        data['status'] = "failed"
        data['method'] = 'view_issues'
        data['data'] = []
        print('Failure: No issues found')

    return str(data)


@api.route('/urgent_needs',methods=['GET', 'POST'])
def urgent_needs():
    data={}
    type=request.args['type']
    needs=request.args['needs']
    details=request.args['details']
    i="insert into needs values(null,'1','%s','%s','%s')"%(type,needs,details)
    insert(i)
    
    return str(data)


@api.route('/get_urgent_needs', methods=['GET', 'POST'])
def get_urgent_needs():
    data = {}
    
    s = "select * from needs"
    res = select(s) 
    if res:
        data['status']="Added"
        data['data']=res
        data['method']='product'
        print('success')
    else:
        data['status']="failed"
        print('fail')
    return str(data)


@api.route('/remove_urgent_need', methods=['GET', 'POST'])
def remove_urgent_need():
    data = {}
    id=request.args['id']
    s = "delete from needs where needs_id='%s'"%(id)
    res = delete(s) 
    
    if res:
        data['status']="success"
        data['data']=res
        print('success')
    else:
        data['status']="failed"
        print('fail')
    return str(data)


@api.route('/place', methods=['GET', 'POST'])
def place():
    data = {}
    i="select place from place"
    res=select(i)
    if res:
        data['status'] = "success"
        data['data'] =res
        data['method']='place'
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['message'] = "No data found"
        print("No data found")
    return str(data)

def get_place_id(place):
    y = "SELECT place_id FROM place WHERE place='%s'" % (place)
    result = select(y)
    if result:
        return result[0]['place_id'] 
    else:
        return None

@api.route('/add_issues', methods=['GET', 'POST'])
def add_issues():
    data = {}
    place=request.args['place']
    place_id=get_place_id(place)
    issue=request.args['issue']
    o="insert into issues values(null,'%s','%s',curdate(),'pending')"%(place_id,issue)
    insert(o)
    return str(data)

@api.route('/camp_names', methods=['GET', 'POST'])
def camp_names():
    data = {}
    i="select camp_name from camps"
    res=select(i)
    if res:
        data['status'] = "datas"
        data['method'] = 'view_camps'
        data['data'] = res
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['message'] = "No data found"
        print("No data found")
    return str(data)


def get_cid(cname):
    y = "SELECT camps_id from camps WHERE camp_name='%s'" % (cname)
    result = select(y)
    if result:
        return result[0]['camps_id'] 
    else:
        return None


@api.route('/add_camp', methods=['GET', 'POST'])
def add_camp():
    data = {}
    cname=request.args['camp_name']
    cid=get_cid(cname)
    vacency=request.args['vacancies']
    i="select * from free_space where camps_id='%s'"%(cid)      
    res=select(i)
    if res:
        data['status'] = 'error'
        data['method'] = 'add_camp'
        data['message'] = 'Please select a different camp name, this camp is already occupied.' 
    else:
        o="insert into free_space values(null,'%s','%s')"%(cid,vacency)
        insert(o)
        data['status'] = 'success'
        data['method'] = 'add_camp'
        data['message'] = 'Camp added successfully.'
    return str(data)

@api.route('/update_free_space', methods=['GET', 'POST'])
def update_free_space():
    data = {}
    id=request.args['freespace_id']
    vacency=request.args['info']
    i="update free_space set freespace='%s' where freespace_id='%s'"%(vacency,id)
    insert(i)
    data['status'] = 'success'
    data['method'] = 'update_free_space'
    data['message'] = 'Free space updated successfully'
    return str(data)

@api.route('/free_space', methods=['GET'])
def free_space():
    data = {}
    query = """
        SELECT camps.camp_name, free_space.freespace
        FROM free_space
        JOIN camps ON free_space.camps_id = camps.camps_id
    """
    res = select(query)

    if res:
        data['status'] = "success"
        data['data'] = [{"camp": row["camp_name"], "freespace": row["freespace"]} for row in res]
    else:
        data['status'] = "error"
        data['message'] = "No free space data available"

    return str(data)

@api.route('/get_needs', methods=['GET'])
def get_needs():
    data = {}
    query = """
        SELECT needs.needs_id, needs.type, needs.needs, needs.details
        FROM needs
    """
    res = select(query)
    if res:
        data['status'] = "success"
        data['data'] = [{"needs_id": row["needs_id"], "type": row["type"], "needs": row["needs"], "details": row["details"]} for row in res]
    else:
        data['status'] = "error"
        data['message'] = "No needs found"

    return str(data)

@api.route('/submit_need', methods=['POST', 'GET'])
def submit_need():
    data={}
    need_id = request.args['needs_id']
    additional_info = request.args['additional_info']
    
    query = "INSERT INTO needs_arrangements (needsarrange_id,needs_id, arrangements, date) VALUES (null,'%s','%s', curdate())"%(need_id,additional_info)
    insert(query)
    q="update needs set details='arranged' where needs_id='%s'"%(need_id)
    insert(q)
    
    return str(data) 


@api.route('/camps', methods=['GET'])
def camps():
    data = {}
    u = "SELECT * FROM camps inner join place using(place_id)"
    res = select(u)
    print("Camps Data:", res) 
    if res:
        data['status'] = 'success'
        data['method'] = 'view_camps'
        data['data'] = res
    else:
        data['status'] = 'failed'
        data['method'] = 'view_camps'
        data['message'] = 'No camps found'

    return str(data)

@api.route('/manage_camp', methods=['GET'])
def manage_camp():
    data = {}
    cname=request.args['camp_name']
    place=request.args['place']
    place_id=get_place_id(place)
    details=request.args['place_details']
    e="insert into camps values (null,'%s','%s','%s')"%(place_id,cname,details)
    insert(e)
    data['status'] = "success"
    data['method'] = "camp added sucessfully"
    
    return str(data)



@api.route('/remove_camp', methods=['GET', 'POST'])
def remove_camp():
    data = {}
    id=request.args['id']
    
    s = "delete from camps where camps_id='%s'"%(id)
    res = delete(s) 
    if res:
        data['status']="success"
        data['data']=res
        print('success')
    else:
        data['status']="failed"
        data['method'] = "remove_camp"  # Add method key

        print('fail')
    return str(data)

@api.route('/issues', methods=['GET'])
def issues():
    data = {}
    u = "SELECT * FROM issues inner join place using(place_id)"
    res = select(u)
    print("issues Data:", res)
    if res:
        data['status'] = 'success'
        data['method'] = 'view_issues'
        data['data'] = res
    else:
        data['status'] = 'failed'
        data['method'] = 'view_issues'
        data['message'] = 'No camps found'

    return str(data)

@api.route('/get_place_names', methods=['GET'])
def get_place_names():
    data = {}
    u = "SELECT place FROM place "
    res = select(u)
    print("issues Data:", res)
    if res:
        data['status'] = 'success'
        data['method'] = 'get_place_names'
        data['data'] = [item['place'] for item in res]
    else:
        data['status'] = 'failed'
        data['method'] = 'get_place_names'
        data['message'] = 'No camps found'

    return str(data)

@api.route('/add_issue', methods=['GET','POST'])
def add_issue():
    data = {}
    place=request.args['place_name']
    place_id=get_place_id(place)
    issue=request.args['issue']
    i="insert into issues values(null,'%s','%s',curdate(),'pending')"%(place_id,issue)
    insert(i)
    return str(data)

@api.route('/update', methods=['GET','POST'])
def update():
    data = {}
    id=request.args['id']
    place=request.args['place_name']
    place_id=get_place_id(place)
    issue=request.args['issue']
    i="update issues set place_id='%s',issue='%s',date=curdate() where issue_id='%s'"%(place_id,issue,id)
    insert(i)
    return str(data)


@api.route('/remove_issue', methods=['GET', 'POST'])
def remove_issue():
    data = {}
    id=request.args['id']
    
    s = "delete from issues where issue_id='%s'"%(id)
    res = delete(s) 
    if res:
        data['status'] = "success"
    else:
        data['status'] = "failed"
    return str(data)

@api.route('/get_places', methods=['GET'])
def get_place():
    data = {}
    query = "SELECT place_id, place FROM place"
    res = select(query)
    
    if res:
        data['status'] = 'success'
        data['method'] = 'get_place_names'
        data['data'] = [{"place_id": item['place_id'], "place": item['place']} for item in res]
    else:
        data['status'] = 'failed'
        data['method'] = 'get_place_names'
        data['message'] = 'No places found'

    return str(data)


@api.route('/add_emergency_situation', methods=['GET'])
def add_emergency_situation():
    data = {}
    
    place=request.args['place_id']
    sit=request.args['situation']
    status=request.args['status']
    query = "insert into emergency_situations values(null,'%s','%s',curdate(),'%s','pending')"%(place,sit,status)
    insert(query) 
    
    return str(data)

@api.route('/get_emergency_situations', methods=['GET'])
def get_emergency_situations():
    data = {}
    query = "SELECT * FROM emergency_situations inner join place using(place_id)"
    res = select(query)  
    
    if res:
        data['status'] = 'success'
        data['method'] = 'get_emergency_situations'
        data['data'] = res
    else:
        data['status'] = 'failed'
        data['method'] = 'get_emergency_situations'
        data['message'] = 'No places found'
    
    return str(data)


@api.route('/view_volunteers', methods=['GET'])
def view_volunteers():
    data = {}
    query = "SELECT * FROM volunteer inner join place using(place_id)"
    res = select(query)  
    
    if res:
        data['status'] = 'success'
        data['method'] = 'view_volunteers'
        data['data'] = res
    else:
        data['status'] = 'failed'
        data['method'] = 'view_volunteers'
        data['message'] = 'No places found'
    
    return str(data)

@api.route('/view_user_camp', methods=['GET'])
def view_user_camp():
    data = {}
    query = "SELECT * FROM camps inner join place using(place_id)"
    res = select(query)  
    
    if res:
        data['status'] = 'success'
        data['method'] = 'view_camps'
        data['data'] = res
    else:
        data['status'] = 'failed'
        data['method'] = 'view_camps'
        data['message'] = 'No places found'
    
    return str(data)



@api.route('/place_details', methods=['GET'])
def place_details():
    data = {}
    
    try:
        place = request.args['place']
        query = "SELECT * FROM place WHERE place = '%s'" % (place)
        res = select(query)
        
        if res:
            data['status'] = 'success'
            data['method'] = 'place_details'
            data['data'] = res
            print(res)
        else:
            data['status'] = 'failed'
            data['method'] = 'place_details'
            data['message'] = 'No places found'
    except KeyError:
        data['status'] = 'failed'
        data['method'] = 'place_details'
        data['message'] = 'Place parameter is missing'
    except Exception as e:
        data['status'] = 'error'
        data['method'] = 'place_details'
        data['message'] = str(e)
    
    return str(data) 


@api.route('/camp_namess', methods=['GET', 'POST'])
def camp_namess():
    data = {}
    i="select camp_name from camps"
    res=select(i)
    if res:
        data['status'] = "datas"
        data['method'] = 'camp_names'
        data['data'] = res
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['message'] = "No data found"
        print("No data found")
    return str(data)

@api.route('/accomodation',methods=['GET','POST'])
def accomodation():
    data={}
    name=request.form['name']
    cname=request.form['cname']
    cid=get_cid(cname)
    phnoo=request.form['phno']
    email=request.form['email']
    img=request.files['image']
    path="static/image/"+str(uuid.uuid4())+img.filename
    img.save(path)
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjj",img)
    q="insert into accomodation values(null,'%s','%s','%s','%s','%s')"%(cid,name,phnoo,email,path)
    insert(q)
    
    return str(data)


@api.route('/update_img',methods=['POST','GET'])
def update_img():
    data={}
    
    id=request.form['aid']
    name=request.form['name']
    cname=request.form['cname']
    cid=get_cid(cname)
    phnoo=request.form['phno']
    email=request.form['email']
    img=request.files['image']
    path="static/image/"+str(uuid.uuid4())+img.filename
    img.save(path)
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjj",img)
    q="update accomodation set camps_id='%s',name='%s',phone='%s',email='%s',image='%s' where accomodation_id='%s'"%(cid,name,phnoo,email,path,id)
    insert(q)
    return str(data)


@api.route('/view_accomodation',methods=['GET','POST'])
def view_accomodation():
    data={}
    i="select * from accomodation inner join camps using(camps_id)"
    res=select(i)
    
    if res:
        data['status'] = 'success'
        data['method'] = 'view_accomodation'
        data['data'] = res
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['message'] = "No data found"
        print("No data found")
    
    return str(data)

@api.route('/delete_accomodation',methods=['GET','POST'])
def delete_accomodation():
    data={}
    id=request.args['id']
    i="delete from accomodation where accomodation_id='%s'"%(id)
    delete(i)
    
    return str(data)

@api.route('/add_issue_accomodation',methods=['GET','POST'])
def add_issue_accomodation():
    data={}
    id=request.args['id']
    issue=request.args['issue']
    i="insert into person_issues values(null,'%s','%s')"%(id,issue)
    insert(i)
    
    return str(data)

@api.route('/add_emergency_situations',methods=['GET','POST'])
def add_emergency_situations():
    data={}
    situation=request.args['situation']
    status=request.args['status']
    latitude=request.args['latitude']
    longitude=request.args['longitude']
    place=request.args['place']
    place_id=get_place_id(place)
    i="insert into emergency_situations values(null,'%s','%s',curdate(),'%s','%s','%s','pending')"%(place_id,situation,status,latitude,longitude)
    insert(i)
    
    data['status'] = "success"
    data['method'] = "add_emergency_situations"
    return str(data)

@api.route('/view_emergency_situations',methods=['GET','POST'])
def view_emergency_situations():
    data={}
    i="select * from emergency_situations inner join place using(place_id)"
    res=select(i)
    
    if res:
        data['status'] = 'success'
        data['method'] = 'view_emergency_situations'
        data['data'] = res
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['message'] = "No data found"
        print("No data found")
    
    return str(data)


@api.route('/view_emergency_situations_vol', methods=['GET', 'POST'])
def view_emergency_situations_vol():
    data = {}
    try:
        # Fetch the volunteer's login ID from the request
        user_id = request.args.get('id')

        if not user_id:
            data['status'] = "error"
            data['message'] = "Missing login ID"
            print("Missing login ID")
            return str(data)

        # Retrieve the place_id of the logged-in volunteer
        user_place_query = f"SELECT place_id FROM volunteer WHERE login_id = {user_id}"
        user_place_result = select(user_place_query)

        if not user_place_result:
            data['status'] = "error"
            data['message'] = "Invalid login ID or volunteer not found"
            print("Invalid login ID or volunteer not found")
            return str(data)

        place_id = user_place_result[0]['place_id']

        # Fetch emergency situations only for the volunteer's place
        emergency_query = f"""
        SELECT emergency_situations.*, place.place 
        FROM emergency_situations 
        INNER JOIN place USING(place_id) 
        WHERE emergency_situations.place_id = {place_id}
        """
        emergency_results = select(emergency_query)

        if emergency_results:
            data['status'] = 'success'
            data['method'] = 'view_emergency_situations'
            data['data'] = emergency_results
            print('Success:', data)
        else:
            data['status'] = "error"
            data['message'] = "No emergency situations found for your location"
            print("No emergency situations found")
    except Exception as e:
        data['status'] = "error"
        data['message'] = f"An error occurred: {str(e)}"
        print(f"Error: {str(e)}")

    return str(data)









@api.route('/update_emergency_situation',methods=['GET','POST'])
def update_emergency_situation():
    data={}
    
    id=request.args['id']
    latitude=request.args['latitude']
    longitude=request.args['longitude']
    z="UPDATE emergency_situations SET latitude = '%s', longitude = '%s' WHERE esituation_id = '%s'" % (latitude, longitude, id)
    insert(z)    
    data['method'] = 'update_emergency_situation'
    data['status'] = 'success'
    return str(data)


def get_user_id(id):
    y = "SELECT user_id FROM user WHERE login_id='%s'" % (id)
    result = select(y)
    if result:
        return result[0]['user_id'] 
    else:
        return None


@api.route('/submit_complaint',methods=['GET','POST'])
def submit_complaint():
    data={}
    
    id=request.args['user_id']
    # user_id=get_user_id(id)
    complaint=request.args['complaint']
    complaint=complaint.replace("'","''")
    i="insert into complaint values(null,'%s','%s','pending',curdate())" % (id,complaint)
    insert(i)
    
    data['status'] = 'success'
    data['method'] = 'submit_complaint'
    return str(data)

@api.route('/view_complaints',methods=['GET','POST'])
def view_complaints():
    data={}
    
    id=request.args['user_id']
    i="select * from complaint where user_id='%s'"%(id)
    res=select(i)
    if res:
        data['status'] = 'success'
        data['method'] = 'view_complaints'
        data['data'] = res
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['method'] = 'view_complaints'  # Add 'method' even in error responses
        data['message'] = "No data found"
        print("No data found")
    
    return str(data)

@api.route('/situations',methods=['GET','POST'])
def situations():
    data={}
    
    i="select situdation from emergency_situations"
    res=select(i)
    if res:
        data['status'] = 'datas'
        data['method'] = 'situations'
        data['data'] = res
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['message'] = "No data found"
        print("No data found")
    
    return str(data)

def get_eid(situations):
    y = "SELECT esituation_id FROM emergency_situations WHERE situdation='%s'" % (situations)
    result = select(y)
    if result:
        return result[0]['esituation_id'] 
    else:
        return None
    

@api.route('/emergency_situation',methods=['GET','POST'])
def emergency_situation():
    data={}
    situations=request.form['situation']
    eid=get_eid(situations)
    details=request.form['detail']
    img=request.files['image']
    path="static/image/"+str(uuid.uuid4())+img.filename
    img.save(path)
    print("jjjjjjjjjjjjjjjjjjjjjjjjjjjj",img)
    q="insert into update_emergency_situations values(null,'%s','%s',curdate(),'%s')"%(eid,details,path)
    insert(q)
    
    return str(data)

@api.route('/view_updated_items',methods=['GET','POST'])
def view_updated_items():
    data={}
    i="select * from update_emergency_situations inner join emergency_situations using(esituation_id)"
    res=select(i)
    if res:
        data['status'] = 'success'
        data['method'] = 'view_updated_emergency'
        data['data'] = res
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['message'] = "No data found"
        print("No data found")
    return str(data)

@api.route('/update_emer_image',methods=['GET','POST'])
def update_emer_image():
    data={}
    details=request.form['details']
    img=request.files['image']
    path="static/image/"+str(uuid.uuid4())+img.filename
    img.save(path)
    id=request.form['id']

    print(id,path,details)
    i="update update_emergency_situations set details='%s', date=curdate(), images='%s' where updesitaution_id='%s'"%(details,path,id)
    insert(i)
    
    
    return str(data)

@api.route('/view_updated_situations',methods=['GET','POST'])
def view_updated_situations():
    data={}
    o="select * from update_emergency_situations inner join emergency_situations using(esituation_id)"
    res=select(o)
    
    if res:
        data['status'] = 'success'
        data['method'] = 'view_updated_situations'
        data['data'] = res
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['message'] = "No data found"
        print("No data found")
    
    return str(data)


@api.route('/live_volunteers', methods=['GET', 'POST'])
def live_volunteers():
    data = {}
    try:
        user_id = request.args.get('id')
        
        if not user_id:
            data['status'] = "error"
            data['message'] = "Missing login ID"
            print("Missing login ID")
            return str(data)
        
        user_place_query = f"SELECT place_id FROM volunteer WHERE login_id = {user_id}"
        user_place_result = select(user_place_query)
        
        if not user_place_result:
            data['status'] = "error"
            data['message'] = "Invalid login ID or user not found"
            print("Invalid login ID or user not found")
            return str(data)
        
        place_id = user_place_result[0]['place_id']

        volunteer_query = f"SELECT login_id, CONCAT(fname, ' ', lname) AS username FROM volunteer WHERE place_id = {place_id} AND login_id != {user_id}"
        volunteer_results = select(volunteer_query)

        if volunteer_results:
            data['status'] = "success"
            data['method'] = "live_volunteers"
            data['data'] = [{"id": volunteer['login_id'], "name": volunteer['username']} for volunteer in volunteer_results]
            print('Success:', data)
        else:
            data['status'] = "error"
            data['message'] = "No volunteers found in the same place"
            print("No volunteers found")
    
    except Exception as e:
        data['status'] = "error"
        data['message'] = f"An error occurred: {str(e)}"
        print(f"Error: {str(e)}")
    
    return str(data)
# @api.route('/live_volunteers', methods=['GET', 'POST'])
# def live_volunteers():
#     data = {}
    
#     user_id = request.args.get('id')
#     volunteer_query = f"SELECT login_id, CONCAT(fname, ' ', lname) AS username FROM volunteer WHERE login_id != {user_id}"
#     volunteer_results = select(volunteer_query)

#     if volunteer_results:
#         data['status'] = "success"
#         data['method'] = "live_volunteers"
#         data['data'] = [{"id": volunteer['login_id'], "name": volunteer['username']} for volunteer in volunteer_results]
#         print('Success:', data)
#     else:
#         data['status'] = "error"
#         data['message'] = "No volunteers found in the same place"
#         print("No volunteers found")
    
    
    
#     return str(data)


@api.route('/chat',methods=['GET','POST'])
def chat():
    data={}
    sender=request.args['sender_id']
    reciver=request.args['reciver_id']
    details=request.args['details']
    details = details.replace("'", "''")
    
    
    i="insert into chat values(null,'%s','%s','%s',curdate())"%(sender,reciver,details)
    insert(i)
    data['status'] = 'success'
    data['method'] = 'chats'
    return str(data)


@api.route('/chatdetail',methods=['GET','POST'])
def chatdetail():
    data={}
    sender=request.args['sender_id']
    reciver=request.args['receiver_id']
    r="select * from chat where (sender_id='%s' and reciver_id='%s' or sender_id='%s' and reciver_id='%s') "%(sender,reciver,reciver,sender)
    res=select(r)
    if res:
        data = {
            'status': 'success',
            'method': 'chatdetail',
            'data': res
        }
    else:
        data = {
            'status': 'error',
            'method': 'chatdetail',
            'message': 'No data found'
        }
    
    return str(data)

@api.route('/update_emergency_reply',methods=['GET','POST'])
def update_emergency_reply():
    data={}
    id=request.args['id']
    reply=request.args['reply']
    
    p="update emergency_situations set reply='%s'where esituation_id='%s'"%(reply,id)
    insert(p)

    return str(data)

@api.route('/view_free_space',methods=['GET','POST'])
def view_free_space():
    data={}
    i="select * from free_space inner join camps using(camps_id)"
    res=select(i)
    if res:
        data['status'] = 'success'
        data['method'] = 'view_free_space'
        data['data'] = res
        print('Success:', data) 
    else:
        data['status'] = "error"
        data['method'] = 'no free space'
        data['message'] = "No data found"
        print("No data found")

    return str(data)

@api.route('/manage_issues',methods=['GET','POST'])
def manage_issues():
    data={}
    issue=request.args['issue']
    place=request.args['place']
    place_id=get_place_id(place)

    i="insert into issues values(null,'%s','%s',curdate(),'pending')"%(place_id,issue)
    insert(i)
    data['method'] = 'manage_issues'
    data['status'] = 'success'  
    
    return str(data)

@api.route('/update_issue',methods=['GET','POST'])
def update_issue():
    data={}
    id=request.args['id']
    issue=request.args['issue']
    place=request.args['place']
    place_id=get_place_id(place)
    data['method'] = 'update_issue'
    data['status'] = 'success'
    i="update issues set issue='%s', place_id='%s' where issue_id='%s'"%(issue,place_id,id)
    insert(i)
    
    return str(data)


@api.route('/update_camp',methods=['GET','POST'])
def update_camp():
    data={}
    id=request.args['id']
    cname=request.args['camp_name']
    place=request.args['place']
    place_id=get_place_id(place)
    placedetails=request.args['place_details']

    i="update camps set place_id='%s', camp_name='%s', place_details='%s' where camps_id='%s'"%(place_id,cname,placedetails,id)
    insert(i)
    data['status'] = "success"
    data['method'] = "camp added sucessfully"

    return str(data)

@api.route('/delete_accommodation',methods=['GET','POST'])
def delete_accommodation():
    data={}
    id=request.args['id'] 
    i="delete from accomodation where accomodation_id='%s'"%(id)
    delete(i)
    
    return str(data)


@api.route('/update_urgent_need',methods=['GET','POST'])
def update_urgent_need():
    data={}
    id=request.args['id'] 
    type=request.args['type']
    needs=request.args['needs']
    details=request.args['details']

    i="update needs set type='%s',needs='%s',details='%s' where needs_id='%s'"%(type,needs,details,id)
    insert(i)
    
    return str(data)



from floodpredicts import *
from pred import *






@api.route('/predict_disaster', methods=['GET', 'POST'])
def predict_disaster():
    data = {}
    try:
        # Handle both GET and POST requests
        if request.method == 'POST':
            # Get parameters from form data
            lati = float(request.form['lati'])
            longi = float(request.form['longi'])
            rain = float(request.form['rain'])
            tem = float(request.form['tem'])
            humi = float(request.form['humi'])
            raindis = float(request.form['raindis'])
            water = float(request.form['water'])
            land = float(request.form['land'])
            landcov = request.form['landcov']
            soil = request.form['soil']
            population = float(request.form['population'])
            infr = int(request.form['infr'])
            hisflood = int(request.form['hisflood'])
        else:
            # Get parameters from query string
            lati = float(request.args['lati'])
            longi = float(request.args['longi'])
            rain = float(request.args['rain'])
            tem = float(request.args['tem'])
            humi = float(request.args['humi'])
            raindis = float(request.args['raindis'])
            water = float(request.args['water'])
            land = float(request.args['land'])
            landcov = request.args['landcov']
            soil = request.args['soil']
            population = float(request.args['population'])
            infr = int(request.args['infr'])
            hisflood = int(request.args['hisflood'])

        outs = predictflooded(lati, longi, rain, tem, humi, raindis, water, land, landcov, soil, population, infr, hisflood)
        data['outs'] = outs
        data['status'] = 'success'
    except KeyError as e:
        data['status'] = 'error'
        data['message'] = f'Missing parameter: {str(e)}'
    except ValueError as e:
        data['status'] = 'error'
        data['message'] = f'Invalid parameter value: {str(e)}'
    except Exception as e:
        data['status'] = 'error'
        data['message'] = f'An error occurred: {str(e)}'
    
    return str(data)
