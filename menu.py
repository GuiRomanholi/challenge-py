print("Inicio do programa")

executando = True
while executando:
    menu = """
    --------------------------------
    M E N U - P R I N C I P A L \n
    1- Cadastrar Usuario
    2- Cadastrar Mecânico
    3- Quem Somos
    4- Help
    5- ChatBot
    6- Sair
    --------------------------------
    """
    print(menu)
    opcao = int(input("Digite o número da opcão desejada: "))
    frase = "Bem-vindo ao "
    if opcao == 1:
        dic ={}
        print(frase,"Cadastrar Usuario!")
        nome = input("Informe seu nome: ")
        email = input("Informe o seu email: ")
        placa = input("Informe sua placa: ")
        print(f"Parábens {nome}, você e seu carro {placa} estão cadastrados no nosso sistema!")
        dic = {"nome": nome, "email": email, "placa": placa}
        print("Arquivos:",dic)
        print("---------------------------------------------")
        print("Gostaria de voltar ao menu? (S/N)")
        voltar = input().upper()
        if voltar == "N":
            print("Até Breve!")
            break
    elif opcao == 2:
        print(frase,"Cadastrar Mecânico!")
        nome_mec = input("Informe o nome do mecânico: ")
        email_mec = input("Informe o email do mecânico: ")
        salario_mec = float(input("Informe o sálario do mecânico: "))
        dic = {"nome": nome_mec, "email": email_mec, "salario": salario_mec}
        print(f"Bem vindo {nome_mec}, seu sálario mensal será de {salario_mec}")
        print("---------------------------------------------")
        print("Gostaria de voltar ao menu? (S/N)")
        voltar = input().upper()
        if voltar == "N":
            print("Até Breve!")
            break
    elif opcao == 3:
        print(frase,"Quem Somos!")
        print("Somos:\nGuilherme R\nIgor\nCristia\nE iremos mudar o mundo!!")
        print("---------------------------------------------")
        print("Gostaria de voltar ao menu? (S/N)")
        voltar = input().upper()
        if voltar == "N":
            print("Até Breve!")
            break
    elif opcao == 4:
        print(frase,"Help!")
        print("Você está com dificuldades de acessar a página?")
        pergunta = input().upper()[0]
        if pergunta == "S":
            print("Tente atualizar a página ou ligue para nossos serviços humanos, tel: (11) 3687-3779")
            print("Gostaria de voltar ao menu? (S/N)")
            voltar = input().upper()
            if voltar == "N":
                print("Até Breve!")
                break
        else:
            print("---------------------------------------------")
            print("Gostaria de voltar ao menu? (S/N)")
            voltar = input().upper()
            if voltar == "N":
                print("Até Breve!")
                break
    elif opcao == 5:
        print(frase,"ChatBot!")
        print("---------------------------------------------")
        print("Gostaria de voltar ao menu? (S/N)")
        voltar = input().upper()
        if voltar == "N":
            print("Até Breve!")
            break
    elif opcao == 6:
        print("Até Breve!")
        executando = False
    else:
        print("Opção Inválida, digite um dos números do Menu.")


print("Fim do Programa!")

