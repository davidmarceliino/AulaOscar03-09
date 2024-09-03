produtos = {}

while True:
    codigo = input("Digite o codigo do produto:")
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto"))
    quantidade = int(input("Digite a quantidade em estoque: "))
    produtos[codigo] = {'nome':nome, 'preço':preco, 'quantidade':quantidade}
    print("Produto adicionado com sucesso!")
    string_digitada = input("Deseja continuar? : ")
    if string_digitada.lower() == "não":
        print(produtos)
        print("Fim!")
        break
 
    