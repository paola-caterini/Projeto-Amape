# dominio/maior_de_idade.py
from sistemaAulas.dominio.morador import Morador

class MaiorDeIdade(Morador):
    def __init__(self, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, profissao):
        super().__init__(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email)
        self.profissao = profissao

    def atualizar(self, nome_completo=None, filiacao=None, data_nascimento=None, endereco=None, telefone=None, email=None, profissao=None):
        super().atualizar(nome_completo, filiacao, data_nascimento, endereco, telefone, email)
        if profissao:
            self.profissao = profissao