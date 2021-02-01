from flask_restful import Resource, reqparse, abort, fields, marshal_with
from models.cliente import ClienteModel

cliente_post_args = reqparse.RequestParser()
cliente_post_args.add_argument("nome", type = str, help = "Nome do cliente precisa ser preenchido!", required = True)
cliente_post_args.add_argument("razao_social", type = str, help = "Razão social do cliente precisa ser preenchido!", required = True)
cliente_post_args.add_argument("cnpj", type = str, help = "CNPJ do cliente precisa ser preenchido!", required = True)

cliente_patch_args = reqparse.RequestParser()
cliente_patch_args.add_argument("nome", type = str, help = "Nome do cliente")
cliente_patch_args.add_argument("razao_social", type = str, help = "Razão social")
cliente_patch_args.add_argument("cnpj", type = str, help = "CNPJ do cliente")
cliente_patch_args.add_argument("data_inclusao",type = str, help = "Data de inclusão")

resource_fields = {
    'codigo' : fields.Integer,
    'nome' : fields.String,
    'razao_social' : fields.String,
    'cnpj' : fields.String,
    'data_inclusao' : fields.DateTime
}

class Cliente(Resource):
    @marshal_with(resource_fields)
    def post(self):
        hoje = ClienteModel.pega_data_atual()
        args = cliente_post_args.parse_args()
        cliente = ClienteModel(nome = args['nome'], razao_social = args['razao_social'], cnpj = args['cnpj'], data_inclusao = hoje)
        cliente.salva_cliente()
        return cliente, 201 #Created

    def get(self):
        return {'clientes': [cliente.json() for cliente in ClienteModel.query.all()]}

class Cliente_com_codigo(Resource):
    @marshal_with(resource_fields)
    def get(self, codigo):
        result = ClienteModel.verifica_codigo(codigo)
        if not result:
            abort(404, message = "Cliente não encontrado")
        return result

    @marshal_with(resource_fields)
    def patch(self, codigo):
        args = cliente_patch_args.parse_args()
        result = ClienteModel.verifica_codigo(codigo)
        if not result:
            abort(404, message = "Cliente não encontrado")

        if args['nome']:
            result.nome = args['nome']
        
        if args['razao_social']:
            result.razao_social = args['razao_social']
        
        if args['cnpj']:
            result.cnpj = args['cnpj']
        
        if args['data_inclusao']:
            result.data_inclusao = args['data_inclusao']
        
        result.salva_cliente()
        return result

    def delete(self, codigo):
        result = ClienteModel.verifica_codigo(codigo)
        if not result:
            abort(404, message = "Cliente não encontrado")
        result.deleta_cliente()
        return '', 204 #No content