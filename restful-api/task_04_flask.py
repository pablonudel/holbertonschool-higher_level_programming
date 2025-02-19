#!/usr/bin/python3
"""Module for handling routes with Flask to respond to different endpoints"""
from flask import Flask, request, jsonify


app = Flask(__name__)
users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
        },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
        }
    }


@app.route('/')
def home():
    """Return a str in root path"""
    return "Welcome to the Flask API!"


@app.route('/data')
def list_users():
    """Return list of users in data path"""
    return [user for user in users]


@app.route('/status')
def send_status():
    """Return a str in status path"""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Return a user data in users dynamic path"""
    if username in users:
        res = jsonify(users[username])
        return res
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """Return a user in users dict"""
    data = request.get_json()
    if not data or "username" not in data:
        res = jsonify({"error": "Username is required"})
        return res, 400
    users[data["username"]] = data
    res = jsonify({"message": "User added", "user": data})
    return res, 201


if __name__ == "__main__":
    app.run()
