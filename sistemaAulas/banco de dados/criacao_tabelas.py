import sqlite3

# Conectar ao banco de dados (ou criar um novo se não existir)
conn = sqlite3.connect('associacao_moradores.db')

# Criar um cursor para executar comandos SQL
cursor = conn.cursor()

# Executar comandos SQL para criar as tabelas
cursor.executescript('''
CREATE TABLE Endereco (
    ID_Endereco INTEGER PRIMARY KEY AUTOINCREMENT,
    Rua TEXT NOT NULL,
    Numero INTEGER NOT NULL,
    Cidade TEXT NOT NULL,
    Estado TEXT NOT NULL,
    CEP TEXT NOT NULL
);

CREATE TABLE Morador (
    CPF TEXT PRIMARY KEY,
    NomeCompleto TEXT NOT NULL,
    Filiacao TEXT,
    DataNascimento DATE NOT NULL,
    Endereco_ID INTEGER,
    Telefone TEXT,
    Email TEXT,
    FOREIGN KEY (Endereco_ID) REFERENCES Endereco(ID_Endereco)
);

CREATE TABLE Professor (
    CPF TEXT PRIMARY KEY,
    NomeCompleto TEXT NOT NULL,
    Especialidade TEXT NOT NULL,
    DataNascimento DATE NOT NULL,
    Endereco_ID INTEGER,
    Telefone TEXT,
    Email TEXT,
    FOREIGN KEY (Endereco_ID) REFERENCES Endereco(ID_Endereco)
);

CREATE TABLE Administrador (
    CPF TEXT PRIMARY KEY,
    NomeCompleto TEXT NOT NULL,
    DataNascimento DATE NOT NULL,
    Endereco_ID INTEGER,
    Telefone TEXT,
    Email TEXT,
    NomeUsuario TEXT NOT NULL,
    Senha TEXT NOT NULL,
    DataCadastro DATE NOT NULL,
    FOREIGN KEY (Endereco_ID) REFERENCES Endereco(ID_Endereco)
);

CREATE TABLE Aula (
    ID_Aula INTEGER PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Descricao TEXT,
    Professor_CPF TEXT,
    DiasSemana TEXT NOT NULL,
    HorarioInicio TIME NOT NULL,
    HorarioTermino TIME NOT NULL,
    Local TEXT NOT NULL,
    NumeroVagas INTEGER NOT NULL,
    FOREIGN KEY (Professor_CPF) REFERENCES Professor(CPF)
);

CREATE TABLE Inscricao (
    ID_Inscricao INTEGER PRIMARY KEY AUTOINCREMENT,
    Morador_CPF TEXT,
    Aula_ID INTEGER,
    DataInscricao DATE NOT NULL,
    StatusInscricao TEXT NOT NULL,
    FOREIGN KEY (Morador_CPF) REFERENCES Morador(CPF),
    FOREIGN KEY (Aula_ID) REFERENCES Aula(ID_Aula)
);
''')

# Confirmar as alterações e fechar a conexão
conn.commit()
conn.close()
