from .app import app
from .routes import *
from database import create_db
from algo import init_algo
import os


def main():
    port = os.environ.get('PORT', 5000)
    init_algo()
    app.run(debug=True, port=port, host='0.0.0.0')
