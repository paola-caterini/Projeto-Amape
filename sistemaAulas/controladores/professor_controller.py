from sistemaAulas.persistencia.professor_dao import ProfessorDAO
from sistemaAulas.dominio.professor import Professor

class ProfessorController:
    def __init__(self, db_path):
        self.dao = ProfessorDAO(db_path)

    def adicionar_professor(self, cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email):
        professor = Professor(cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email)
        self.dao.adicionar_professor(professor)

    def atualizar_professor(self, cpf, nome_completo=None, especialidade=None, data_nascimento=None, endereco=None, telefone=None, email=None):
        professor = self.dao.buscar_professor_por_cpf(cpf)
        if professor:
            professor.atualizar(nome_completo, especialidade, data_nascimento, endereco, telefone, email)
            self.dao.atualizar_professor(professor)

    def remover_professor(self, cpf):
        self.dao.remover_professor(cpf)

    def listar_professores(self):
        return self.dao.listar_professores()

    def buscar_professor_por_nome(self, nome_completo):
        return self.dao.buscar_professor_por_nome(nome_completo)