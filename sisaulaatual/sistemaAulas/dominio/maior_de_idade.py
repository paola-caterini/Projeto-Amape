# dominio/maior_de_idade.py
from dominio.morador import Morador

class MaiorDeIdade(Morador):
    def __init__(self, matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, profissao):
        super().__init__(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email)
        self.matricula = matricula
        self.profissao = profissao

    def atualizar(self, nome_completo=None, filiacao=None, data_nascimento=None, endereco=None, telefone=None, email=None, profissao=None):
        super().atualizar(nome_completo, filiacao, data_nascimento, endereco, telefone, email)
        if profissao:
            self.profissao = profissao