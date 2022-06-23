from classes import Login
from pub import Npub, Pub


#LOGIN --------------


##Autenticador##
##Ajustar login sem cadastro##

  
  

#-------------------------------------------------------------------------------------------------------------------------
#AÇÕES

def Log():
  
  cpf = 0
  senha = 0
  nome = ''

  ação = int(input('Menu Login:\n 1 - Fazer Login \n 2 - Cadastrar \n 3 - Sair:\n'))

  while ação != 100:

    if ação == 1:

      cpf = int(input('Digite seu cpf:\n'))
      senha = str(input('Digite sua senha:\n'))
      
      if(user.cpf == cpf and user.senha == senha):
        print("####################################################\nBem Vindo!",user.nome,'!\n####################################################\n\n')
        ação = int(input('Digite o número da ação:\n 1 - Mostrar Publicações \n 2 - Fazer uma Publicação \n 3 - Sair\n'))

        if ação == 1:
          return Pub()
        
        elif ação == 2:
          return Npub()
          
      else:
        print("####################################################\nACESSO NEGADO\n Senha ou CPF invalido.\n####################################################\n\n")
        
      continue

      

    elif ação == 2:

      user = Login(cpf,nome,senha)

      nome = str(input('Digite seu nome: \n'))
      cpf = int(input('Digite seu cpf: \n'))
      if len(str(cpf)) != 11 :
        print("Esse CPF não é válido")
        continue
      senha = str(input('Digite sua senha: \n'))

      user.DefNome(nome) 
      user.DefCPF(cpf)
      user.DefSenha(senha)

      print("####################################################\nCadastrado com sucesso!\n####################################################\n\n")
      ação = int(input('Digite o número da ação:\n 1 - Fazer Login \n 2 - Cadastrar \n 3 - Sair\n'))

    else:
      break





