from models.ubs import Ubs
from models.documento import Documento

class Pessoa:
  def __init__(self, nome_pessoa, estado_civil, ubs: Ubs):
    self.nome_pessoa = nome_pessoa
    self.emails = []
    self.telefones = []
    self.documentos = []
    self.estado_civil = estado_civil
    self.ubs = ubs
    
  #Permanecer assim para não resultar em fluxo circular, já que nos respectivos arquivos de telefone e email já importam pessoa

  #O que é passado para este método não é um objeto do tipo Email -> (String)
  def adicionar_email(self, email):
    self.emails.append(email)
  
  def exibir_emails(self):
    print("--- Emails ---")
    for email in self.emails:
      print(f"Email: {email}")
    print("---------------")

  #O que é passado para este método não é um objeto do tipo Telefone -> (String)
  def adicionar_telefone(self, telefone):
    self.telefones.append(telefone)

  def exibir_telefones(self):
    print("--- Telefones ---")
    for telefone in self.telefones:
      print(f"Telefone: {telefone}")
    print("----------------")
    
  def adicionar_documento(self, documento: Documento):
    self.documentos.append(documento)
  
  def exibir_documentos(self):
    print("--- Documentos ---")
    for documento in self.documentos:
      documento.exibir()

  def exibir(self):
    print("--- Pessoa: ---")
    print(f"Nome: {self.nome_pessoa}")
    print(f"Estado Cívil: {self.estado_civil}")
    print()
    
    self.exibir_documentos()
    print()
    
    self.exibir_emails()
    print()
    
    self.exibir_telefones()
    print()
    
    print(f"Nome da UBS: {self.ubs.name}")
    print("----------------\n")