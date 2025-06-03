from flask import Flask
import fdb
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])

app.config.from_pyfile('config.py')

host = app.config['DB_HOST']
database = app.config['DB_NAME']
user = app.config['DB_USER']
password = app.config['DB_PASSWORD']

try:
    con = fdb.connect(host=host, database=database, user=user, password=password)
    print("Conexao estabelicida com sucesso")
except Exception as e:
    print(f"Erroooooo {e}")

from view import *

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)