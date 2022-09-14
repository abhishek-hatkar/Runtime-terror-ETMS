from flask import Flask, render_template, flash, redirect, url_for, request, session, logging
from sqlalchemy import create_engine, MetaData,Table,Column,Integer,String
from sqlalchemy.sql import ForeignKey,insert
from wtforms import Form, validators, StringField, BooleanField, DateTimeField, SelectField, PasswordField
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets
from wtforms.widgets import TextArea
app = Flask(__name__)

engine=create_engine ('mysql://root:brainbeam@localhost/ETMS',echo=True)
meta= MetaData()

demoss = Table(

   'demoss', meta,

   Column('emp_id', Integer, primary_key = True),
   Column('firstname', String(100)),
   Column('lastname', String(100)),
   Column('image', String(100)),
   Column('email', String(100)),
   Column('skills', String(100)),
   Column('certifications', String(100)),
   Column('trainings attended', String(100))
)

conn=engine.connect()
# class datastore:
#     myotp = " "
# data = datastore()
def create_table():
    meta.create_all(engine)
# full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
# create_table()


class UserRegisterForm(Form):
    uFirstName = StringField("First Name", validators=[
                        validators.InputRequired(), validators.Length(min=3, max=250)])
    uLastName = StringField("Last Name", validators=[
                        validators.InputRequired(), validators.Length(min=3, max=250)])        

    uPass = PasswordField("Password", validators=[
                        validators.InputRequired(), validators.Length(min=4, max=15)])
    
    uEmail = StringField("Email", validators=[validators.InputRequired()])
    isGetEmails = BooleanField("Get Promotional Emails", default=False)
   

# route handler
@app.route("/", methods=["GET", "POST"])
def index():
    form = UserRegisterForm(request.form)
    if request.method == "POST" and form.validate():
        uName = request.form["uName"]
        print("First Name=", form.uFirstName)
        print("Last Name=", form.uLastName )
        print("Password =", form.uPass.data)
        
        print("Email =", form.uEmail.data)
        print("Get Emails =", form.isGetEmails.data)
       
        if not uName[0].isalpha():
            form.uName.errors.append("Username should start with an alphabet")
    return render_template("home.html", form=form)

# run the server
app.run(host="0.0.0.0", port=50100, debug=True)



@app.route('/view_all_emp')
def display_all_emp():
    
    stmt=demoss.select()

    exe=conn.execute(stmt)

    displaylist=[dict(row) for row in exe]
    print(displaylist)
    return render_template('home.html',emp=displaylist)



