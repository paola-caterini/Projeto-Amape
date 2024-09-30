# persistencia/inscricao_dao.py
import sqlite3
from dominio.inscricao import Inscricao

class InscricaoDAO:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS inscricoes (
                                    morador_cpf TEXT,
                                    aula_id INTEGER,
                                    data_inscricao TEXT,
                                    status TEXT,
                                    PRIMARY KEY (morador_cpf, aula_id))''')

    def adicionar_inscricao(self, inscricao):
        with self.conn:
            self.conn.execute('INSERT INTO inscricoes (morador_cpf, aula_id, data_inscricao, status) VALUES (?, ?, ?, ?)',
                              (inscricao.morador.cpf, inscricao.aula.id, inscricao.data_inscricao, inscricao.status))

    def remover_inscricao(self, morador_cpf, aula_id):
        with self.conn:
            self.conn.execute('DELETE FROM inscricoes WHERE morador_cpf = ? AND aula_id = ?', (morador_cpf, aula_id))