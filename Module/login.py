from flask import Flask,request,jsonify
import sqlite3

def login():
    if request.method=="POST":
        data=request.get_json()
        username=data.get("username")
        password=data.get("password")
        if (not username or not password):
            return "Username or password invalid"
        connectdb=sqlite3.connect("PaperTrail.db")
        c=connectdb.cursor()
        c.execute("SELECT * FROM new_user WHERE username = ? AND password = ?",(username,password))
        login_users=c.fetchone()
        connectdb.close()
        if login_users:
            return "Login Successfully"
        else:
            return jsonify({"error": "Invalid username or password!"}), 401

