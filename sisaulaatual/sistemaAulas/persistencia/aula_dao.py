# persistencia/aula_dao.py
import sqlite3
from dominio.aula import Aula

class AulaDAO:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS aulas (
                                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                                    nome TEXT NOT NULL,
                                    descricao TEXT,
                                    professor_responsavel TEXT,
                                    dias_semana TEXT,
                                    horario_inicio TEXT,
                                    horario_termino TEXT,
                                    local TEXT,
                                    numero_vagas INTEGER)''')

    def adicionar_aula(self, aula):
        with self.conn:
            self.conn.execute('INSERT INTO aulas (nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas) VALUES (?, ?, ?, ?, ?, ?, ?, ?)',
                              (aula.nome, aula.descricao, aula.professor_responsavel, aula.dias_semana, aula.horario_inicio, aula.horario_termino, aula.local, aula.numero_vagas))

    def atualizar_aula(self, aula):
        with self.conn:
            self.conn.execute('UPDATE aulas SET nome = ?, descricao = ?, professor_responsavel = ?, dias_semana = ?, horario_inicio = ?, horario_termino = ?, local = ?, numero_vagas = ? WHERE id = ?',
                              (aula.nome, aula.descricao, aula.professor_responsavel, aula.dias_semana, aula.horario_inicio, aula.horario_termino, aula.local, aula.numero_vagas, aula.id))

    def remover_aula(self, aula_id):
        with self.conn:
            self.conn.execute('DELETE FROM aulas WHERE id = ?', (aula_id,))

    def listar_aulas(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas FROM aulas')
        aulas = cursor.fetchall()
        return [Aula(id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas) for id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas in aulas]