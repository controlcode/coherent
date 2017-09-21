from flask import Flask

app = Flask(__name__)

from coherent.views.login import login_bp
app.register_blueprint(login_bp)