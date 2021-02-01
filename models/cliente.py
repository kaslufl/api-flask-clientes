from sql_alchemy import db
from datetime import date

class ClienteModel(db.Model):
    __tablename__ = 'cliente'
    
    codigo = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(100), nullable=False)
    razao_social = db.Column(db.String(100), nullable=False)
    cnpj = db.Column(db.String(12), nullable=False)
    data_inclusao = db.Column(db.DateTime, nullable=False)

    def __init__(self, nome, razao_social, cnpj, data_inclusao):
        self.nome = nome
        self.razao_social = razao_social
        self.cnpj = cnpj
        self.data_inclusao = data_inclusao
    
    def __repr__(self):
        return f"Cliente(nome = {nome}, razão social = {razao_social}, cnpj = {cnpj}, data de inclusão = {data_inclusao})"

    def json(self):
        return {
            'codigo': self.codigo,
            'nome': self.nome,
            'razao_social': self.razao_social,
            'cnpj': self.cnpj,
            'data_inclusao': self.data_inclusao.isoformat()
        }

    @classmethod
    def pega_data_atual(cls):
        hoje = date.today()
        return hoje

    def salva_cliente(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def verifica_codigo(cls, codigo):
        result = cls.query.filter_by(codigo = codigo).first()
        if result:
            return result
        return None

    def deleta_cliente(self):
        db.session.delete(self)
        db.session.commit()