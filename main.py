from pprint import pprint
from exceptions import OperacaoFinanceiraError, SaldoInsuficienteError
from leitor import LeitorDeArquivo
import traceback

class Cliente:
    def __init__(self, nome, cpf, profissao):
        self.nome = nome
        self.cpf = cpf
        self.profissao = profissao

class ContaCorrente:
    total_contas_criadas = 0
    taxa_operacao = None

    def __init__(self, cliente, agencia, numero):
        self.__saldo = 100
        self.cliente = cliente
        self.__set_agencia(agencia)
        self.__set_numero(numero)
        self.saques_nao_permitidos = 0
        self.trasferencias_nao_permitidas = 0
        ContaCorrente.total_contas_criadas += 1
        ContaCorrente.taxa_operacao = 30 / ContaCorrente.total_contas_criadas
    
    def transferir(self, value, favorecido):
        if (value < 0):
            raise ValueError("O valor a ser sacado não pode ser menor que zero")

        try:
            self.sacar(value)
        except SaldoInsuficienteError as E:
            self.trasferencias_nao_permitidas += 1
            raise OperacaoFinanceiraError("Operação não finalizada") from E
        favorecido.depositar(value)
    
    def sacar(self, value):
        if (value < 0):
            raise ValueError("O valor a ser sacado não pode ser menor que zero")
        if (self.__saldo < value):
            raise SaldoInsuficienteError('', self.__saldo, value)
            self.saques_nao_permitidos += 1
        self.__saldo -= value
    
    def depositar(self, value):
        self.__saldo += value
    
    @property
    def agencia(self):
        return self.__agencia
    
    def __set_agencia(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser inteiro", value)
        if (value <= 0):
            raise ValueError("O valor atribuido deve ser maior que zero")
        self.__agencia = value
    
    @property
    def numero(self):
        return self.__numero
    
    def __set_numero(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser inteiro")
        if (value <= 0):
            raise ValueError("O valor atribuido deve ser maior que zero")
        self.__numero = value
    
    @property
    def saldo(self):
        return self.__saldo
    
    @saldo.setter
    def saldo(self, value):
        if not isinstance(value, int):
            raise ValueError("O atributo agencia deve ser inteiro")
        self.__saldo = value


with LeitorDeArquivo("arquivo.txt") as leitor:
    leitor.ler_proxima_linha()

# try:
#     leitor = LeitorDeArquivo("arquivo.txt")
#     leitor.ler_proxima_linha()
#     leitor.ler_proxima_linha()
#     leitor.ler_proxima_linha()
# except FileNotFoundError:
#     print("Erro ao abrir")
# except IOError:
#     print("Erro ao ler")
# finally:
#     if 'leitor' in locals():
#         leitor.fechar()
# try:
#     c1 = ContaCorrente(None, 40, 1234567)
#     c2 = ContaCorrente(None, 41, 1234566)
#     c1.transferir(1000, c2)
#     print('Saldo c1:', c1.saldo)
#     print('Saldo c2:', c2.saldo)
# except SaldoInsuficienteError as E:
#     breakpoint()
#     pass
        
# def main():

#     import sys

#     contas = []

#     while True:
#         try:
#             nome = input("Nome Cliente:\n")
#             agencia = input("Numero de agencia:\n")
#             breakpoint()
#             numero = input("Numero da conta corrente:\n")
#             cliente = Cliente(nome, None, None)
#             conta_corrente = ContaCorrente(cliente, agencia, numero)
#             contas.append(conta_corrente)
#         except KeyboardInterrupt:
#             print(f"\n\n{len(contas)}(s) contas criadas")
#             sys.exit()

# if __name__ == "__main__":
#     main()