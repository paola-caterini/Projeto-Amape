# dominio/morador.py
class Morador:
    def __init__(self, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email):
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.filiacao = filiacao
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def atualizar(self, nome_completo=None, filiacao=None, data_nascimento=None, endereco=None, telefone=None, email=None):
        if nome_completo:
            self.nome_completo = nome_completo
        if filiacao:
            self.filiacao = filiacao
        if data_nascimento:
            self.data_nascimento = data_nascimento
        if endereco:
            self.endereco = endereco
        if telefone:
            self.telefone = telefone
        if email:
            self.email = email