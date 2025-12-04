from flask import Flask
from public import public
from admin import admin
from counselor import counselor
from volunteer_head import volunteer_head
from api import api

app=Flask(__name__)

app.secret_key="hello"

app.register_blueprint(admin)
app.register_blueprint(public)
app.register_blueprint(counselor)
app.register_blueprint(volunteer_head)
app.register_blueprint(api,url_prefix='/api')

app.run(debug=True,host="0.0.0.0",port=5105)