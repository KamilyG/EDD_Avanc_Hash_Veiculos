import os
from Veiculo import Veiculo
from HashTable import HashTable

hashtable = HashTable()

cadastrar = True
while cadastrar == True:
    print("#################### MENU ####################")
    print("1 - Inserir\n"
        "2 - Remover\n"
        "3 - Verificar por Placa\n"
        "4 - Ver todas as informações contidas na lista\n"
        "0 - Sair\n")
    print("Escolha o que você deseja fazer:")

    option = input()
    os.system("cls")

    #inserir
    if option == "1":
        print("Informe a placa: ")
        placa = input()
        print("Informe o ano: ")
        ano = input()
        print("Informe a marca e o modelo: ")
        marcamodelo = input()
        print("Informe a cor: ")
        cor = input()

        os.system("cls")

        veiculo = Veiculo(placa, ano, marcamodelo, cor)
        #adiciona no hash, placa é a key, string é o dado/informação que já vai formatado
        hashtable.__setitem__(veiculo.placa, veiculo.__str__())

    #remover
    elif option == "2":
        print("Informe a placa do veículo que deseja remover da lista: ")
        placa = input()
        hashtable.remove(placa)

    #ver por placa
    elif option == "3":
        print("Informe a placa do veículo que deseja ver: ")
        placa = input()
        #print placa e dados da placa
        print(hashtable.__getitem__(placa))

    #ver todas as placas e informações por placa
    elif option == "4":
        hashtable.tabledados()

    #sair
    elif option == "0":
        exit()

    #caso especial
    else:
        print("Entrada inválida!")
