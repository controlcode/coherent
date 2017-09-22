import logging

from flask import Blueprint, redirect, url_for, render_template
from structlog import wrap_logger

logger = wrap_logger(logging.getLogger(__name__))

login_bp = Blueprint('login_bp', __name__, static_folder='static', template_folder='coherent/templates/login')

@login_bp.route('/login', methods=['GET'])
def login():
    return render_template('login/login.html', _theme='default')