import logging

from flask import Blueprint, jsonify, make_response
from structlog import wrap_logger


logger = wrap_logger(logging.getLogger(__name__))

health_bp = Blueprint('health_bp', __name__, static_folder='static', template_folder='templates')

@health_bp.route('/', methods=['GET'])
def get_info():
    return jsonify(status="healthy")