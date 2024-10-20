import sqlite3
from datetime import datetime
from dominio.admin import Admin

class AdminDAO:
    def __init__(self, db_path):
        self.db_path = db_path
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS administradores (
                    cpf TEXT PRIMARY KEY,
                    nome_completo TEXT,
                    data_nascimento TEXT,
                    endereco TEXT,
                    telefone TEXT,
                    email TEXT,
                    nome_usuario TEXT,
                    senha TEXT,
                    data_cadastro TEXT
                )
            ''')
            conn.commit()

    def adicionar_admin(self, admin):
        if not admin.data_cadastro:
            admin.data_cadastro = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO administradores (cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (admin.cpf, admin.nome_completo, admin.data_nascimento, admin.endereco, admin.telefone, admin.email, admin.nome_usuario, admin.senha, admin.data_cadastro))
            conn.commit()

    def listar_admins(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro FROM administradores')
            rows = cursor.fetchall()
            admins = [Admin(*row) for row in rows]
            return admins

    def buscar_admin_por_cpf(self, cpf):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro FROM administradores WHERE cpf = ?', (cpf,))
            row = cursor.fetchone()
            if row:
                return Admin(*row)
            return None

    def remover_admin(self, cpf):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('DELETE FROM administradores WHERE cpf = ?', (cpf,))
            conn.commit()