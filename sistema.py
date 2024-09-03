produtos = {}
def cadastro_produto():
    codigo = input("Digite o codigo do produto:")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos[codigo] = {"nome": nome, "preço": preco, "quantidade": quantidade}
    print("Produto cadastrado com sucesso")
    
def altera_peco():
    novo_preco = float(input("Digite o novo preço: "))
    codigo = input("Entre com o codigo do produto: ")
    if(codigo in produtos):
        produtos[codigo]['Preço'] = novo_preco
        print("preço alterado!")
        
def  pesquisar_produto():
    codigop = input("digite o codigo do produto: ")
    produtoCerto = produtos.get(codigop)
    if produtoCerto:
        print("Produto localizado")
        print(produtoCerto)
    
while(True):
    print("\nMenu: ")
    print("1 - Adicione produto")
    print("2 - Alterar preço produto")
    print("3 - Pesquisar por codigo")
    print("4 - Sair")
    print("-------------------------")
    opcao = int(input("Escolha uma opção: "))
    if(opcao == 1):
        cadastro_produto()
    elif(opcao == 2):
        altera_peco()
    elif(opcao == 3):
         pesquisar_produto()
    elif(opcao == 4):
        break
    else:
        print("Escolha a opção correta")
    
    