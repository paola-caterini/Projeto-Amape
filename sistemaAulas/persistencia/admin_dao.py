# persistencia/admin_dao.py
import sqlite3
from dominio.admin import Admin

class AdminDAO:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        with self.conn:
            self.conn.execute('''CREATE TABLE IF NOT EXISTS admins (
                                    cpf TEXT PRIMARY KEY,
                                    nome_completo TEXT NOT NULL,
                                    data_nascimento TEXT,
                                    endereco TEXT,
                                    telefone TEXT,
                                    email TEXT,
                                    nome_usuario TEXT,
                                    senha TEXT,
                                    data_cadastro TEXT)''')

    def adicionar_admin(self, admin):
        with self.conn:
            self.conn.execute('INSERT INTO admins (cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
                              (admin.cpf, admin.nome_completo, admin.data_nascimento, admin.endereco, admin.telefone, admin.email, admin.nome_usuario, admin.senha, admin.data_cadastro))

    def atualizar_admin(self, admin):
        with self.conn:
            self.conn.execute('UPDATE admins SET nome_completo = ?, data_nascimento = ?, endereco = ?, telefone = ?, email = ?, nome_usuario = ?, senha = ?, data_cadastro = ? WHERE cpf = ?',
                              (admin.nome_completo, admin.data_nascimento, admin.endereco, admin.telefone, admin.email, admin.nome_usuario, admin.senha, admin.data_cadastro, admin.cpf))

    def remover_admin(self, cpf):
        with self.conn:
            self.conn.execute('DELETE FROM admins WHERE cpf = ?', (cpf,))

    def listar_admins(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro FROM admins')
        admins = cursor.fetchall()
        return [Admin(cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro) for cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro in admins]