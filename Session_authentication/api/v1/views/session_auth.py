from api.v1.views import app_views
from flask import request, jsonify, make_response
from typing import TypeVar
from models.user import User
from os import getenv


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """ POST /auth_session/login
    """
    email: str = request.form.get("email")

    if not email:
        return make_response(jsonify({"error": "email missing"}), 400)

    pwd: str = request.form.get("password")

    if not pwd:
        return make_response(jsonify({"error": "password missing"}), 400)

    users = User.search({"email": email})

    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}), 400

    from api.v1.app import auth
    for user in users:
        if user.is_valid_password(pwd):
            session_id = auth.create_session(user.id)
            SESSION_NAME = getenv('SESSION_NAME', "_my_session_id")
            response = make_response(user.to_json())
            response.set_cookie(SESSION_NAME, session_id)
            return response

    return make_response(jsonify({"error": "wrong password"}), 401)
