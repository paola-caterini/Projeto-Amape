# controladores/inscricao_controller.py
from persistencia.inscricao_dao import InscricaoDAO

class InscricaoController:
    def __init__(self, db_path):
        self.dao = InscricaoDAO(db_path)

    def adicionar_inscricao(self, inscricao):
        self.dao.adicionar_inscricao(inscricao)

    def remover_inscricao(self, morador, aula):
        self.dao.remover_inscricao(morador.cpf, aula.id)