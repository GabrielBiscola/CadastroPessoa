# CLASSE ENDERECO
from datetime import date


class Endereco:
    def _init_(self, logradouro="", numero="", endereco_Comercial=False):
        # Inicializar atributos com valores padrão
        self.logradouro = logradouro
        self.numero = numero
        self.endereco_Comercial = endereco_Comercial

# CLASSE PESSOA
class Pessoa:
    def _init_(self, nome="", rendimento=0.0, endereco=None):
        # Inicializar atributos com valores padrão
        self.nome = nome
        self.rendimento = rendimento
        self.endereco = endereco

    def calcular_imposto(self, rendimento):
        return rendimento

# CLASSE PESSOA FISICA
class PessoaFisica(Pessoa):
    def _init_(self, nome="", rendimento=0.0, endereco=None, cpf="", dataNascimento=None):
        if endereco is None:
            endereco = Endereco()

        if dataNascimento is None:
            dataNascimento = date.today()

        super()._init_(nome, rendimento, endereco)
        
        self.cpf = cpf
        self.dataNascimento = dataNascimento

    def calcular_imposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0
        elif 1500 < rendimento <= 3500:
            return (rendimento * 0.02)
        elif 3500 < rendimento <= 6000:
            return (rendimento * 0.035)
        # chama o construtor da superclasse Pessoa para inicializar os atributos herdados
        else:
            return (rendimento * 0.05)

# CLASSE PESSOA JURIDICA
class PessoaJuridica(Pessoa):
    def _init_(self, nome="", rendimento=0.0, endereco=None, cnpj="", dataAbertura=None):
        if endereco is None:
            endereco = Endereco()

        if dataAbertura is None:
            dataAbertura = date.today()

        super()._init_(nome, rendimento, endereco)
        
        self.cnpj = cnpj
        self.dataAbertura = dataAbertura

    def calcular_imposto(self, rendimento: float) -> float:
        if rendimento <= 1500:
            return 0
        elif 1500 < rendimento <= 3500:
            return (rendimento)
        elif 3500 < rendimento <= 6000:
            return (rendimento)
        else:
            return (rendimento)