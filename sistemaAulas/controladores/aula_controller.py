# controladores/aula_controller.py
from sistemaAulas.dominio.aula import Aula
from sistemaAulas.persistencia.aula_dao import AulaDAO

class AulaController:
    def __init__(self, db_path):
        self.dao = AulaDAO(db_path)

    def adicionar_aula(self, id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas):
        aula = Aula(id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas)
        self.dao.adicionar_aula(aula)

    def atualizar_aula(self, id, nome=None, descricao=None, professor_responsavel=None, dias_semana=None, horario_inicio=None, horario_termino=None, local=None, numero_vagas=None):
        aula = self.dao.buscar_aula_por_id(id)
        if aula:
            aula.atualizar(nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas)
            self.dao.atualizar_aula(aula)

    def remover_aula(self, id):
        self.dao.remover_aula(id)

    def listar_aulas(self):
        return self.dao.listar_aulas()