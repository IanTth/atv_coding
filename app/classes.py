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

class Login:
  def __init__(self, nome, cpf, senha):
    self.nome = nome
    self.cpf = cpf
    self.senha = senha

  def DefNome(self, novoNome):
    self.nome = novoNome

  def DefCPF(self, novoCPF):
    self.cpf = novoCPF

  def DefSenha(self, novaSenha):
    self.senha = novaSenha

