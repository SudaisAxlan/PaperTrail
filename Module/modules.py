from flask import Blueprint, render_template, request, redirect, url_for,jsonify
# from Routes.AllRoutes import routes
import sqlite3

# get Notes
def homes():
    
     conn = sqlite3.connect('PaperTrail.db')
     c = conn.cursor()
   
     c.execute('SELECT title, content FROM notes')
     rows = c.fetchall()
     conn.close()
     notes = []
     for note in rows:
        notes.append({
            "title": note[0],
            "content": note[1]
        })
     return jsonify({"notes": notes}), 200 
 
 
#  Create Notes


