from dominio.admin import Admin
from persistencia.admin_dao import AdminDAO
from controladores.professor_controller import ProfessorController
from controladores.morador_controller import MoradorController
from controladores.aula_controller import AulaController
from controladores.inscricao_controller import InscricaoController

class AdminController:
    def __init__(self, db_path):
        self.dao = AdminDAO(db_path)
        self.professor_controller = ProfessorController(db_path)
        self.morador_controller = MoradorController(db_path)
        self.aula_controller = AulaController(db_path)
        self.inscricao_controller = InscricaoController(db_path)
        self.admin_autenticado = None

    def autenticar_admin(self, nome_usuario, senha):
        admins = self.dao.listar_admins()
        for admin in admins:
            if admin.nome_usuario == nome_usuario and admin.senha == senha:
                self.admin_autenticado = admin
                return True
        return False

    def verificar_autenticacao(self):
        return self.admin_autenticado is not None

    def encerrar_sessao(self):
        self.admin_autenticado = None

    # Métodos para delegar operações CRUD para controladores específicos
    def adicionar_professor(self, *args, **kwargs):
        if self.verificar_autenticacao():
            self.professor_controller.adicionar_professor(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    def atualizar_professor(self, *args, **kwargs):
        if self.verificar_autenticacao():
            self.professor_controller.atualizar_professor(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    def remover_professor(self, *args, **kwargs):
        if self.verificar_autenticacao():
            self.professor_controller.remover_professor(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    def listar_professores(self):
        if self.verificar_autenticacao():
            return self.professor_controller.listar_professores()
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    def buscar_professor_por_nome(self, *args, **kwargs):
        if self.verificar_autenticacao():
            return self.professor_controller.buscar_professor_por_nome(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    # Métodos para delegar operações CRUD para aulas
    def adicionar_aula(self, *args, **kwargs):
        if self.verificar_autenticacao():
            self.aula_controller.adicionar_aula(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    def atualizar_aula(self, *args, **kwargs):
        if self.verificar_autenticacao():
            self.aula_controller.atualizar_aula(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    def remover_aula(self, *args, **kwargs):
        if self.verificar_autenticacao():
            self.aula_controller.remover_aula(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    def listar_aulas(self):
        if self.verificar_autenticacao():
            return self.aula_controller.listar_aulas()
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    def buscar_aula_por_nome(self, *args, **kwargs):
        if self.verificar_autenticacao():
            return self.aula_controller.buscar_aula_por_nome(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    # Métodos para delegar operações CRUD para inscrições


    def adicionar_morador_e_inscricao(self, tipo, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, aula_codigo, status, **kwargs):
        if self.verificar_autenticacao():
            matricula = self.morador_controller.gerar_matricula()
            # Adicionar o morador
            self.morador_controller.adicionar_morador(
                tipo=tipo,
                cpf=cpf,
                nome_completo=nome_completo,
                filiacao=filiacao,
                data_nascimento=data_nascimento,
                endereco=endereco,
                telefone=telefone,
                email=email,
                matricula=matricula,
                **kwargs
            )
            # Adicionar a inscrição
            self.inscricao_controller.adicionar_inscricao(
                cpf=cpf,
                aula_codigo=aula_codigo,
                status=status,
                matricula=matricula
            )
            return nome_completo, matricula
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")
    def buscar_inscricao_por_morador(self, *args, **kwargs):
        if self.verificar_autenticacao():
            return self.inscricao_controller.buscar_inscricao_por_morador(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")

    def buscar_inscricao_por_aula(self, *args, **kwargs):
        if self.verificar_autenticacao():
            return self.inscricao_controller.buscar_inscricao_por_aula(*args, **kwargs)
        else:
            raise PermissionError("Acesso negado. Admin não autenticado.")