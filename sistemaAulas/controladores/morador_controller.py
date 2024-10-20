# controladores/morador_controller.py
import uuid
from datetime import datetime
from sistemaAulas.persistencia.morador_dao import MoradorDAO
from sistemaAulas.dominio.morador import Morador
from sistemaAulas.dominio.menor_de_idade import MenorDeIdade
from sistemaAulas.dominio.maior_de_idade import MaiorDeIdade
from sistemaAulas.dominio.portador_de_necessidades_especiais import PortadorDeNecessidadesEspeciais
from sistemaAulas.dominio.inscricao import Inscricao

class MoradorController:
    def __init__(self, db_path):
       # self.db_path = db_path
        self.dao = MoradorDAO(db_path)
    def gerar_matricula(self):
        return f"{uuid.uuid4().hex[:8]}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def adicionar_morador(self, tipo, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, matricula, **kwargs):
        if tipo == 'MenorDeIdade':
            morador = MenorDeIdade(
                matricula=matricula,
                cpf=cpf,
                nome_completo=nome_completo,
                filiacao=filiacao,
                data_nascimento=data_nascimento,
                endereco=endereco,
                telefone=telefone,
                email=email,
                responsavel_nome=kwargs.get('responsavel_nome'),
                responsavel_cpf=kwargs.get('responsavel_cpf'),
                documento_permissao=kwargs.get('documento_permissao')
            )
        elif tipo == 'MaiorDeIdade':
            morador = MaiorDeIdade(
                matricula=matricula,
                cpf=cpf,
                nome_completo=nome_completo,
                filiacao=filiacao,
                data_nascimento=data_nascimento,
                endereco=endereco,
                telefone=telefone,
                email=email,
                profissao=kwargs.get('profissao')
            )
        elif tipo == 'PortadorDeNecessidadesEspeciais':
            morador = PortadorDeNecessidadesEspeciais(
                matricula=matricula,
                cpf=cpf,
                nome_completo=nome_completo,
                filiacao=filiacao,
                data_nascimento=data_nascimento,
                endereco=endereco,
                telefone=telefone,
                email=email,
                tipo_necessidade=kwargs.get('tipo_necessidade'),
                grau_necessidade=kwargs.get('grau_necessidade')
            )
        else:
            raise ValueError("Tipo de morador inválido.")
        
        self.dao.adicionar_morador(morador)
        return matricula

    def remover_morador(self, cpf):
        self.dao.remover_morador(cpf)

    def listar_moradores(self):
        return self.dao.listar_moradores()