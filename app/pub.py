
from classes import Publicação


def Pub(x):
    escolha = 99
    Tpub = []
    titulo1 = 'Cappuccino'
    tema1 = 'Bebidas'
    texto1 = 'Coloque em uma xícara:\n - 2 colheres de sopa de café solúvel,\n  - 3 colheres de sopa de chocolate em pó,\n  - 1 colher de chá de canela em pó\n  - e 500ml de leite quente\n  Misture tudo até ficar uniforme'

    Pub1 = Publicação(titulo1,texto1, tema1,)

    titulo2 = 'Torresmo de boteco'
    tema2 = 'Petiscos'
    texto2 = 'Ingrediente principal: Barriga de porco\n Primeiro passo: Corte a barriga em tiras e salgue-a por completo\n Segundo passo: Em uma panela funda, coloque as tiras\n Terceiro passo: Deixe fritar em fogo baixo mexendo a cada 10 minutos\n Quarto passo: Deixe fritar até dourar por completo\n Quinto passo: Deixe descansar por 5 minutos e sirva-se'

    Pub2 = Publicação(titulo2,texto2, tema2,)

    Pub1.alterarTema(tema1)
    Pub1.alterarTitulo(titulo1)
    Pub1.alterarTexto(texto1)
    Pub2.alterarTema(tema2)
    Pub2.alterarTitulo(titulo2)
    Pub2.alterarTexto(texto2)
    print(Tpub)
            
    Tpub.append(vars(Pub1))
    Tpub.append(vars(Pub2))

    while escolha != 100:
        if x == 0:
            

            print(Tpub)
            print("Digite a ação a ser executada: \n","1 - Mostrar as Publicações: \n","2 - Fazer uma Publicação: \n 3 - Sair \n\n")
            escolha = int(input("Ação: "))
            if(escolha == 1):
                return Pub(0)
            
            elif(escolha == 2):
                return Npub()
            
            elif(escolha == 3):
                break
        else:
            
            Tpub.append(vars(x))
            print("Digite a ação a ser executada: \n","1 - Mostrar as Publicações: \n","2 - Fazer uma Publicação: \n 3 - Sair \n\n")
            escolha = int(input("Ação: "))
            if(escolha == 1):
                return Pub(0)
            
            elif(escolha == 2):
                return Npub()
            
            elif(escolha == 3):
                break
            
        

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
    Pub(NovaPub)
 
    print("Digite a ação a ser executada: \n","1 - Mostrar as Publicações: \n","2 - Fazer uma Publicação: \n 3 - Sair \n\n")
    escolha = int(input("Ação: "))

    while (escolha != 100):
        
        if(escolha == 1):
            return Pub(0)
            
        elif(escolha == 2):
            if NovaPub.titulo == 'any' and NovaPub.tema == 'any' and NovaPub.texto == 'any':
                return Npub()
            else:
                print('####################################################\nOlá! \n Voce so pode fazer uma publicação por dia!\n####################################################\n\n')
                print("Digite a ação a ser executada: \n","1 - Mostrar as Publicações: \n","2 - Fazer uma Publicação: \n 3 - Sair \n\n")
                escolha = int(input("Ação: "))
        elif(escolha == 3):
            break