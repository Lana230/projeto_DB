from enum import Enum

class TipoDocumento(Enum):
    CPF = "CPF"
    RG = "RG"
    CNH = "CNH"
    CERTIDAO_NASCIMENTO = "Certidão de nascimento"

class Documento():
    def __init__(self, tipo_documento, numero_documento, id_pessoa):
        
        self.id_documento = None
        self.tipo_documento = tipo_documento if isinstance(tipo_documento, TipoDocumento) else TipoDocumento(tipo_documento)
        self.numero_documento = numero_documento
        self.id_pessoa = id_pessoa
        
    def exibir(self):
        print("--- Documento ---")
        print(f"Tipo do documento: {self.tipo_documento.value}")
        print(f"Número do documento: {self.numero_documento}")