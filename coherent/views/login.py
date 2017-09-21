import os
import logging

from coherent.application import app
from flask import Blueprint, redirect, url_for, render_template

login_bp = Blueprint('login_bp', __name__, static_folder='static', template_folder='coherent/templates/login')

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('login_bp.login', _external=True, _scheme=os.getenv('SCHEME', 'http')))

@login_bp.route('/login', methods=['GET'])
def login():
    return render_template('login/login.html', _theme='default')