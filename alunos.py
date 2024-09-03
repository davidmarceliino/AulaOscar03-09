sala = {}
def cadastro_aluno():
    rm = input("Digite o registro de matricula do aluno : ")
    nome = input("Digite o nome do aluno : ")
    nascimento = input("Digite o nascimento do aluno : ")
    emailAluno = input("Digite o EMAIL do aluno : ")
    fone = float(input("Digite o telefone do aluno"))
    end = input("Digite o endereço do aluno: ")
    sala[rm] = {"nome": nome, "data nascimento": nascimento, "Email": emailAluno, "Contato": fone, "Endereço Aluno": end}
    print("Aluno cadastrado com sucesso")
    
def altera_end():
    novo_end = float(input("Digite o novo endereço: "))
    rm = input("Entre com o registro de matricula: ")
    if(rm in sala):
        sala[rm]['Preço'] = novo_end
        print("preço alterado!")
        
def  pesquisar_aluno():
    rm = input("Digite o registro de matricula do aluno : ")
    alunoCerto = sala.get(rm)
    if alunoCerto:
        print("Aluno localizado")
        print(alunoCerto)
        
def listar_alunos():
    print(sala)
    
    
while(True):
    print("\nMenu: ")
    print("1 - Adicionar aluno")
    print("2 - Alterar endereço aluno")
    print("3 - Pesquisar por Resgitro de Matricula")
    print("4 - Lista chamada")
    print("5 - sair")
    print("-------------------------")
    opcao = int(input("Escolha uma opção: "))
    if(opcao == 1):
        cadastro_aluno()
    elif(opcao == 2):
        altera_end()
    elif(opcao == 3):
        pesquisar_aluno()
    elif(opcao == 4):
        listar_alunos()     
    elif(opcao == 5):
        break
    else:
        print("Escolha a opção correta")
    
    