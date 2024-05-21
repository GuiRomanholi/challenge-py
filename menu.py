print("Inicio do programa")

lista_usuario = []
lista_mecanico = []


def menu():
    return """
--------------------------------
    M E N U - P R I N C I P A L \n
    - (U)suario Cadastrar
    - (M)ecânico Cadastrar
    - (L)istar Usuarios Cadastrados
    - L(I)star Mecanicos Cadastrados
    - (Q)uem Somos
    - (H)elp
    - (C)hatBot
    - (S)air
--------------------------------
"""


def continuar():
    e = True
    while e == True:
        print("---------------------------------------------")
        print("Gostaria de voltar ao menu principal? (S/N)")
        voltar_usu = input().upper()[0]
        if voltar_usu == "S":
            e = False
            executando = True
        elif voltar_usu == "N":
            print("Até Breve!")
            e = False
            executando = False
        else:
            print("Por favor digite S para (Sim) ou N para (Não)!")
    return executando


def cadastro_usuario():
    print(frase,"Cadastrar Usuario!")
    nome = input("Informe seu nome: ")
    email = input("Informe o seu email: ")
    placa = input("Informe sua placa: ")
    print(f"Parábens {nome}, você e seu carro {placa} estão cadastrados no nosso sistema!")
    d_usu = {"nome": nome, "email": email, "placa": placa}
    return d_usu


def cadastro_mecanico():
    print(frase,"Cadastrar Mecânico!")
    nome_mec = input("Informe o nome do mecânico: ")
    email_mec = input("Informe o email do mecânico: ")
    salario_mec = float(input("Informe o sálario do mecânico: "))
    print(f"Bem vindo {nome_mec}, e seu sálario mensal será de R$ {salario_mec}")
    d_mec = {"nome": nome_mec, "email": email_mec, "salario": salario_mec}
    return d_mec


def quem_somos():
    print(frase,"Quem Somos!")
    print("Somos:\nGuilherme R\nIgor\nCristian\nE iremos mudar o mundo!!")


def help():
    print(frase,"Help!")
    print("Você está com dificuldades de acessar a página? (S/N) ")
    pergunta = input().upper()[0]
    if pergunta == "S":
        print("Tente atualizar a página ou ligue para nossos serviços humanos, tel: (11) 3687-3779")
        executando = continuar()
    elif pergunta == "N":
        executando = continuar()
    return executando


