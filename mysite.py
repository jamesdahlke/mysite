from flask import Flask
from flask import render_template
from flask import url_for
from flask import request
import sqlite3 as sql 
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
@app.route ("/myform")
def new_myform():
        
        return render_template("form.html")
def create_database():
        conn=sql.connect("myb.db")
        conn.execute("CREATE TABLE profile (name TEXT, address TEXT)")
        conn.close()

# create_database()
  
    
@app.route ("/display")
def display_data():
        con = sql.connect("myb.db")
        con.row_factory =sql.Row

        cur = con.cursor()
        cur.execute("select * from profile")
        rows= cur.fetchall()
        return render_template("list.html", rows = rows)

@app.route ("/post", methods=['GET','POST'])
def post():
        if request.method == "POST":
               name = request.form["nm"]
               addr = request.form["add"]
        
        with sql.connect("myb.db") as con:
                cur = con.cursor()
                cur.execute("INSERT INTO profile (name, address) VALUES (?,?)", [name,addr])
        con.commit
        return render_template("list.html")