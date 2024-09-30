# dominio/aula.py
class Aula:
    def __init__(self, id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.professor_responsavel = professor_responsavel
        self.dias_semana = dias_semana
        self.horario_inicio = horario_inicio
        self.horario_termino = horario_termino
        self.local = local
        self.numero_vagas = numero_vagas

    def atualizar(self, nome=None, descricao=None, professor_responsavel=None, dias_semana=None, horario_inicio=None, horario_termino=None, local=None, numero_vagas=None):
        if nome:
            self.nome = nome
        if descricao:
            self.descricao = descricao
        if professor_responsavel:
            self.professor_responsavel = professor_responsavel
        if dias_semana:
            self.dias_semana = dias_semana
        if horario_inicio:
            self.horario_inicio = horario_inicio
        if horario_termino:
            self.horario_termino = horario_termino
        if local:
            self.local = local
        if numero_vagas:
            self.numero_vagas = numero_vagas