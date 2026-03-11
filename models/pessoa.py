class Pessoa:
  def __init__(self, cpf, nome, id_ubs):
    self.cpf = cpf
    self.nome = nome
    self.emails = []
    self.telefones = []
    self.id_ubs = id_ubs

  def adicionar_email(self, email):
    self.emails.append(email)

  def exibir_emails(self):
    for email in self.emails:
      print(email)

  def adicionar_telefone(self, telefone):
    self.telefones.append(telefone)

  def exibir_telefones(self):
    for telefone in self.telefones:
      print(telefone)

  def exibir(self):
    print(self.nome)
    print(self.cpf)
    self.exibir_emails()
    self.exibir_telefones()
    print(self.id_ubs)