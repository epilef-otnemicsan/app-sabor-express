import os
restaurantes = [{"nome":"Outback Steakhouse", "categoria":"Carnes", "ativo":True}, 
                {"nome":"Pizza & Beer 7055", "categoria":"Pizzas", "ativo":False}, 
                {"nome":"Fogo de Chão", "categoria":"Carnes", "ativo":False},
                {"nome":"Taverna Medieval", "categoria":"Hamburgueria", "ativo":False}]

def menu_principal():
    print("|| ----- [App Sabor Express] ----- ||\n")
    print("1) Cadastrar restaurante")
    print("2) Listar restaurante")
    print("3) Alterar status do restaurante")
    print("4) Sair")

def selecionar_opcoes():
    """
    Função que serve para selecionar as opções do menu principal.

    Input: opcao_escolhida

    Utilizando o 'try' e 'except' para tratar possíveis erros do usuário e utilizando o if para chamar as funções dependendo da opção escolhida pelo usuário
    """
    try:
        opcao_escolhida = int(input("Escolha uma opção: "))

        if opcao_escolhida == 1:
            cadastrar_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            alterar_status()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def finalizar_app():
    limpar_tela()
    print("Encerrando o programa...")

def opcao_invalida():
    print("Opção inválida!")
    voltar_ao_menu_principal()

def cadastrar_restaurante():
    """
    Função que serve para cadastrar um restaurante.

    Input: Nome do restaurante, Categoria

    Output: Adiciona dados do restaurante ao dicionario "restaurantes"
    """
    limpar_tela()
    print("---  Cadastro de restaurantes  ---")
    nome_do_restaurante = input("Digite o nome do restaurante: ")
    categoria = input(f"Digite o nome da categoria do restaurante [{nome_do_restaurante}]: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante [{nome_do_restaurante}] foi cadastrado com sucesso!\n")
    voltar_ao_menu_principal()

def listar_restaurantes():
    """
    Função que serve para listar os restaurantes do dicionario.

    Uso do laço de repetição 'for' e as funções nome_restaurante, categoria e ativo para mostrar os dados do restaurante na tela 
    """
    limpar_tela()
    print("Listando os restaurantes abaixo: \n")
    print(f"{'Nome do restaurante'.ljust(23)} | {'Categoria'.ljust(20)} | Status do restaurante")
    print("-" * 70)
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "Ativado" if restaurante["ativo"] else "Desativado"
        print(f" - {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")

    voltar_ao_menu_principal()

def limpar_tela():
    os.system("cls")

def voltar_ao_menu_principal():
    input("\nDigite qualquer tecla para voltar ao menu principal: ")
    main()

def alterar_status():
    """
    Função que serve para alterar o status do restaurante.

    Input: nome_restaurante

    Utiliza o laço de repetição for para percorrer o dicionario e o if para localizar o nome do restaurante dentro do dicionario, caso o retaurante esteja ativo, o status é mudado para inativo, seguindo a mesma lógica caso o status do restaurante seja inativo
    """
    limpar_tela()
    print("Alterando status do restaurante")
    nome_restaurante = input("Digite o nome do restaurante que deseja alterar o status: ")
    restaurante_encontrado = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante["nome"]:
            restaurante_encontrado = True
            restaurante["ativo"] = not restaurante["ativo"]
            mensagem = f"O restaurante {nome_restaurante} foi ativado com sucesso" if restaurante["ativo"] else f"O restaurante {nome_restaurante} foi desativado com sucesso"
            print(mensagem)
    if not restaurante_encontrado:
        print("O restaurante não foi encontrado")
    voltar_ao_menu_principal()


##   ------------------   ##   --------------------  FUNÇÕES  ----------------------  ##  ------------------  ##
    
def main():
    limpar_tela()
    menu_principal()
    selecionar_opcoes()


if __name__ == "__main__":
    main()
