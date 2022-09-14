from flask import Flask, render_template, request
from wtforms import Form, validators, StringField, BooleanField, DateTimeField, SelectField, PasswordField
from wtforms.fields import html5 as h5fields
from wtforms.widgets import html5 as h5widgets
from wtforms.widgets import TextArea

# create a server instance
app = Flask(__name__)

# create form object
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