from sql_alchemy import db
from datetime import date

class ClienteModel(db.Model):
    __tablename__ = 'cliente'
    
    codigo = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    razao_social = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(12), nullable=False)
    data_inclusao = db.Column(db.DateTime, nullable=False)

    def __init__(self, codigo, nome, razao_social, cnpj, data_inclusao):
        self.codigo = codigo
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.data_inclusao = data_inclusao