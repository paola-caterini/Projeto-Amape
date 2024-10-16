from datetime import datetime

class Professor:
    def __init__(self, cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email, data_cadastro=None):
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.especialidade = especialidade
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.data_cadastro = data_cadastro or datetime.now().strftime('%Y-%m-%d %H:%M:%S')

   