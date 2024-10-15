# dominio/menor_de_idade.py
from sistemaAulas.dominio.morador import Morador

class MenorDeIdade(Morador):
    def __init__(self, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, responsavel_nome, responsavel_cpf, documento_permissao):
        super().__init__(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email)
        self.responsavel_nome = responsavel_nome
        self.responsavel_cpf = responsavel_cpf
        self.documento_permissao = documento_permissao

    def atualizar(self, nome_completo=None, filiacao=None, data_nascimento=None, endereco=None, telefone=None, email=None, responsavel_nome=None, responsavel_cpf=None, documento_permissao=None):
        super().atualizar(nome_completo, filiacao, data_nascimento, endereco, telefone, email)
        if responsavel_nome:
            self.responsavel_nome = responsavel_nome
        if responsavel_cpf:
            self.responsavel_cpf = responsavel_cpf
        if documento_permissao:
            self.documento_permissao = documento_permissao