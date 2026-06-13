#!/usr/bin/python3

"""Basic Auth, JWT Auth, and role-based access control API."""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash


app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "helloworld"

auth = HTTPBasicAuth()
jwt = JWTManager(app)


users = {
    "user1": {
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "password": generate_password_hash("adminpass"),
        "role": "admin",
    },
}


@auth.verify_password
def verify_password(username, password):
    user = users.get(username)

    if user and check_password_hash(user["password"], password):
        return username

    return None


@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")
    user = users.get(username)

    if not user or not check_password_hash(user["password"], password):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity=username)

    return jsonify({"access_token": access_token})


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    username = get_jwt_identity()
    user = users.get(username)

    if not user or user.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(debug=True)
