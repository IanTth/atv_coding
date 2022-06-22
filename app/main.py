from classes import Publicação
from log import Log
from pub import Pub, Npub



def Main():
    print("Digite a ação a ser executada: \n","1 - Mostrar as Publicações: \n","2 - Fazer Login: \n 3 - Sair \n\n")
    escolha = int(input("Ação: "))

    while (escolha != 100):
        
        if(escolha == 1):
            return Pub()
            
        elif(escolha == 2):
            return Log()

        elif(escolha == 3):
            break


print('####################################################\nBem Vindo a Receitas da Vovó\n####################################################\n')
Main()