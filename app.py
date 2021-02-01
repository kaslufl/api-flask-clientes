from flask import Flask
from flask_restful import Api
from resources.cliente import Cliente, Cliente_com_codigo
from flask_cors import CORS

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost/smartnx'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
api = Api(app)
CORS(app)

@app.before_first_request
def create_database():
    db.create_all()

api.add_resource(Cliente, "/cliente")
api.add_resource(Cliente_com_codigo, "/cliente/<int:codigo>")

if __name__ == '__main__':
    from sql_alchemy import db
    db.init_app(app)
    app.run(debug=True)