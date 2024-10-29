import sqlite3

morador=False
professor=True

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('/home/emerson/Área de trabalho/TK/sistema_aulas.db')
cursor = conn.cursor()


# Função para adicionar um morador
def adicionar_morador(matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, responsavel_nome, responsavel_cpf, documento_permissao, profissao, tipo_necessidade, grau_necessidade):
    cursor.execute('''INSERT INTO moradores (matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, responsavel_nome, responsavel_cpf, documento_permissao, profissao, tipo_necessidade, grau_necessidade)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', (matricula, cpf, nome_completo, filiacao, data_nascimento, endereco, telefone, email, tipo, responsavel_nome, responsavel_cpf, documento_permissao, profissao, tipo_necessidade, grau_necessidade))
    conn.commit()

# Exemplo de uso
if morador:    
    for i in range(100, 200):
        adicionar_morador(
            f'{i}', 
            f'123456789{i:02}', 
            f'Nome Completo {i}', 
            f'Filiacao {i}', 
            f'2000-01-{i % 30 + 1:02}', 
            f'Rua Tal, {i}', 
            f'12345678{i % 10}', 
            f'{i}@exemplo.com', 
            'Estudante', 
            f'Responsavel Nome {i}', 
            f'123456789{i:02}', 
            f'12345{i}', 
            'Profissao', 
            'Tipo Necessidade', 
            'Grau Necessidade'
        )




if professor:        
        # Função para adicionar um professor
        def adicionar_professor(cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email, data_cadastro):
            cursor.execute('''INSERT INTO professores (cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email, data_cadastro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', (cpf, nome_completo, especialidade, data_nascimento, endereco, telefone, email, data_cadastro))
            conn.commit()

        # Adicionar 100 exemplos de professores
        for i in range(100, 200):
            adicionar_professor(
                f'987654321{i:02}', 
                f'Professor Nome {i}', 
                f'Especialidade {i}', 
                f'1980-01-{i % 30 + 1:02}', 
                f'Avenida Tal, {i}', 
                f'87654321{i % 10}', 
                f'prof{i}@exemplo.com', 
                f'2023-10-{i % 30 + 1:02}'
            )






# Fechar a conexão
conn.close()