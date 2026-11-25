
from produto import Produto
from venda import Venda
from pagamento import Pagamento  


produto1 = Produto("Caneta", 2.50, 100)

venda1 = Venda()
venda1.adicionar_item(produto=produto1, quant=1)   

print(f"\nTotal de vendas no sistema: {Venda.quantidade_vendas}")
