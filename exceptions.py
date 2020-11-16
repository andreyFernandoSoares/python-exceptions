class OperacaoFinanceiraError(Exception):
    pass

class SaldoInsuficienteError(OperacaoFinanceiraError):
    def __init__(self, message="", saldo=None, valor=None, *args):
        self.saldo = saldo
        self.valor = valor
        msg = """Saldo insuficiente para efeturar a trasação! Saldo atual: {} Valor a ser sacado: {}""".format(self.saldo, self.valor)
        super(SaldoInsuficienteError, self).__init__(message or msg, self.saldo, self.valor, *args)
