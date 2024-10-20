# persistencia/aula_dao.py
import sqlite3
from dominio.aula import Aula

class AulaDAO:
    def __init__(self, db_path):
        self.db_path = db_path
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS aulas (
                    id TEXT PRIMARY KEY,
                    nome TEXT NOT NULL,
                    descricao TEXT,
                    professor_responsavel TEXT,
                    dias_semana TEXT,
                    horario_inicio TEXT,
                    horario_termino TEXT,
                    local TEXT,
                    numero_vagas INTEGER
                )
            ''')
            conn.commit()

    def adicionar_aula(self, aula):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO aulas (id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (aula.id, aula.nome, aula.descricao, aula.professor_responsavel, aula.dias_semana, aula.horario_inicio, aula.horario_termino, aula.local, aula.numero_vagas))
            conn.commit()

    def listar_aulas(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas FROM aulas')
            aulas = cursor.fetchall()
            return [Aula(id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas) for id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas in aulas]

    def remover_aula(self, id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM aulas WHERE id = ?', (id,))
            conn.commit()
    def buscar_aula_por_id(self, id):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT id, nome, descricao, professor_responsavel, dias_semana, horario_inicio, horario_termino, local, numero_vagas FROM aulas WHERE id = ?', (id,))
            result = cursor.fetchone()
            if result:
                return Aula(*result)
            return None

    def atualizar_aula(self, aula):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE aulas
                SET nome = ?, descricao = ?, professor_responsavel = ?, dias_semana = ?, horario_inicio = ?, horario_termino = ?, local = ?, numero_vagas = ?
                WHERE id = ?
            ''', (aula.nome, aula.descricao, aula.professor_responsavel, aula.dias_semana, aula.horario_inicio, aula.horario_termino, aula.local, aula.numero_vagas, aula.id))
            conn.commit()