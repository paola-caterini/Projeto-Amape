# dominio/admin.py
from dominio.inscricao import Inscricao
from dominio.aula import Aula
from dominio.morador import Morador
from datetime import datetime

class Admin:
    def __init__(self, cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro):
        self.cpf = cpf
        self.nome_completo = nome_completo
        self.data_nascimento = data_nascimento
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.nome_usuario = nome_usuario
        self.senha = senha
        self.data_cadastro = data_cadastro

    def atualizar(self, nome_completo=None, data_nascimento=None, endereco=None, telefone=None, email=None, nome_usuario=None, senha=None):
        if nome_completo:
            self.nome_completo = nome_completo
        if data_nascimento:
            self.data_nascimento = data_nascimento
        if endereco:
            self.endereco = endereco
        if telefone:
            self.telefone = telefone
        if email:
            self.email = email
        if nome_usuario:
            self.nome_usuario = nome_usuario
        if senha:
            self.senha = senha

    def emitir_relatorio_aulas(self, aula_controller):
        aulas = aula_controller.listar_aulas()
        relatorio = "\n".join([f"{aula.id}: {aula.nome}, {aula.descricao}, {aula.professor_responsavel}, {aula.dias_semana}, {aula.horario_inicio}-{aula.horario_termino}, {aula.local}, {aula.numero_vagas} vagas" for aula in aulas])
        return relatorio

    def emitir_relatorio_professores(self, professor_controller):
        professores = professor_controller.listar_professores()
        relatorio = "\n".join([f"{professor.cpf}: {professor.nome_completo}, {professor.especialidade}, {professor.data_nascimento}, {professor.endereco}, {professor.telefone}, {professor.email}" for professor in professores])
        return relatorio

    def matricular_morador(self, inscricao_controller, morador, aula):
        data_inscricao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        inscricao = Inscricao(morador, aula, data_inscricao, "confirmada")
        inscricao_controller.adicionar_inscricao(inscricao)

    def cancelar_matricula(self, inscricao_controller, morador, aula):
        inscricao_controller.remover_inscricao(morador, aula)