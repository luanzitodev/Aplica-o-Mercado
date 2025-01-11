import os
from tabulate import tabulate
#ate onde eu testei, tudo esta funcionando e bem estruturado, loops funcionando e tratamento de erro tambem, as funcoes de limpar tela estao todas em seus lugares


# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

inventario = []

# Função para salvar os dados no .txt
def salvar_inventario():
    with open("inventario.txt", "w") as arquivo:
        for produto in inventario:
            linha = f"{produto[0]},{produto[1]},{produto[2]},{produto[3]},{produto[4]}\n"
            arquivo.write(linha)

# Função para carregar os dados do .txt
def carregar_inventario():
    try:
        with open("inventario.txt", "r") as arquivo:
            for linha in arquivo:
                dados = linha.strip().split(",")
                produto = [int(dados[0]), dados[1], dados[2], int(dados[3]), float(dados[4])]
                inventario.append(produto)               
    except FileNotFoundError:
        pass

# adicionar produtos
def adicionar_produto():
    def obter_codigo():
        while True:
            try:
                print("Digite 'Menu' para retornar ao menu principal")
                codigo = input("Digite o código do produto: ")

                if codigo.lower() == "menu": #coloquei uma opcao de volta ao menu aq
                    return menu()  # 

                codigo = int(codigo) #tive q converter os codigos para int ou float depois que eu adicionei a opcao de voltar ao menu
                if codigo < 0:
                    print("Erro! Digite um número válido.")
                    continue

                for produto in inventario:
                    if produto[0] == codigo:
                        print(f"Erro! o código {codigo} já está cadastrado.") #coloquei isso para que ele pudesse verificar na lista se o codigo ja esta la, se tiver ele vai emitir esse erro ai, para nao termos codigos repitidos
                        break
                else:
                    return codigo
                    
            except ValueError:
                limpar_tela()
                print("Erro! Digite apenas números.")
                

    def obter_categoria():
        while True:
            categoria = input("Digite a categoria do produto: ").strip()
            if categoria.lower() == "menu":
                return menu()  # #coloquei uma opcao de volta ao menu aq

            if categoria.isalpha(): #na categoria eu vou manter o isalpha mesmo, apenas letras, nao tem necessidade de numeros
                return categoria
            else:
                print("Erro! Digite uma categoria válida (Apenas letras).")

    def obter_produto():
        while True:
            produto = input("Digite o nome do produto: ").strip()
            if produto.lower() == "menu": #coloquei uma opcao de volta ao menu aq
                return menu()

            if produto and all(c.isalnum() or c.isspace() or c == '-' for c in produto):
                return produto #retirei o isalpha pq em casos como coca-cola 2litros, o programa nao iria aceitar
            else:
                print("Erro! Digite um nome válido (Apenas letras).")

    def obter_quantidade():
        while True:
            try:
                quantidade = input("Digite a quantidade do produto: ")
                if quantidade.lower() == "menu": #coloquei uma opcao de volta ao menu aq
                    return menu()

                quantidade = int(quantidade)
                if quantidade < 0:
                    print("Erro! Digite um número válido.")
                else:
                    return quantidade
            except ValueError:
                print("Erro! Digite apenas números válidos.")

    def obter_preco():
        while True:
            try:
                preco = input("Digite o preço do produto: ")
                if preco.lower() == "menu": #coloquei uma opcao de volta ao menu aq
                    return menu()

                preco = float(preco)
                if preco < 0:
                    print("Erro! Digite um número válido.")
                else:
                    return preco
            except ValueError:
                print("Erro! Digite um número válido.")

    codigo = obter_codigo()
    categoria = obter_categoria()
    produto = obter_produto()
    quantidade = obter_quantidade()
    preco = obter_preco()

    inventario.append([codigo, categoria, produto, quantidade, preco])
    print('''Produto adicionado ao inventário com sucesso!''')
    salvar_inventario()
    input("\nPressione Enter para continuar...")

