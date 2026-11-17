from pagamento import Pagamento

class PagamentoPix(Pagamento):
    def calcular_valor_final(self):
        return self.valor_base * 0.95   # 5% de desconto