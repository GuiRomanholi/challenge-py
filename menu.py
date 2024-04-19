print("Inicio do programa")

executando = True
while executando:
    menu = """
    --------------------------------
    M E N U - P R I N C I P A L \n
    - Cadastrar (U)suario
    - Cadastrar (M)ecânico
    - (Q)uem Somos
    - (H)elp
    - (C)hatBot
    - (S)air
    --------------------------------
    """
    print(menu)
    opcao = input("Digite a letra entre () da opcão desejada: ").upper()
    frase = "Bem-vindo ao "
    if opcao == "U":
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
    elif opcao == "M":
        print(frase,"Cadastrar Mecânico!")
        nome_mec = input("Informe o nome do mecânico: ")
        email_mec = input("Informe o email do mecânico: ")
        salario_mec = float(input("Informe o sálario do mecânico: "))
        dic = {"nome": nome_mec, "email": email_mec, "salario": salario_mec}
        print(f"Bem vindo {nome_mec}, seu sálario mensal será de R$ {salario_mec}")
        print("---------------------------------------------")
        print("Gostaria de voltar ao menu? (S/N)")
        voltar = input().upper()
        if voltar == "N":
            print("Até Breve!")
            break
    elif opcao == "Q":
        print(frase,"Quem Somos!")
        print("Somos:\nGuilherme R\nIgor\nCristian\nE iremos mudar o mundo!!")
        print("---------------------------------------------")
        print("Gostaria de voltar ao menu? (S/N)")
        voltar = input().upper()
        if voltar == "N":
            print("Até Breve!")
            break
    elif opcao == "H":
        print(frase,"Help!")
        print("Você está com dificuldades de acessar a página? ")
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
    elif opcao == "C":
        print(frase,"ChatBot!")
        menu_chat ="""
        --------------------------------
        M E N U - D E - P R O B L E M A S \n
        - (S)uperaquecimento
        - Pane (E)létrica
        - (B)ateria
        - (F)alta de Combustível
        - Carro (T)repidando
        - (P)neus Furados
        - Correia (D)entada
        - Problemas no (C)âmbio
        --------------------------------
        """
        print(menu_chat)
        problema = input("Por favor me informe o problema no seu carro: ").upper()
        if problema == "S":
            print("É provável que o problema seja Superaquecimento")
        elif problema == "E":
            print("É provável que seja um problema Elétrico")
        elif problema == "B":
            print("É provável que o problema seja Bateria ruim")
        elif problema == "F":
            print("É provável que o problema seja Falta de Combustível")
        elif problema == "T":
            print("É provável que o problema seja Carro Trepidando")
        elif problema == "P":
            print("É provável que o problema seja Pneus Furados")
        elif problema == "D":
            print("É provável que o problema seja Correia Dentada")
        elif problema == "C":
            print("É provável que o problema seja Problemas no Câmbio")
        else:
            print("Valor inválido, por favor digitar o que está entre ().")

        print("---------------------------------------------")
        print("Gostaria de voltar ao menu? (S/N)")
        voltar = input().upper()
        if voltar == "N":
            print("Até Breve!")
            break
    elif opcao == "S":
        print("Até Breve!")
        executando = False
    else:
        print("Opção Inválida, digite um dos números do Menu.")


print("Fim do Programa!")

