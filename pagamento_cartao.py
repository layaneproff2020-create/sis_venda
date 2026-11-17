from pagamento import Pagamento

class PagamentoCartao(Pagamento):
    def calcular_valor_final(self):
        return self.valor_base * 1.05   # 5% de acréscimo