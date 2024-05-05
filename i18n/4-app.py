#!/usr/bin/env python3
"""Base flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)


class Config(object):
    """Setups"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale"""
    lang = request.args.get("locale")
    if lang in app.config["LANGUAGES"]:
        return lang
    else:
        return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def home():
    """ Home Page
    """
    return render_template('4-index.html')


if __name__ == "__main__":
    app.run("0.0.0.0", 5000)
