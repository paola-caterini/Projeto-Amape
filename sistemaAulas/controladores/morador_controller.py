# controladores/morador_controller.py
from persistencia.morador_dao import MoradorDAO
from dominio.morador import Morador
from dominio.menor_de_idade import MenorDeIdade
from dominio.maior_de_idade import MaiorDeIdade
from dominio.portador_de_necessidades_especiais import PortadorDeNecessidadesEspeciais

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