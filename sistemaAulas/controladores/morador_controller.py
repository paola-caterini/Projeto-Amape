# controladores/morador_controller.py
from sistemaAulas.persistencia.morador_dao import MoradorDAO
from sistemaAulas.dominio.morador import Morador
from sistemaAulas.dominio.menor_de_idade import MenorDeIdade
from sistemaAulas.dominio.maior_de_idade import MaiorDeIdade
from sistemaAulas.dominio.portador_de_necessidades_especiais import PortadorDeNecessidadesEspeciais

class MoradorController:
    def __init__(self, db_path):
        self.dao = MoradorDAO(db_path)

    def adicionar_morador(self, tipo, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, extra1=None, extra2=None):
        if tipo == 'MenorDeIdade':
            morador = MenorDeIdade(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, extra1, extra2, extra1)
        elif tipo == 'MaiorDeIdade':
            morador = MaiorDeIdade(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, extra1)
        elif tipo == 'PortadorDeNecessidadesEspeciais':
            morador = PortadorDeNecessidadesEspeciais(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, extra1, extra2)
        else:
            morador = Morador(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email)
        self.dao.adicionar_morador(morador)

    def remover_morador(self, cpf):
        self.dao.remover_morador(cpf)

    def listar_moradores(self):
        return self.dao.listar_moradores()