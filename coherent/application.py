import logging

from flask import Flask
from flask_wtf.csrf import CSRFProtect

from coherent.logger_config import logger_initial_config
from structlog import wrap_logger

logger_initial_config(service_name='coherent')
logger = wrap_logger(logging.getLogger(__name__))

app = Flask(__name__)

csrf = CSRFProtect(app)

from coherent.views.login import login_bp
app.register_blueprint(login_bp)

logger.info('Starting Coherent UI')