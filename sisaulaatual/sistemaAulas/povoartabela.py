import sqlite3
from datetime import datetime

# Dados dos administradores
administradores = [
    ('12345678900', 'Admin1', '1980-01-01', 'Rua A, 123', '123456789', 'admin1@example.com', 'admin1', 'senha1'),
    ('09876543211', 'Admin2', '1985-02-02', 'Rua B, 456', '987654321', 'admin2@example.com', 'admin2', 'senha2')
]

# Caminho para o banco de dados
db_path = 'sistema_aulas.db'

def povoar_tabela_administradores(db_path, administradores):
    with sqlite3.connect(db_path) as conn:
        cursor = conn.cursor()
        # Adiciona a data de cadastro atual para cada administrador
        administradores_com_data = [(cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, datetime.now().strftime('%Y-%m-%d %H:%M:%S')) for (cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha) in administradores]
        
        cursor.executemany('''
            INSERT INTO administradores (cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha, data_cadastro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', administradores_com_data)
        
        conn.commit()

# Povoar a tabela administradores
povoar_tabela_administradores(db_path, administradores)