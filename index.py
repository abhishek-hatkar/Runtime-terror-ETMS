from flask import Flask , jsonify ,request, render_template,redirect,url_for,send_from_directory,flash
from sqlalchemy import create_engine, MetaData,Table,Column,Integer,String


app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# app.secret_key = "secret"
# # If you’re using middleware or the HTTP server to serve files, you can register the download_file 
# # endpoint as build_only so url_for will work without a view function.
# app.add_url_rule(
#     "/downloadfile/<name>", endpoint="download_file", build_only=True
# )


# from sqlalchemy.sql import ForeignKey,insert

engine=create_engine ('mysql://root:brainbeam@localhost/ETMS',echo=True)

meta= MetaData()

demoss = Table(

   'demoss', meta,

   Column('emp_id', Integer, primary_key = True),
   Column('firstname', String(100)),
   Column('lastname', String(100)),
   Column('image', String(100)),
   Column('email', String(100)),
   Column('skills', String(100))
)

conn=engine.connect()
# class datastore:
#     myotp = " "
    
# data = datastore()
def create_table():
    meta.create_all(engine)
# full_filename = os.path.join(app.config['UPLOAD_FOLDER'], 'image.jpg')
# create_table()
@app.route('/login')

def login():
    return render_template("login.html")
    
@app.route('/signup')
def signup():
    return render_template("signup.html")
@app.route('/view_all_emp')

def display_all_emp():
    
    stmt=demoss.select()

    exe=conn.execute(stmt)

    displaylist=[dict(row) for row in exe]
    print(displaylist)
    return render_template('home.html',emp=displaylist)

@app.get('/new_emp')
def add_emp():
    return render_template("addemps.html")
@app.post('/newemps')

    # return render_template("adddoctors.html")
def add_new_doctor():
    
    print(request.files['file'])
    print(request.url)
    print(app.config['UPLOAD_FOLDER'])
    # use secure_filename If you want to use the filename of the client to store the file on the server
    file = request.files['file']
    # If the user does not select a file, the browser submits an
    # empty file without a filename.
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        uploadedfileurl = url_for('static', filename = filename)
        # return f'Thanks, the file got saved and here is your uploaded file url {uploadedfileurl})'
        print( uploadedfileurl)
    id =request.form['id']
    firstname = request.form['firstname']
    lastname = request.form['lastname']
    image =  uploadedfileurl
    email = request.form['email']
    mobile = request.form['mobile']
    doctortuple=(id,firstname,lastname,image,email,mobile)
    stmt=demoss.insert().values(doctortuple)
    exe=conn.execute(stmt)
    return render_template("adddoctors.html")
    # return "<html><body><h1>its WOrking</h1></body><html>"
    
  
  
  
  
  
  
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS   
    
 
@app.errorhandler(404)
def page_error(error):
    return render_template('error.html'), 404

if __name__ == '__main__':
    app.run(debug=True)