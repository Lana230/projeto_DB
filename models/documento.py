from enum import Enum

class TipoDocumento(Enum):
    CPF = "CPF"
    RG = "RG"
    CNH = "CNH"
    CERTIDAO_NASCIMENTO = "Certidão de nascimento"

class Documento():
    def __init__(self, tipo_documento, numero_documento):
        self.tipo_documento = tipo_documento
        self.numero_documento = numero_documento
        
    def exibir(self):
        print("--- Documento ---")
        print(f"Tipo do documento: {self.tipo_documento}")
        print(f"Número do documento: {self.numero_documento}")