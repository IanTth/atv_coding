
from classes import Publicação
from ação import Ação

def Pub():
    print("s")


def Npub():
    
    titulo = 'any'
    tema = 'any'
    texto = 'any'

    NovaPub = Publicação(titulo,texto, tema,)

    tema = str(input('Qual o tema?\n'))
    NovaPub.alterarTema(tema)

    titulo = str(input('Qual o titulo?\n'))
    NovaPub.alterarTitulo(titulo)

    texto = str(input('Qual a receita?\n'))
    NovaPub.alterarTexto(texto)
            
    print("Digite a ação a ser executada: \n","1 - Mostrar as Publicações: \n","2 - Fazer uma Publicação: \n 3 - Sair \n\n")
    escolha = int(input("Ação: "))

    while (escolha != 100):
        
        if(escolha == 1):
            return Pub()
            
        elif(escolha == 2):
            if NovaPub.titulo == 'any' and NovaPub.tema == 'any' and NovaPub.texto == 'any':
                return Npub()
            else:
                print('####################################################\nOlá! \n Voce so pode fazer uma publicação por dia!\n####################################################\n\n')
                return Ação()
        elif(escolha == 3):
            break