import os

from settings import SERVER_PORT
from app import create_app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=SERVER_PORT)
