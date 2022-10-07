from modulefinder import Module
from pyexpat import model
from flask import Flask, render_template,url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String


app = Flask(__name__)
    
@app.route("/")
def home():
    return render_template('frontpage.html')

@app.route("/admin_login")
def AdminLogin():
    return render_template('admin_login.html')

@app.route("/admin_register")
def AdminRegister():
    return render_template('admin_register.html')

@app.route("/hr_login")
def HrLogin():
    return render_template('hr_login.html')

@app.route("/hr_register")
def HrRegister():
    return render_template('hr_register.html')

@app.route("/admin_page")
def AdminPage():
    return render_template('adminpage.html')

@app.route("/hr_page")
def HrPage():
    return render_template('hrpage.html')

@app.route("/hrsearchpage")
def HrSearchPage():
    return render_template('hrsearchpage.html')
if __name__ == '__main__':
    app.run(debug=True)