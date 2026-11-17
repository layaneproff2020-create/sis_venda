# item_venda.py
from produto import Produto

class ItemVenda:
    def __init__(self, produto: Produto, quantidade: int):
        self.produto = produto  # Referência ao objeto Produto
        self.quantidade = quantidade
        # O valor_item é calculado no momento da criação do item
        self.valor_item = produto.preco_unitario * quantidade

    def calcular_subtotal(self) -> float:
        """Retorna o valor total deste item."""
        return self.valor_item

    def __str__(self):
        return f"{self.quantidade}x {self.produto.descricao} - Subtotal: R$ {self.calcular_subtotal():.2f}"