from sistemaAulas.persistencia.aula_dao import AulaDAO
from sistemaAulas.dominio.aula import Aula

class AulaController:
    def __init__(self, db_path):
        self.dao = AulaDAO(db_path)

    def adicionar_aula(self, codigo, nome, descricao, data, horario, professor_cpf):
        aula = Aula(codigo, nome, descricao, data, horario, professor_cpf)
        self.dao.adicionar_aula(aula)

    def atualizar_aula(self, codigo, nome=None, descricao=None, data=None, horario=None, professor_cpf=None):
        aula = self.dao.buscar_aula_por_codigo(codigo)
        if aula:
            aula.atualizar(nome, descricao, data, horario, professor_cpf)
            self.dao.atualizar_aula(aula)

    def remover_aula(self, codigo):
        self.dao.remover_aula(codigo)

    def listar_aulas(self):
        return self.dao.listar_aulas()

    def buscar_aula_por_nome(self, nome):
        return self.dao.buscar_aula_por_nome(nome)