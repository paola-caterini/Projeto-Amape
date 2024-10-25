# dominio/portador_de_necessidades_especiais.py
from sistemaAulas.dominio.morador import Morador

class PortadorDeNecessidadesEspeciais(Morador):
    def __init__(self, matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo_necessidade, grau_necessidade):
        super().__init__(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email)
        self.matricula = matricula
        self.tipo_necessidade = tipo_necessidade
        self.grau_necessidade = grau_necessidade

    def atualizar(self, nome_completo=None, filiacao=None, data_nascimento=None, endereco=None, telefone=None, email=None, tipo_necessidade=None):
        super().atualizar(nome_completo, filiacao, data_nascimento, endereco, telefone, email)
        if tipo_necessidade:
            self.tipo_necessidade = tipo_necessidade