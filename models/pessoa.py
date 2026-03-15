from models.ubs import Ubs

class Pessoa:
  def __init__(self, cpf, nome, ubs: Ubs):
    self.cpf = cpf
    self.nome = nome
    self.emails = []
    self.telefones = []
    self.ubs = ubs

  def adicionar_email(self, email):
    self.emails.append(email)

  def exibir_emails(self):
    print("--- Emails ---")
    for email in self.emails:
      print(f"Email: {email.email}")
    print("----------------")

  def adicionar_telefone(self, telefone):
    self.telefones.append(telefone)

  def exibir_telefones(self):
    print("--- Telefones ---")
    for telefone in self.telefones:
      print(f"Telefone:{telefone.num_telefone}")
    print("----------------")

  def exibir(self):
    print("--- Pessoa: ---")
    print(f"Nome: {self.nome}")
    print(f"CPF: {self.cpf}")
    print()
    
    self.exibir_emails()
    print()
    
    self.exibir_telefones()
    print()
    
    print(f"Nome da UBS: {self.ubs.name}")
    print("----------------\n")