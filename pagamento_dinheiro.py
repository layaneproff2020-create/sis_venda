from pagamento import Pagamento

class PagamentoDinheiro(Pagamento):
    def calcular_valor_final(self):
        return self.valor_base * 0.97   # 3% de desconto