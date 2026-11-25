from cliente import Cliente
from movimentacao import Movimentacao

class Conta:
    def __init__(self, numero: str, saldo: float, cliente: Cliente):
        self._numero = numero
        self._saldo = saldo
        self._cliente = cliente
        self._movimentacoes: list[Movimentacao] = [Movimentacao("Abertura da conta com saldo inicial de R${saldo:.2f}")]


        @property
        def numero(self):
            return self._numero

        @numero.setter
        def numero(self, novo_numero):
            self._numero = novo_numero

        @property 
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, novo_saldo):
            self._saldo = novo_saldo

        @property
        def  cliente(self):
            return self._cliente

        @cliente.setter
        def cliente(self, novo_cliente):
               self._cliente = novo_cliente


def obter_extrato(self):
    return self._Movimentacoes