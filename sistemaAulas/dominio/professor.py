# dominio/professor.py
class Professor:
    def __init__(self, cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email):
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.especialidade = especialidade
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email

    def atualizar(self, nome_completo=None, especialidade=None, data_nascimento=None, endereco=None, telefone=None, email=None):
        if nome_completo:
            self.nome_completo = nome_completo
        if especialidade:
            self.especialidade = especialidade
        if data_nascimento:
            self.data_nascimento = data_nascimento
        if endereco:
            self.endereco = endereco
        if telefone:
            self.telefone = telefone
        if email:
            self.email = email