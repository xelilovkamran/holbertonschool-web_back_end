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
    pwd: str = request.form.get("password")

    if not email:
        return jsonify({"error": "email missing"}, 400)

    if not pwd:
        return jsonify({"error": "password missing"}, 400)

    users: TypeVar('User') = User.search({"email": email})

    if len(users) == 0:
        return jsonify({"error": "no user found for this email"}, 400)

    for user in users:
        if user.is_valid_password(pwd):
            from api.v1.app import auth
            session_id = auth.create_session(user.id)
            SESSION_NAME = getenv('SESSION_NAME')
            response = make_response(user.to_json())
            response.set_cookie(SESSION_NAME, session_id)
            return response

    return jsonify({"error": "wrong password"}, 401)
