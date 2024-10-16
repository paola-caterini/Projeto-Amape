import sqlite3
from dominio.professor import Professor

class ProfessorDAO:
    def __init__(self, db_path):
        self.db_path = db_path
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS professores (
                    cpf TEXT PRIMARY KEY,
                    nome_completo TEXT,
                    especialidade TEXT,
                    data_nascimento TEXT,
                    endereco TEXT,
                    telefone TEXT,
                    email TEXT,
                    data_cadastro TEXT
                )
            ''')
            conn.commit()

    def adicionar_professor(self, professor):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO professores (cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email, data_cadastro)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (professor.cpf, professor.nome_completo, professor.especialidade, professor.data_nascimento, professor.endereco, professor.telefone, professor.email, professor.data_cadastro))
            conn.commit()

    def atualizar_professor(self, professor):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE professores
                SET nome_completo = ?, especialidade = ?, data_nascimento = ?, endereco = ?, telefone = ?, email = ?
                WHERE cpf = ?
            ''', (professor.nome_completo, professor.especialidade, professor.data_nascimento, professor.endereco, professor.telefone, professor.email, professor.cpf))
            conn.commit()

    def remover_professor(self, cpf):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM professores WHERE cpf = ?', (cpf,))
            conn.commit()

    def listar_professores(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM professores')
            rows = cursor.fetchall()
            professores = []
            for row in rows:
                professor = Professor(*row)
                professores.append(professor)
            return professores

    def buscar_professor_por_cpf(self, cpf):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM professores WHERE cpf = ?', (cpf,))
            row = cursor.fetchone()
            if row:
                return Professor(*row)
            return None

    def buscar_professor_por_nome(self, nome_completo):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM professores WHERE LOWER(nome_completo) = LOWER(?)', (nome_completo,))
            rows = cursor.fetchall()
            professores = []
            for row in rows:
                professor = Professor(*row)
                professores.append(professor)
            return professores