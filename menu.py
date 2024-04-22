print("Inicio do programa")
# Iniciando programa
executando = True
while executando:
    menu = """
    --------------------------------
    M E N U - P R I N C I P A L \n
    - (U)suario Cadastrar
    - (M)ecânico Cadastrar
    - (Q)uem Somos
    - (H)elp
    - (C)hatBot
    - (S)air
    --------------------------------
    """
    # Criando o menu ultilizando laços e if e else
    print(menu)
    opcao = input("Digite a letra entre () da opcão desejada: ").upper()[0]
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
        voltar_usu = input().upper()[0]
        if voltar_usu == "N":
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
        voltar_mec = input().upper()[0]
        if voltar_mec == "N":
            print("Até Breve!")
            break
    elif opcao == "Q":
        print(frase,"Quem Somos!")
        print("Somos:\nGuilherme R\nIgor\nCristian\nE iremos mudar o mundo!!")
        print("---------------------------------------------")
        print("Gostaria de voltar ao menu? (S/N)")
        voltar_quem = input().upper()[0]
        if voltar_quem == "N":
            print("Até Breve!")
            break
    elif opcao == "H":
        print(frase,"Help!")
        print("Você está com dificuldades de acessar a página? ")
        pergunta = input().upper()[0]
        if pergunta == "S":
            print("Tente atualizar a página ou ligue para nossos serviços humanos, tel: (11) 3687-3779")
            print("Gostaria de voltar ao menu? (S/N)")
            voltar_help = input().upper()[0]
            if voltar_help == "N":
                print("Até Breve!")
                break
        else:
            print("---------------------------------------------")
            print("Gostaria de voltar ao menu? (S/N)")
            voltar_vol = input().upper()[0]
            if voltar_vol == "N":
                print("Até Breve!")
                break
    elif opcao == "C":
        executando_chat = True
        while executando_chat:
            print(frase,"ChatBot!")
            # Segundo menu de chatbot criado
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
            - (V)oltar
            --------------------------------
            """
            print(menu_chat)
            problema = input("Por favor me informe o problema no seu carro: ").upper()
            if problema == "S":
                print("-----------------------------------------------")
                print("Se o carro estiver superaquecendo, pare imediatamente, desligue o motor e deixe esfriar.\nVerifique o nível do líquido de arrefecimento e procure por vazamentos.")
                print("-----------------------------------------------")
                print("Gostaria de voltar ao menu de problemas? (S/N)")
                voltar = input().upper()
                if voltar == "N":
                    break
            elif problema == "E":
                print("-----------------------------------------------")
                print("Em caso de pane elétrica no carro, verifique os fusíveis e conexões elétricas.\nSe necessário, chame um eletricista automotivo qualificado para diagnosticar e corrigir o problema.")
                print("-----------------------------------------------")
                print("Gostaria de voltar ao menu de problemas? (S/N)")
                voltar = input().upper()
                if voltar == "N":
                    break
            elif problema == "B":
                print("-----------------------------------------------")
                print("Se a bateria do carro estiver ruim, tente dar uma carga com cabos auxiliares ou um carregador portátil.\nSe não resolver, substitua por uma nova ou chame um serviço de assistência para fazer isso.")
                print("-----------------------------------------------")
                print("Gostaria de voltar ao menu de problemas? (S/N)")
                voltar = input().upper()
                if voltar == "N":
                    break
            elif problema == "F":
                print("-----------------------------------------------")
                print("Se estiver sem combustível, pare o carro em local seguro.\nSe possível, peça ajuda para trazer combustível. Se não, chame um serviço de assistência para reabastecer ou providenciar uma solução.")
                print("-----------------------------------------------")
                print("Gostaria de voltar ao menu de problemas? (S/N)")
                voltar = input().upper()
                if voltar == "N":
                    break
            elif problema == "T":
                print("-----------------------------------------------")
                print("Se o carro estiver trepidando, verifique as rodas quanto a danos ou desequilíbrio.\nSe necessário, ajuste a pressão dos pneus.\nSe o problema persistir, pode ser necessário verificar os freios ou a suspensão com um mecânico.")
                print("-----------------------------------------------")
                print("Gostaria de voltar ao menu de problemas? (S/N)")
                voltar = input().upper()
                if voltar == "N":
                    break
            elif problema == "P":
                print("-----------------------------------------------")
                print("Se tiver um pneu furado, estacione em local seguro.\nTroque o pneu utilizando o macaco e a chave de roda, ou chame um serviço de assistência para trocar o pneu por você.")
                print("-----------------------------------------------")
                print("Gostaria de voltar ao menu de problemas? (S/N)")
                voltar = input().upper()
                if voltar == "N":
                    break
            elif problema == "D":
                print("-----------------------------------------------")
                print("Se a correia dentada quebrar, pare o carro imediatamente para evitar danos ao motor.\nChame um serviço de reboque para levar o veículo a uma oficina mecânica para substituir a correia e verificar se há danos adicionais no motor.")
                print("-----------------------------------------------")
                print("Gostaria de voltar ao menu de problemas? (S/N)")
                voltar = input().upper()
                if voltar == "N":
                    break
            elif problema == "C":
                print("-----------------------------------------------")
                print("Se enfrentar problemas de câmbio, estacione com segurança.\nVerifique o nível de fluido de transmissão e procure sinais de vazamento.\nSe persistir, consulte um mecânico qualificado para diagnosticar e reparar o câmbio.")
                print("-----------------------------------------------")
                print("Gostaria de voltar ao menu de problemas? (S/N)")
                voltar = input().upper()
                if voltar == "N":
                    break
            elif problema =="V":
                break
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
# Finalizando programa
print("Fim do Programa!")

