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
    print("Emails")
    for email in self.emails:
      print(f"Email: {email.email}")

  def adicionar_telefone(self, telefone):
    self.telefones.append(telefone)

  def exibir_telefones(self):
    print("Telefones")
    for telefone in self.telefones:
      print(f"Telefone:{telefone.numero}")

  def exibir(self):
    print(f"Nome: {self.nome}")
    print(f"CPF: {self.cpf}")
    self.exibir_emails()
    self.exibir_telefones()
    print(f"ID da UBS: {self.id_ubs}")