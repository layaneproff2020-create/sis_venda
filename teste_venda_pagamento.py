from produto import Produto
from venda import Venda
from pagamento_debito import PagamentoDebito
from pagamento_pix import PagamentoPix
from pagamento_cartao import PagamentoCartao


def nova_venda():
    p1 = Produto("mouse", 100, 5)
    p2 = Produto("pendrive", 50, 10)

    v = Venda()
    v.adicionar_item(p1, 1)   # 100
    v.adicionar_item(p2, 2)   # 100
    return v                  # total = 200


# Teste 1 - Débito
v = nova_venda()
v.finalizar(PagamentoDebito(0))

# Teste 2 - Pix
v = nova_venda()
v.finalizar(PagamentoPix(0))

# Teste 3 - Cartão
v = nova_venda()
v.finalizar(PagamentoCartao(0))