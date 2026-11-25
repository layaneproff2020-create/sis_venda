from cliente import Cliente
from movimentacao import Movimentacao

class Conta:
    def __init__(self, numero: str, cliente: Cliente, saldo: float = 0):
        self._numero = numero
        self._saldo = saldo
        self._cliente = cliente
        self._movimentacoes: list[Movimentacao] = [
            Movimentacao(f"Abertura da conta com saldo inicial de R${saldo:.2f}")
        ]

    @property
    def numero(self):
        return self._numero

    @property
    def saldo(self):
        return self._saldo

    @property
    def cliente(self):
        return self._cliente

    def consultar_saldo(self) -> float:
        return self._saldo

    def obter_extrato(self):
        return self._movimentacoes
