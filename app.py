import os

from flask import Flask, render_template
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    commit = os.getenv('COMMIT', default=123456)
    username = request.args.get("username", "")
    return render_template('index.html', username=username, commit=commit)
