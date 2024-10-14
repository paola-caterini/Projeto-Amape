import sqlite3

def criar_banco_de_dados(db_path):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        
        # Criar tabela de administradores
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
        
        # Criar tabela de professores
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
        
        # Criar tabela de moradores
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS moradores (
                cpf TEXT PRIMARY KEY,
                nome_completo TEXT,
                data_nascimento TEXT,
                endereco TEXT,
                telefone TEXT,
                email TEXT,
                data_cadastro TEXT
            )
        ''')
        
        # Criar tabela de aulas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS aulas (
                codigo TEXT PRIMARY KEY,
                nome TEXT,
                descricao TEXT,
                data TEXT,
                horario TEXT,
                professor_cpf TEXT,
                FOREIGN KEY(professor_cpf) REFERENCES professores(cpf)
            )
        ''')
        
        # Criar tabela de inscrições
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inscricoes (
                morador_cpf TEXT,
                aula_codigo TEXT,
                PRIMARY KEY(morador_cpf, aula_codigo),
                FOREIGN KEY(morador_cpf) REFERENCES moradores(cpf),
                FOREIGN KEY(aula_codigo) REFERENCES aulas(codigo)
            )
        ''')
        
        conn.commit()

# Caminho para o banco de dados
db_path = 'sistema_aulas.db'
criar_banco_de_dados(db_path)