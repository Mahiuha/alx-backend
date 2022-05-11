#!/usr/bin/env python3
"""Task 4"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Simple configuration"""
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """Gets locale"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(Config['LANGUAGES'])


@app.route("/", methods=['GET'])
def index():
    """Index of route"""
    return render_template("3-index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
