
class Produto:
    def __init__(self, descricao: str, preco_unitario: float, estoque: int = 0):
        self.descricao = descricao
        self.preco_unitario = preco_unitario
        self.estoque = estoque

    def decrementar_estoque(self, quant: int) -> bool:
        if self.estoque >= quant:
            self.estoque -= quant
            return True
        return False

    def incrementar_estoque(self, quant: int) -> None:
        self.estoque += quant

    def __str__(self):
        return f"{self.descricao} (R$ {self.preco_unitario:.2f})"