def menu_chat():
    return """
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


def continuar_problemas():
    e = True
    while e == True:
        print("-"*50)
        print("Gostaria de voltar ao menu de problemas? (S/N)")
        voltar = input().upper()
        if voltar == "N":
            executando_chat = False
            e = False
        elif voltar == "S":
            executando_chat = True
            e = False
        else:
            print("Por Favor digite (S) para Sim e (N) para não")
    return executando_chat


def p_superaquecimento():
    print("-----------------------------------------------")
    print("Se o carro estiver superaquecendo, pare imediatamente, desligue o motor e deixe esfriar.\nVerifique o nível do líquido de arrefecimento e procure por vazamentos.")
    print("--------------------------------------------------")
    return continuar_problemas()


def p_eletrico():
    print("-----------------------------------------------")
    print("Em caso de pane elétrica no carro, verifique os fusíveis e conexões elétricas.\nSe necessário, chame um eletricista automotivo qualificado para diagnosticar e corrigir o problema.")
    print("--------------------------------------------------")
    return continuar_problemas()


def p_bateria():
    print("-----------------------------------------------")
    print("Se a bateria do carro estiver ruim, tente dar uma carga com cabos auxiliares ou um carregador portátil.\nSe não resolver, substitua por uma nova ou chame um serviço de assistência para fazer isso.")
    print("--------------------------------------------------")
    return continuar_problemas()


def p_falt_compus():
    print("-----------------------------------------------")
    print("Se estiver sem combustível, pare o carro em local seguro.\nSe possível, peça ajuda para trazer combustível. Se não, chame um serviço de assistência para reabastecer ou providenciar uma solução.")
    print("--------------------------------------------------")
    return continuar_problemas()


def p_trepidando():
    print("-----------------------------------------------")
    print("Se o carro estiver trepidando, verifique as rodas quanto a danos ou desequilíbrio.\nSe necessário, ajuste a pressão dos pneus.\nSe o problema persistir, pode ser necessário verificar os freios ou a suspensão com um mecânico.")
    print("--------------------------------------------------")
    return continuar_problemas()


def p_pneu():
    print("-----------------------------------------------")
    print("Se tiver um pneu furado, estacione em local seguro.\nTroque o pneu utilizando o macaco e a chave de roda, ou chame um serviço de assistência para trocar o pneu por você.")
    print("--------------------------------------------------")
    return continuar_problemas()


def p_dentada():
    print("-----------------------------------------------")
    print("Se a correia dentada quebrar, pare o carro imediatamente para evitar danos ao motor.\nChame um serviço de reboque para levar o veículo a uma oficina mecânica para substituir a correia e verificar se há danos adicionais no motor.")
    print("--------------------------------------------------")
    return continuar_problemas()


def p_cambio():
    print("-----------------------------------------------")
    print("Se enfrentar problemas de câmbio, estacione com segurança.\nVerifique o nível de fluido de transmissão e procure sinais de vazamento.\nSe persistir, consulte um mecânico qualificado para diagnosticar e reparar o câmbio.")
    print("--------------------------------------------------")
    return continuar_problemas()


def sair():
    print("Até Breve!")
    return False


def invalido():
    print("Opção Inválida, digite um dos valores dentro dos () do Menu.")
    print("Aperte <ENTER> para continuar")
    input()


def funcao_menu_problemas():
    executando_chat = True
    while executando_chat:
        print(frase,"ChatBot!")
        # Segundo menu de chatbot criado
        print(menu_chat())
        problema = input("Por favor me informe o problema no seu carro: ").upper()
        if problema == "S":
            executando_chat = p_superaquecimento()
        elif problema == "E":
            executando_chat = p_eletrico()
        elif problema == "B":
            executando_chat = p_bateria()
        elif problema == "F":
            executando_chat = p_falt_compus()
        elif problema == "T":
            executando_chat = p_trepidando()
        elif problema == "P":
            executando_chat = p_pneu()
        elif problema == "D":
            executando_chat = p_dentada()
        elif problema == "C":
            executando_chat = p_cambio()
        elif problema == "V":
            break
        else:
            invalido()


def listar_usu(lista_usuario):
    indice = 0
    while indice < len(lista_usuario):
        print(lista_usuario[indice])
        print("-"*50)
        indice = indice + 1
    print("Aperte <ENTER> para continuar")
    input()


def listar_mec(lista_mecanico):
    indice = 0
    while indice < len(lista_mecanico):
        print(lista_mecanico[indice])
        print("-"*50)
        indice = indice + 1
    print("Aperte <ENTER> para continuar")
    input()


# Iniciando programa
executando = True
while executando:
    frase = "Bem-vindo ao "
    print(menu())
    # Criando o menu ultilizando laços e if e else
    opcao = input("Digite a letra entre () da opcão desejada: ").upper()[0]
    if opcao == "U":
        lista_usuario.append(cadastro_usuario())
        executando = continuar()
    elif opcao == "M":
        lista_mecanico.append(cadastro_mecanico())
        executando = continuar()
    elif opcao == "L":
        listar_usu(lista_usuario)
    elif opcao == "I":
        listar_mec(lista_mecanico)
    elif opcao == "Q":
        quem_somos()
        executando = continuar()
    elif opcao == "H":
            executando = help()
    elif opcao == "C":
        funcao_menu_problemas()
        executando = continuar()
    elif opcao == "S":
        executando = sair()
    else:
        invalido()
# Finalizando programa
print("Fim do Programa!")

