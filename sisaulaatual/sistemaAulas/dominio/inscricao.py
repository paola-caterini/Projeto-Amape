from datetime import datetime

class Inscricao:
    def __init__(self, morador_cpf, aula_codigo, status, matricula, data_inscricao=None):
        self.morador_cpf = morador_cpf
        self.aula_codigo = aula_codigo
        self.status = status
        self.matricula = matricula
        self.data_inscricao = data_inscricao if data_inscricao else datetime.now().strftime('%Y-%m-%d %H:%M:%S')