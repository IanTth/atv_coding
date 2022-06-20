publicacoes = []

class Publicação:
    def __init__(self,titulo, texto, tema, data_publicacao = 1, identificador = 00):
        self.identificador = identificador
        self.titulo = titulo
        self.texto = texto
        self.tema = tema
        self.data_publicacao = data_publicacao

    def alterarTitulo(self, novoTitulo):
        self.titulo = novoTitulo

    def alterarTexto(self, novoTexto):
        self.texto = novoTexto

    def alterarTema(self, novoTema):
        self.tema = novoTema

#-------------------------------------------------------------------------------------------------------------------------
#AÇÕES

print('####################################################\nBem Vindo a Receitas da Vovó\n####################################################\n')

print("Digite a ação a ser executada: \n","1- Fazer uma publicação: \n","2- Mostrar minhas publicações: \n","3- Sair: \n")
escolha = int(input("Ação: "))

while (escolha != 3):
    
    if(escolha == 1):

        #-------------------------------------------------------------------------------------------------------------------------
        #CRIAR UMA NOVA PUBLICAÇÃO
        titulo = 'any'
        tema = 'any'
        texto = 'any'

        NovaPub = Publicação(titulo,texto, tema,) 

        tema = str(input('Qual o tema?\n'))
        NovaPub.alterarTema(tema)

        titulo = str(input('Qual o titulo?\n'))
        NovaPub.alterarTitulo(titulo)

        texto = str(input('Qual o texto\n'))
        NovaPub.alterarTexto(texto)
        
        print("Digite a ação a ser executada: \n","1- Fazer uma publicação: \n","2- Mostrar minhas publicações: \n","3- Sair: \n")
        escolha = int(input("Ação: "))

    elif(escolha == 2):
        print(vars(NovaPub))

        print("Digite a ação a ser executada: \n","1- Fazer uma publicação: \n","2- Mostrar minhas publicações: \n","3- Sair: \n")
        escolha = int(input("Ação: "))

    else:
        break
