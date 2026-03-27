from models.ubs import Ubs
from models.documento import Documento
from enum import Enum

from typing import TYPE_CHECKING

if TYPE_CHECKING:
  from models.email import Email
  from models.telefone import Telefone

class EstadoCivil(Enum):
  SOLTEIRO = "Solteiro(a)"
  CASADO = "Casado(a)"
  DIVORCIADO = "Divorciado(a)"
  VIUVO = "Viúvo(a)"
  UNIAO_ESTAVEL = "União estável"

class Pessoa:
  def __init__(self, nome_pessoa, estado_civil, ubs: Ubs):
    
    self.id_pessoa = None
    self.nome_pessoa = nome_pessoa
    self.emails = []
    self.telefones = []
    self.documentos = []
    self.estado_civil = estado_civil if isinstance(estado_civil, EstadoCivil) else EstadoCivil(estado_civil)
    self.ubs = ubs
    
  def adicionar_email(self, email: "Email"):
    self.emails.append(email)
  
  def exibir_emails(self):
    print("--- Emails ---")
    for email in self.emails:
      print(f"Email: {email.email}")
    print("---------------")

  def adicionar_telefone(self, telefone: "Telefone"):
    self.telefones.append(telefone)

  def exibir_telefones(self):
    print("--- Telefones ---")
    for telefone in self.telefones:
      print(f"Telefone: {telefone.num_telefone}")
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
    print(f"Estado Cívil: {self.estado_civil.value}")
    print()
    
    self.exibir_documentos()
    print()
    
    self.exibir_emails()
    print()
    
    self.exibir_telefones()
    print()
    
    print(f"Nome da UBS: {self.ubs.name}")
    print("----------------\n")