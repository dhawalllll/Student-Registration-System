from flask import *

import sqlite3,os

app = Flask(__name__)

app.secret_key = "@Eatqsqw12163627e23e7ediu"

app.config['UPLOAD_FOLDER'] = "C:/Users/Shree/Desktop/myflaskproject,py/static/images/"

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/registration")
def registration():
    return render_template("registration.html")

@app.route("/student_list")
def student_list():
    con = sqlite3.connect("mydb.db")
    c = con.cursor()
    c.execute("select * from student order by id desc")
    data = c.fetchall()

    return render_template("student_list.html",data=data)

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/formsave",methods=["POST","GET"])
def formsave():
    if request.method == "POST":
        fn = request.form["fullname"]
        em = request.form["email"]
        ps = request.form["password"]
        ad = request.form["address"]

        f = request.files["photo"]
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))


        con = sqlite3.connect("mydb.db")
        c = con.cursor()
        c.execute("insert into student(fullname,email,password,address,photo)values(?,?,?,?,?)",(fn,em,ps,ad,f.filename))
        con.commit()
        



        return redirect(url_for('student_list'))
    else:
        return "Fail"
    
@app.route("/delete/<int:id>")
def deletestudent(id):
    con = sqlite3.connect("mydb.db")
    c = con.cursor()
    c.execute("delete from student where id=?", [id])
    con.commit()
    return redirect(url_for('student_list'))

@app.route("/profileedit/<int:id>")
def profileedit(id):
    con = sqlite3.connect("mydb.")
    c = con.cursor()
    c.execute("select * from student where id=?", [id])
    data = c.fetchone()
    return render_template("profileedit.html",data=data)


@app.route("/profilesave",methods=["POST","GET"])
def profilesave():
    if request.method == "POST":
        fn = request.form["fullname"]
        em = request.form["email"]
        ps = request.form["password"]
        ad = request.form["address"]
        

        con = sqlite3.connect("mydb.db")
        c = con.cursor()
        c.execute("update student set full_name=?,emai=?,password=?,address=? where id=?",(fn,em,ps,ad,id))
        con.commit()
        return redirect(url_for('student_list'))
    else:
    
        return redirect(url_for('student_list'))
    
@app.route("/logincheck",methods=["POST","GET"])
def logincheck():
    if request.method == "POST":
        em = request.form["email"]
        ps = request.form["password"]

        con = sqlite3.connect("mydb.db")
        c = con.cursor()
        c.execute("select * from student where email=? and password=?",(em,ps))
        data = c.fetchall()

        if data:
            session["username"] = em#session start
            return redirect(url_for("dashboard"))
        else:
            return redirect(url_for("login"))   

        
             
@app.route("/dashboard")
def dashboard():
    if session.get("username") is not None:
        return render_template("dashboard.html")
    
    else:
        return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("username",None) #Session End
    return redirect(url_for("login"))


@app.route("/addcookie")
def addcookie():
    res = make_response(render_template("home.html"))
    res.set_cookie("mobile","samsung")#set cookie
    res.set_cookie("price", "10000")
    return res

@app.route("/view_cookie")
def view_cookie():
    m = request.cookies.get("mobile")#get cookie
    return "%s" %m

@app.route("/fileupload")
def fileupload():
    return render_template("fileupload.html")

@app.route("/filesave",methods=["POST","GET"])
def filesave():
    if request.method == "POST":
        f = request.files["photo"]
        f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,f.filename))
        




        return "file upload successfully"
    
    else:
        return "Fail"
    



if __name__ == '__main__':
    app.run(debug=True)


    
