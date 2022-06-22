from pub import Pub, Npub

def Ação():
    ação = int(input('Digite o número da ação:\n 1 - Ver publicação \n 2 - Criar publicação \n 3 - Sair\n'))
    if (ação == 1):
        return Pub()
    elif (ação == 2):
        return Npub()
