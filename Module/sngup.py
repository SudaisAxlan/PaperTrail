from flask import Flask,request,jsonify
import sqlite3
from flask_mail import Mail, Message
# mail = None


# def userRegister():
#     if request.method == "POST":
#         # Get JSON data from the request
#         data = request.get_json()

#         # Extract username, email, and password from the JSON data
#         username = data.get("username")
#         email = data.get("email")
#         password = data.get("password")

#         # Connect to SQLite database (or create it if it doesn't exist)
#         conn = sqlite3.connect('PaperTrail.db')
#         c = conn.cursor()

#         # Create the table if it doesn't already exist
#         c.execute('''
#             CREATE TABLE IF NOT EXISTS new_user (
#                 id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 username TEXT NOT NULL,
#                 email TEXT NOT NULL,
#                 password TEXT NOT NULL
#             )
#         ''')
#         # Insert user data from the request
#         c.execute('''
#             INSERT INTO new_user(username, email, password)
#             VALUES (?, ?, ?)
#         ''', (username, email, password))

#         # Commit changes and close the connection
#         conn.commit()
#         conn.close()

#         # Send a welcome email to the user
#         try:
#             msg = Message(
#                 subject="Welcome to PaperTrail!",
#                 recipients=[email],
#                 body=f"Hi {username},\n\nThank you for registering with PaperTrail. We're excited to have you on board!\n\nBest regards,\nThe PaperTrail Team"
#             )
#             mail.send(msg)
#         except Exception as e:
#             return jsonify({"error": f"Failed to send email: {str(e)}"}), 500

#         # Return a success message
#         return jsonify({"message": "User successfully registered and email sent!"}), 200

#     return jsonify({"error": "Invalid request method. Use POST."}), 400




def userRegister():

    if request.method == "POST":
        # Get JSON data from the request
        data = request.get_json()

        # Extract username, email, and password from the JSON data
        username = data.get("username")
        email = data.get("email")
        password = data.get("password")

        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('PaperTrail.db')
        c = conn.cursor()

        # Create the table if it doesn't already exist
        
        c.execute('''
            CREATE TABLE IF NOT EXISTS new_user (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        # Insert user data from the request
        c.execute('''
            INSERT INTO new_user(username, email, password)
            VALUES (?, ?, ?)
        ''', (username, email, password))

        # Commit changes and close the connection
        conn.commit()
        conn.close()


        # Return a success message
        return jsonify({"message": "User successfully registered!"}), 200

    return jsonify({"error": "Invalid request method. Use POST."}), 400