#excluir produtooo
def excluir_produto():
    try:
        print("Digite 'Menu' para retornar ao menu principal")
        codigo = input("Digite o código do produto que deseja excluir: ")

        if codigo.lower() == "menu":  # Verifica se o usuário digitou "menu"
            return menu()

        codigo = int(codigo)  # Converte para inteiro após verificar se não é "menu"

    except ValueError:
        limpar_tela()
        print("Erro! Digite um número válido.")
        return excluir_produto()

    for produto in inventario:
        if produto[0] == codigo:
            inventario.remove(produto)
            print("Produto excluído do inventário com sucesso!")
            input("\nPressione Enter para continuar...")
            salvar_inventario()
            return

    print("Produto não encontrado!")
    input("\nPressione Enter para continuar...")


# alterar produto
def alterar_produto():
    try:
        print("Digite 'Menu' para retornar ao menu principal")
        codigo = input("Digite o código do produto que deseja alterar: ")

        if codigo.lower() == "menu":  #coloquei uma opcao de volta ao menu aq
            return menu()

        codigo = int(codigo)  #coloquei uma opcao de volta ao menu aq

    except ValueError:
        print("Erro! Digite um número válido.")
        return alterar_produto()

    for produto in inventario:
        if produto[0] == codigo:
            novo_produto = input("Digite o novo nome do produto: ")
            if novo_produto.lower() == "menu":  #coloquei uma opcao de volta ao menu aq
                return menu()

            nova_categoria = input("Digite a nova categoria do produto: ")
            if nova_categoria.lower() == "menu":  #coloquei uma opcao de volta ao menu aq
                return menu()

            try:
                nova_quantidade = input("Digite a nova quantidade do produto: ")
                if nova_quantidade.lower() == "menu":  #coloquei uma opcao de volta ao menu aq
                    return menu()

                nova_quantidade = int(nova_quantidade)  # Converte para inteiro após a verificação

                novo_preco = input("Digite o novo preço do produto: ")
                if novo_preco.lower() == "menu":  #coloquei uma opcao de volta ao menu aq
                    return menu()

                novo_preco = float(novo_preco)  # Converte para float após a verificação

            except ValueError:
                print("Erro! Digite valores numéricos válidos.")
                return

            produto[2] = novo_produto
            produto[1] = nova_categoria
            produto[3] = nova_quantidade
            produto[4] = novo_preco
            print("Produto alterado com sucesso!")
            salvar_inventario()
            return

    print("Produto não encontrado!")
    continuar = input("Deseja procurar novamente? ")  #pra tentar novamente caso nao encontre o codigo, melhor do que voltar ao menu
    if continuar.lower() == "sim":
        return alterar_produto()

    elif continuar.lower() == "não":
        return menu()

    else:
        pass #


# relatorio geral dos produtos do inventario
def relatorio_geral():
    if inventario:
        headers = ["Código", "Categoria", "Produto", "Quantidade", "Preço", "Total"] #headers é para a tabela ficar bonita
        tabela = [[p[0], p[1], p[2], p[3], f"R${p[4]:.2f}", f"R${p[3] * p[4]:.2f}"] for p in inventario]  #eu coloquei uma f string aqui no p3 e p4 para que ele apareça o R$ na tabela
        print("\nRelatório Geral do Inventário:")
        print(tabulate(tabela, headers=headers, tablefmt="grid")) 
    else:
        print("\nNenhum produto cadastrado no inventário.")

    input("\nPressione Enter para continuar...")



# relatorio por categoria
def relatorio_categoria():
    print("Digite 'Menu' para retornar ao menu principal")
    categoria = input("Digite a categoria dos produtos que deseja ver: ").strip()

    if categoria.lower() == "menu":  #coloquei uma opcao de volta ao menu a
        return menu()
        
    produtos_filtrados = [p for p in inventario if p[1].lower() == categoria.lower()]
    if produtos_filtrados:
        headers = ["Código", "Categoria", "Produto", "Quantidade", "Preço", "Total"]
        tabela = [[p[0], p[1], p[2], p[3], f"R${p[4]:.2f}", f"R${p[3] * p[4]:.2f}"] for p in produtos_filtrados]
        print(f"\nRelatório da Categoria '{categoria}':")
        print(tabulate(tabela, headers=headers, tablefmt="grid"))
    else:
        print(f"\nNenhum produto encontrado na categoria '{categoria}'.")

    input("\nPressione Enter para continuar...")

