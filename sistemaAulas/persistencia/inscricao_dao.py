import sqlite3

class InscricaoDAO:
    def __init__(self, db_path):
        self.db_path = db_path
        self._criar_tabela()

    def _criar_tabela(self):
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS inscricoes (
                    morador_cpf TEXT,
                    aula_codigo TEXT,
                    PRIMARY KEY (morador_cpf, aula_codigo)
                )
            ''')
            conn.commit()

    def adicionar_inscricao(self, inscricao):
        from dominio.inscricao import Inscricao  # Importação local para evitar ciclo
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO inscricoes (morador_cpf, aula_codigo)
                VALUES (?, ?)
            ''', (inscricao.morador_cpf, inscricao.aula_codigo))
            conn.commit()

    def remover_inscricao(self, morador_cpf, aula_codigo):
        from dominio.inscricao import Inscricao  # Importação local para evitar ciclo
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM inscricoes
                WHERE morador_cpf = ? AND aula_codigo = ?
            ''', (morador_cpf, aula_codigo))
            conn.commit()

    def listar_inscricoes(self):
        from dominio.inscricao import Inscricao  # Importação local para evitar ciclo
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT morador_cpf, aula_codigo FROM inscricoes')
            rows = cursor.fetchall()
            inscricoes = [Inscricao(morador_cpf=row[0], aula_codigo=row[1]) for row in rows]
            return inscricoes