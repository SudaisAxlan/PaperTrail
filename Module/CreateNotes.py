from flask import Flask,jsonify,request
import sqlite3


def CreateNotes():
    
    if request.method == "POST":
        # Get the JSON data from the request
        data = request.get_json()

        # Extract user_id, title, and content from the JSON data
        user_id = data.get("user_id")
        title = data.get("title")
        content = data.get("content")

        # Check if all required data is provided
        if not user_id or not title or not content:
            return "error : userid title or content are requred",200
            
            # return jsonify({"error": "User ID, title, and content are required."}), 400

        # Connect to SQLite database (or create it if it doesn't exist)
        conn = sqlite3.connect('PaperTrail.db')
        c = conn.cursor()

        # Create the Notes table if it doesn't exist already
        c.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER NOT NULL,
                title TEXT,
                content TEXT NOT NULL,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
            )
        ''')

        # Insert the note data into the Notes table
        c.execute('''
            INSERT INTO notes (user_id, title, content)
            VALUES (?, ?, ?)
        ''', (user_id, title, content))

        # Commit changes and close the connection
        conn.commit()
        conn.close()
        # Return a success message
        return jsonify({"message": "Note created successfully!"}), 200

    # Return error if the method is not POST
    return jsonify({"error": "Invalid request method. Use POST."}), 400
    
    


