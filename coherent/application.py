import os
import logging

from flask import Flask, redirect, url_for
from flask_wtf.csrf import CSRFProtect

from coherent.logger_config import logger_initial_config
from structlog import wrap_logger

logger_initial_config(service_name='coherent')
logger = wrap_logger(logging.getLogger(__name__))

app = Flask(__name__)

csrf = CSRFProtect(app)

from coherent.views.login import login_bp
from coherent.views.health import health_bp
app.register_blueprint(login_bp)
app.register_blueprint(health_bp, url_prefix='/health')

logger.info('Starting Coherent UI')

@app.route('/', methods=['GET'])
def home():
    return redirect(url_for('login_bp.login', _external=True, _scheme=os.getenv('SCHEME', 'http')))
