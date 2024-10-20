from sistemaAulas.dominio.inscricao import Inscricao
from sistemaAulas.persistencia.inscricao_dao import InscricaoDAO

class InscricaoController:
    def __init__(self, db_path):
        self.inscricao_dao = InscricaoDAO(db_path)

    def adicionar_inscricao(self, morador_cpf, aula_codigo, status, matricula, data_inscricao=None):
        inscricao = Inscricao( morador_cpf, aula_codigo, status,matricula, data_inscricao)
        self.inscricao_dao.adicionar_inscricao(inscricao)

    def remover_inscricao(self, matricula, morador_cpf, aula_codigo):
        self.inscricao_dao.remover_inscricao(matricula, morador_cpf, aula_codigo)

    def listar_inscricoes(self):
        return self.dao.listar_inscricoes()

    def buscar_inscricao_por_morador(self, morador_cpf):
        return self.dao.buscar_inscricao_por_morador(morador_cpf)

    def buscar_inscricao_por_aula(self, aula_codigo):
        return self.dao.buscar_inscricao_por_aula(aula_codigo)