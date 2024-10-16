#executar este script para cadastrar o primeiro administrador do sistema
#python scripts/cadastrar_primeiro_admin.py

from controladores.admin_controller import AdminController

def cadastrar_primeiro_admin():
    db_path = '/Users/user/Desktop/sistemaAulas/banco_de_dados.db'
    controller = AdminController(db_path)
    
    cpf = '12345678900'
    nome_completo = 'Primeiro Admin'
    data_nascimento = '1980-01-01'
    endereco = 'Rua Exemplo, 123'
    telefone = '123456789'
    email = 'admin@example.com'
    nome_usuario = 'admin'
    senha = 'senha123'
    
    controller.adicionar_admin(cpf, nome_completo, data_nascimento, endereco, telefone, email, nome_usuario, senha)
    print("Primeiro administrador cadastrado com sucesso!")

if __name__ == '__main__':
    cadastrar_primeiro_admin()

