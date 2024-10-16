from config import DB_PATH
#import shutil
#import os
from controladores.admin_controller import AdminController

def main():
    # Inicializar o controlador principal com o caminho do banco de dados
    admin_controller = AdminController(DB_PATH)

    # Solicitar nome de usuário e senha para autenticação
    nome_usuario = input("Digite o nome de usuário do admin: ")
    senha = input("Digite a senha do admin: ")

    # Debug: Verificar se os valores foram capturados corretamente
    print(f"Nome de usuário: {nome_usuario}")
    print(f"Senha: {senha}")

    # Autenticar um administrador
    if admin_controller.autenticar_admin(nome_usuario, senha):
        print("Admin autenticado com sucesso!")
    else:
        print("Falha na autenticação do admin.")
        return

    while True:
        # Menu de opções
        print("\nSelecione a operação que deseja testar:")
        print("1. Adicionar Professor")
        print("2. Fazer Inscrição do Aluno")
        print("3. Listar Professores")
        print("4. Listar Alunos (Moradores)")
        print("5. Adicionar Inscrição de Aluno")
        print("6. Remover Inscrição de Aluno")
        print("7. Listar Inscrições de Aluno")
        print("8. Sair")

        opcao = input("Digite o número da operação: ")

        if opcao == '1':
            cpf = input("Digite o CPF do professor: ")
            nome_completo = input("Digite o nome completo do professor: ")
            especialidade = input("Digite a especialidade do professor: ")
            data_nascimento = input("Digite a data de nascimento do professor (YYYY-MM-DD): ")
            endereco = input("Digite o endereço do professor: ")
            telefone = input("Digite o telefone do professor: ")
            email = input("Digite o email do professor: ")

            try:
                admin_controller.adicionar_professor(
                    cpf=cpf,
                    nome_completo=nome_completo,
                    especialidade=especialidade,
                    data_nascimento=data_nascimento,
                    endereco=endereco,
                    telefone=telefone,
                    email=email
                )
                print("Professor adicionado com sucesso!")
            except PermissionError as e:
                print(e)
#################################
        elif opcao == '2':
            tipo = input("Digite o tipo de morador (MenorDeIdade, MaiorDeIdade, PortadorDeNecessidadesEspeciais): ")
            cpf = input("Digite o CPF do morador: ")
            nome_completo = input("Digite o nome completo do morador: ")
            filiacao = input("Digite a filiação do morador: ")
            data_nascimento = input("Digite a data de nascimento do morador (YYYY-MM-DD): ")
            endereco = input("Digite o endereço do morador: ")
            telefone = input("Digite o telefone do morador: ")
            email = input("Digite o email do morador: ")
            aula_codigo = input("Digite o código da aula: ")
            status = input("Digite o status da inscrição: ")

            try:
                if tipo == 'MenorDeIdade':
                    responsavel = input("Digite o nome do responsável: ")
                    escola = input("Digite o nome da escola: ")
                    documento_permissao = input("Digite o caminho do documento de permissão (ex: /Users/seu_usuario/Documentos/nome_do_arquivo.pdf): ")
                    #caminho_arquivo = input("Digite o caminho do documento de permissão /caminho/para/seu/projeto/documentos_permissao/nome_do_arquivo.pdf: ")
                    
                    # Diretório onde os arquivos serão salvos
                    #diretorio_destino = "documentos_permissao"
                    #if not os.path.exists(diretorio_destino):
                        #os.makedirs(diretorio_destino)
                    
                    # Nome do arquivo no diretório de destino
                    #nome_arquivo = os.path.basename(caminho_arquivo)
                    #caminho_destino = os.path.join(diretorio_destino, nome_arquivo)
                    
                    # Copiar o arquivo para o diretório de destino
                    #shutil.copy(caminho_arquivo, caminho_destino)

                    nome, matricula = admin_controller.adicionar_morador_e_inscricao(
                        tipo=tipo,
                            cpf=cpf,
                            nome_completo=nome_completo,
                            filiacao=filiacao,
                            data_nascimento=data_nascimento,
                            endereco=endereco,
                            telefone=telefone,
                            email=email,
                            aula_codigo=aula_codigo,
                            status=status,
                            responsavel=responsavel,
                            escola=escola,
                            documento_permissao=documento_permissao
                        )
                elif tipo == 'MaiorDeIdade':
                    profissao = input("Digite a profissão: ")
                    nome, matricula=admin_controller.adicionar_morador_e_inscricao(
                        tipo=tipo,
                            cpf=cpf,
                            nome_completo=nome_completo,
                            filiacao=filiacao,
                            data_nascimento=data_nascimento,
                            endereco=endereco,
                            telefone=telefone,
                            email=email,
                            aula_codigo=aula_codigo,
                            status=status,
                            profissao=profissao
                        )
                elif tipo == 'PortadorDeNecessidadesEspeciais':
                    tipo_necessidade = input("Digite o tipo de necessidade especial: ")
                    grau_necessidade = input("Digite o grau de necessidade especial: ")
                    nome, matricula = admin_controller.adicionar_morador_e_inscricaoadmin_controller.adicionar_morador_e_inscricao(
                        tipo=tipo,
                            cpf=cpf,
                            nome_completo=nome_completo,
                            filiacao=filiacao,
                            data_nascimento=data_nascimento,
                            endereco=endereco,
                            telefone=telefone,
                            email=email,
                            aula_codigo=aula_codigo,
                            status=status,
                            tipo_necessidade=tipo_necessidade,
                            grau_necessidade=grau_necessidade
                        )
                else:
                    print("Tipo de morador inválido.")
                    continue

                print(f"Morador {nome_completo} e inscrição adicionados com sucesso! Matrícula: {matricula}")
            except PermissionError as e:
                print(f"Erro de permissão: {e}")
            except Exception as e:
                print(f"Erro ao adicionar morador: {e}")
###################################
        elif opcao == '3':
            try:
                professores = admin_controller.listar_professores()
                for professor in professores:
                    print(f"CPF: {professor.cpf}, Nome: {professor.nome_completo}, Especialidade: {professor.especialidade}")
            except PermissionError as e:
                print(e)

        elif opcao == '4':
            try:
                moradores = admin_controller.morador_controller.listar_moradores()
                for morador in moradores:
                    print(f"CPF: {morador.cpf}, Nome: {morador.nome_completo}")
            except PermissionError as e:
                print(e)

        elif opcao == '5':
            morador_cpf = input("Digite o CPF do aluno: ")
            aula_codigo = input("Digite o código da aula: ")

            try:
                admin_controller.adicionar_inscricao_aluno(
                    morador_cpf=morador_cpf,
                    aula_codigo=aula_codigo
                )
                print("Inscrição de aluno adicionada com sucesso!")
            except PermissionError as e:
                print(e)

        elif opcao == '6':
            morador_cpf = input("Digite o CPF do aluno: ")
            aula_codigo = input("Digite o código da aula: ")

            try:
                admin_controller.remover_inscricao_aluno(
                    morador_cpf=morador_cpf,
                    aula_codigo=aula_codigo
                )
                print("Inscrição de aluno removida com sucesso!")
            except PermissionError as e:
                print(e)

        elif opcao == '7':
            try:
                inscricoes = admin_controller.listar_inscricoes_aluno()
                for inscricao in inscricoes:
                    print(f"CPF do Aluno: {inscricao.morador_cpf}, Código da Aula: {inscricao.aula_codigo}")
            except PermissionError as e:
                print(e)

        elif opcao == '8':
            print("Saindo...")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()