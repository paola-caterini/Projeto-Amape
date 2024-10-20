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
                matricula TEXT PRIMARY KEY,
              cpf TEXT,
              nome_completo TEXT,
              filiacao TEXT,
              data_nascimento TEXT,
              endereco TEXT,
              telefone TEXT,
              email TEXT,
              tipo TEXT,
              responsavel_nome TEXT,
              responsavel_cpf TEXT,
              documento_permissao TEXT,
              profissao TEXT,
              tipo_necessidade TEXT,
              grau_necessidade TEXT
            )
        ''')
        
        # Criar tabela de aulas
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
        
        # Criar tabela de inscrições
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS inscricoes (
                
                morador_cpf TEXT,
                aula_codigo TEXT,
                status TEXT,
                matricula TEXT,       
                data_inscricao TEXT,
                PRIMARY KEY (matricula, morador_cpf, aula_codigo)
            )
        ''')
        
        conn.commit()

# Caminho para o banco de dados
db_path = 'sistema_aulas.db'
criar_banco_de_dados(db_path)