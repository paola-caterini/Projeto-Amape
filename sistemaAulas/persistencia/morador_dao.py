# persistencia/morador_dao.py
import sqlite3
from dominio.morador import Morador
from dominio.menor_de_idade import MenorDeIdade
from dominio.maior_de_idade import MaiorDeIdade
from dominio.portador_de_necessidades_especiais import PortadorDeNecessidadesEspeciais

class MoradorDAO:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS moradores (
                                    cpf TEXT PRIMARY KEY,
                                    nome_completo TEXT NOT NULL,
                                    filiacao TEXT,
                                    data_nascimento TEXT,
                                    endereco TEXT,
                                    telefone TEXT,
                                    email TEXT,
                                    tipo TEXT,
                                    responsavel_nome TEXT,
                                    responsavel_cpf TEXT,
                                    documento_permissao TEXT,
                                    profissao TEXT,
                                    tipo_necessidade TEXT)''')

    def adicionar_morador(self, morador):
        with self.conn:
            if isinstance(morador, MenorDeIdade):
                self.conn.execute('INSERT INTO moradores (cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, responsavel_nome, responsavel_cpf, documento_permissao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                  (morador.cpf, morador.nome_completo, morador.filiacao, morador.data_nascimento, morador.endereco, morador.telefone, morador.email, 'MenorDeIdade', morador.responsavel_nome, morador.responsavel_cpf, morador.documento_permissao))
            elif isinstance(morador, MaiorDeIdade):
                self.conn.execute('INSERT INTO moradores (cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, profissao) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                  (morador.cpf, morador.nome_completo, morador.filiacao, morador.data_nascimento, morador.endereco, morador.telefone, morador.email, 'MaiorDeIdade', morador.profissao))
            elif isinstance(morador, PortadorDeNecessidadesEspeciais):
                self.conn.execute('INSERT INTO moradores (cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, tipo_necessidade) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                  (morador.cpf, morador.nome_completo, morador.filiacao, morador.data_nascimento, morador.endereco, morador.telefone, morador.email, 'PortadorDeNecessidadesEspeciais', morador.tipo_necessidade))
            else:
                self.conn.execute('INSERT INTO moradores (cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                                  (morador.cpf, morador.nome_completo, morador.filiacao, morador.data_nascimento, morador.endereco, morador.telefone, morador.email, 'Morador'))

    def remover_morador(self, cpf):
        with self.conn:
            self.conn.execute('DELETE FROM moradores WHERE cpf = ?', (cpf,))

    def listar_moradores(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, responsavel_nome, responsavel_cpf, documento_permissao, profissao, tipo_necessidade FROM moradores')
        moradores = cursor.fetchall()
        resultado = []
        for morador in moradores:
            cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, responsavel_nome, responsavel_cpf, documento_permissao, profissao, tipo_necessidade = morador
            if tipo == 'MenorDeIdade':
                resultado.append(MenorDeIdade(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, responsavel_nome, responsavel_cpf, documento_permissao))
            elif tipo == 'MaiorDeIdade':
                resultado.append(MaiorDeIdade(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, profissao))
            elif tipo == 'PortadorDeNecessidadesEspeciais':
                resultado.append(PortadorDeNecessidadesEspeciais(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo_necessidade))
            else:
                resultado.append(Morador(cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email))
        return resultado