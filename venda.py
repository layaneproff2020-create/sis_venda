
from datetime import datetime
from produto import Produto
from item_venda import ItemVenda
from pagamento import Pagamento


class Venda:
  
    quantidade_vendas = 0

    def __init__(self):
        self.data = datetime.now()
        self.valor_total = 0.0
        self.itens = []
        self.pagamento = None


        Venda.quantidade_vendas += 1

    def adicionar_item(self, produto: Produto, quant: int):
        """Tenta adicionar um item à venda se houver estoque."""
        if produto.decrementar_estoque(quant):
            novo_item = ItemVenda(produto, quant)
            self.itens.append(novo_item)
            print(f"Item '{produto.descricao}' adicionado à venda.")
            self.calcular_total()
        else:
            print(f"ERRO: Estoque insuficiente para '{produto.descricao}'. "
                  f"Disponível: {produto.estoque}")

    def remover_item(self, produto: Produto):
        """Remove um item da venda e devolve a quantidade ao estoque."""
        for item in self.itens:
            if item.produto == produto:
                self.itens.remove(item)
                produto.estoque += item.quantidade
                print(f"Item '{produto.descricao}' removido da venda.")
                self.calcular_total()
                return
        print(f"ERRO: Produto '{produto.descricao}' não encontrado nesta venda.")

    def calcular_total(self) -> float:
        """Calcula e atualiza o valor total da venda (valor base)."""
        self.valor_total = sum(item.calcular_subtotal() for item in self.itens)
        return self.valor_total

    def finalizar(self, pagamento):
        self.calcular_total()
        pagamento.valor_base = self.valor_total
        self.pagamento = pagamento

        valor_final = pagamento.calcular_valor_final()  # polimorfismo

        print("\n" + "=" * 55)
        print("           RECIBO DA VENDA")
        print("=" * 55)
        print(f"Data: {self.data.strftime('%d/%m/%Y %H:%M:%S')}")
        for item in self.itens:
            print(f"  {item}")
        print("-" * 55)
        print(f"Valor base:         R$ {self.valor_total:.2f}")
        print(f"Modalidade:         {pagamento.__class__.__name__}")
        print(f"VALOR FINAL A PAGAR: R$ {valor_final:.2f}")
        print("=" * 55)

        return valor_final

    def __str__(self):
        recibo = (f"--- VENDA REALIZADA EM: "
                  f"{self.data.strftime('%d/%m/%Y %H:%M:%S')} ---\n")
        if not self.itens:
            recibo += "Nenhum item vendido.\n"
        else:
            for item in self.itens:
                recibo += f"{item}\n"
        recibo += f"VALOR TOTAL: R$ {self.valor_total:.2f}"
        return recibo

def resumo(self):
    """Retorna dict com os dados do recibo (para a interface exibir)."""
    self.calcular_total()
    valor_final = (self.pagamento.calcular_valor_final()
                   if self.pagamento else self.valor_total)
    return {
        "data": self.data.strftime('%d/%m/%Y %H:%M:%S'),
        "itens": [
            {"descricao": it.produto.descricao,
             "preco": it.produto.preco_unitario,
             "qtd": it.quantidade,
             "subtotal": it.calcular_subtotal()}
            for it in self.itens
        ],
        "valor_base": self.valor_total,
        "modalidade": self.pagamento.__class__.__name__ if self.pagamento else "-",
        "valor_final": valor_final,
    }
