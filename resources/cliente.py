from flask_restful import Resource, reqparse, abort, fields, marshal_with
from models.cliente import ClienteModel

cliente_post_args = reqparse.RequestParser()
cliente_post_args.add_argument("nome", type = str, help = "Nome do cliente precisa ser preenchido!", required = True)
cliente_post_args.add_argument("razao_social", type = str, help = "Razão social do cliente precisa ser preenchido!", required = True)
cliente_post_args.add_argument("cnpj", type = str, help = "CNPJ do cliente precisa ser preenchido!", required = True)
#cliente_post_args.add_argument("data_inclusao",type = str, help = "Data de inclusão", required = True)

resource_fields = {
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

class Cliente_com_codigo(Resource):
    @marshal_with(resource_fields)
    def get(self, codigo):
        result = ClienteModel.verifica_codigo(codigo)
        if not result:
            abort(404, message = "Cliente não encontrado")
        return result

    def patch(self, codigo):
        pass

    def delete(self, codigo):
        result = ClienteModel.verifica_codigo(codigo)
        if not result:
            abort(404, message = "Cliente não encontrado")
        result.deleta_cliente()
        return '', 204 #No content