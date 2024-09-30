# persistencia/professor_dao.py
import sqlite3
from dominio.professor import Professor

class ProfessorDAO:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS professores (
                                    cpf TEXT PRIMARY KEY,
                                    nome_completo TEXT NOT NULL,
                                    especialidade TEXT,
                                    data_nascimento TEXT,
                                    endereco TEXT,
                                    telefone TEXT,
                                    email TEXT)''')

    def adicionar_professor(self, professor):
        with self.conn:
            self.conn.execute('INSERT INTO professores (cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email) VALUES (?, ?, ?, ?, ?, ?, ?)',
                              (professor.cpf, professor.nome_completo, professor.especialidade, professor.data_nascimento, professor.endereco, professor.telefone, professor.email))

    def atualizar_professor(self, professor):
        with self.conn:
            self.conn.execute('UPDATE professores SET nome_completo = ?, especialidade = ?, data_nascimento = ?, endereco = ?, telefone = ?, email = ? WHERE cpf = ?',
                              (professor.nome_completo, professor.especialidade, professor.data_nascimento, professor.endereco, professor.telefone, professor.email, professor.cpf))

    def remover_professor(self, cpf):
        with self.conn:
            self.conn.execute('DELETE FROM professores WHERE cpf = ?', (cpf,))

    def listar_professores(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email FROM professores')
        professores = cursor.fetchall()
        return [Professor(cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email) for cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email in professores]