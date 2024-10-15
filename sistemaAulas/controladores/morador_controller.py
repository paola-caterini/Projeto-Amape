# controladores/morador_controller.py
import uuid
from datetime import datetime
from persistencia.morador_dao import MoradorDAO
from dominio.morador import Morador
from dominio.menor_de_idade import MenorDeIdade
from dominio.maior_de_idade import MaiorDeIdade
from dominio.portador_de_necessidades_especiais import PortadorDeNecessidadesEspeciais
from dominio.inscricao import Inscricao

class MoradorController:
    def __init__(self, dao):
        self.dao = dao
    def gerar_matricula(self):
        return f"{uuid.uuid4().hex[:8]}-{datetime.now().strftime('%Y%m%d%H%M%S')}"
    
    def adicionar_morador(self, tipo, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, **kwargs):
        matricula = self.gerar_matricula()
        if tipo == 'MenorDeIdade':
            responsavel = kwargs.get('responsavel')
            escola = kwargs.get('escola')
            documento_permissao = kwargs.get('documento_permissao')
            morador = MenorDeIdade(matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, responsavel, escola, documento_permissao)
        elif tipo == 'MaiorDeIdade':
            profissao = kwargs.get('profissao')
            morador = MaiorDeIdade(matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, profissao)
        elif tipo == 'PortadorDeNecessidadesEspeciais':
            tipo_necessidade = kwargs.get('tipo_necessidade')
            grau_necessidade = kwargs.get('grau_necessidade')
            morador = PortadorDeNecessidadesEspeciais(matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo_necessidade, grau_necessidade)
        else:
            raise ValueError("Tipo de morador inválido.")
        
        self.dao.adicionar_morador(morador)
        return matricula

    def remover_morador(self, cpf):
        self.dao.remover_morador(cpf)

    def listar_moradores(self):
        return self.dao.listar_moradores()