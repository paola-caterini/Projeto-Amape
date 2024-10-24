import sqlite3
from datetime import datetime

class InscricaoDAO:
    def __init__(self, db_path):
        self.db_path = db_path
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS inscricoes (
                    matricula TEXT,
                    morador_cpf TEXT,
                    aula_codigo TEXT,
                    status TEXT,
                    data_inscricao TEXT,
                    PRIMARY KEY (matricula, morador_cpf, aula_codigo)
                )
            ''')
            conn.commit()

    def adicionar_inscricao(self, inscricao):
        from dominio.inscricao import Inscricao  # Importação local para evitar ciclo
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO inscricoes ( morador_cpf, aula_codigo, status, matricula, data_inscricao)
                VALUES (?, ?, ?, ?, ?)
            ''', ( inscricao.morador_cpf, inscricao.aula_codigo, inscricao.status, inscricao.matricula, inscricao.data_inscricao))
            conn.commit()

    def remover_inscricao(self, matricula, morador_cpf, aula_codigo):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM inscricoes
                WHERE matricula = ? AND morador_cpf = ? AND aula_codigo = ?
            ''', (matricula, morador_cpf, aula_codigo))
            conn.commit()

    def listar_inscricoes(self):
        from dominio.inscricao import Inscricao  # Importação local para evitar ciclo
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                SELECT morador_cpf, matricula, aula_codigo, status, data_inscricao
                FROM inscricoes
            ''')
            inscricoes = cursor.fetchall()
            return [Inscricao(morador_cpf, matricula, aula_codigo, status, data_inscricao) for morador_cpf, matricula, aula_codigo, status, data_inscricao in inscricoes]