# relatorio por preço
def relatorio_preco():
    try:
        print("Digite 'Menu' para retornar ao menu principal")
        preco = input("Digite o preço máximo dos produtos que deseja ver: ")  # Captura como string

        if preco.lower() == "menu":  # Verifica se o usuário deseja retornar ao menu
            return menu()

        preco = float(preco)  # Converte para float após verificar "menu"

        if preco < 0:
            print("Erro! O preço não pode ser negativo.")
            return relatorio_preco()

    except ValueError:
        print("Erro! Digite um valor numérico válido.")
        return relatorio_preco()

    produtos_filtrados = [p for p in inventario if p[4] <= preco]

    if produtos_filtrados:
        headers = ["Código", "Categoria", "Produto", "Quantidade", "Preço", "Total"]
        tabela = [[p[0], p[1], p[2], p[3], f"R${p[4]:.2f}", f"R${p[3] * p[4]:.2f}"] for p in produtos_filtrados] #para conseguir fazer o R$ aparecer eu so precisei modificar o p4 e p4 com f string
        print(f"\nRelatório de Produtos com Preço Até R$ {preco:.2f}:")
        print(tabulate(tabela, headers=headers, tablefmt="grid"))
    else:
        print(f"\nNenhum produto encontrado com preço até R$ {preco:.2f}.")

    input("\nPressione Enter para continuar...")
    #coloquei uma opcao de apertar o enter para continuar no final de cada input

#menu principal
def menu():
    while True:
        limpar_tela()
        print('''
███╗░░░███╗███╗░░░███╗██╗░░██╗███████╗  ░█████╗░████████╗░█████╗░░█████╗░░█████╗░██████╗░██╗░██████╗████████╗░█████╗░
████╗░████║████╗░████║██║░░██║╚════██║  ██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║██╔════╝╚══██╔══╝██╔══██╗
██╔████╔██║██╔████╔██║███████║░░███╔═╝  ███████║░░░██║░░░███████║██║░░╚═╝███████║██║░░██║██║╚█████╗░░░░██║░░░███████║
██║╚██╔╝██║██║╚██╔╝██║██╔══██║██╔══╝░░  ██╔══██║░░░██║░░░██╔══██║██║░░██╗██╔══██║██║░░██║██║░╚═══██╗░░░██║░░░██╔══██║
██║░╚═╝░██║██║░╚═╝░██║██║░░██║███████╗  ██║░░██║░░░██║░░░██║░░██║╚█████╔╝██║░░██║██████╔╝██║██████╔╝░░░██║░░░██║░░██║
╚═╝░░░░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░╚═╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝

Olá, seja bem-vindo ao menu do inventário:
1. Adicionar produto
2. Excluir produto
3. Alterar produto
4. Relatório geral
5. Relatório por categoria
6. Relatório por preço
7. Sair''')
        try:
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                adicionar_produto()
            elif opcao == 2:
                excluir_produto()
            elif opcao == 3:
                alterar_produto()
            elif opcao == 4:
                relatorio_geral()
            elif opcao == 5:
                relatorio_categoria()
            elif opcao == 6:
                relatorio_preco()
            elif opcao == 7:
                print("Saindo do inventário...")
                salvar_inventario() #chamei a funcao de salvar o inventario a cada modificacao que fizermos, assim nao preciamos se preocupar se algo foi salvo ou nao
                break
            else:
                print("Opção inválida. Tente novamente.")
        except ValueError:
            print("Entrada inválida, digite um número.")

#carregar inventario para carregar os dados antes de iniciar o menu
carregar_inventario()
menu()
#salvar inventario para salvar os dados depois de sair do menu