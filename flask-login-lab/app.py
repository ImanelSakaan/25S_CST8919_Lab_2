from flask import Flask, request, jsonify
import logging

app = Flask(__name__)

# Configure logging to console
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')

# Simple user database (for demo)
users = {"user1": "password1", "user2": "password2"}

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username in users and users[username] == password:
        app.logger.info(f"Successful login attempt for user: {username}")
        return jsonify({"message": "Login successful"}), 200
    else:
        app.logger.warning(f"Failed login attempt for user: {username}")
        return jsonify({"message": "Login failed"}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
