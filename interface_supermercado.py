import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ===== IMPORTS DOS ARQUIVOS DO "MUNDO B" =====
from produto import Produto
from venda import Venda
from pagamento_dinheiro import PagamentoDinheiro
from pagamento_debito import PagamentoDebito
from pagamento_pix import PagamentoPix
from pagamento_cartao import PagamentoCartao

# ============ PALETA ============
COR_FUNDO       = "#0f172a"
COR_PAINEL      = "#1e293b"
COR_DESTAQUE    = "#22c55e"
COR_DESTAQUE2   = "#f59e0b"
COR_PERIGO      = "#ef4444"
COR_TEXTO       = "#f1f5f9"
COR_TEXTO_MUTED = "#94a3b8"
COR_BORDA       = "#334155"

FONTE_TITULO    = ("Segoe UI", 22, "bold")
FONTE_SUBTITULO = ("Segoe UI", 12, "bold")
FONTE_NORMAL    = ("Segoe UI", 11)


class InterfaceSupermercado:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Mercado Bom Preço - Sistema de Caixa")
        self.root.geometry("1150x720")
        self.root.configure(bg=COR_FUNDO)
        self.root.minsize(1000, 640)

        # ===== CATÁLOGO DE PRODUTOS REAIS =====
        self.catalogo = {
            "Mouse sem fio":   Produto("Mouse sem fio",   49.90, 30),
            "Camisa Polo":     Produto("Camisa Polo",     50.00, 20),
            "Caneta":          Produto("Caneta",           2.50, 100),
            "Pendrive 32GB":   Produto("Pendrive 32GB",   50.00, 10),
            "Teclado ABNT2":   Produto("Teclado ABNT2",  120.00, 15),
            "Monitor 24\"":    Produto("Monitor 24\"",   899.00, 8),
        }

        # ===== VENDA REAL (classe Venda) =====
        self.venda_atual = Venda()

        self._construir_cabecalho()
        self._construir_corpo()
        self._construir_rodape()

    # ---------- CABEÇALHO ----------
    def _construir_cabecalho(self):
        header = tk.Frame(self.root, bg=COR_PAINEL, height=90)
        header.pack(fill="x")
        header.pack_propagate(False)

        esq = tk.Frame(header, bg=COR_PAINEL)
        esq.pack(side="left", padx=25, pady=15)
        tk.Label(esq, text="🛒", font=("Segoe UI Emoji", 32),
                 bg=COR_PAINEL, fg=COR_DESTAQUE).pack(side="left")
        tk.Label(esq, text="Mercado Bom Preço", font=FONTE_TITULO,
                 bg=COR_PAINEL, fg=COR_TEXTO).pack(side="left", padx=12)

        dir_ = tk.Frame(header, bg=COR_PAINEL)
        dir_.pack(side="right", padx=25)
        self.lbl_relogio = tk.Label(dir_, text="", font=FONTE_NORMAL,
                                    bg=COR_PAINEL, fg=COR_TEXTO_MUTED)
        self.lbl_relogio.pack(anchor="e")
        self.lbl_vendas = tk.Label(
            dir_,
            text=f"Caixa 01  •  Vendas no sistema: {Venda.quantidade_vendas}",
            font=FONTE_SUBTITULO, bg=COR_PAINEL, fg=COR_DESTAQUE)
        self.lbl_vendas.pack(anchor="e")
        self._tick_relogio()

    def _tick_relogio(self):
        self.lbl_relogio.config(
            text=datetime.now().strftime("%d/%m/%Y  %H:%M:%S"))
        self.root.after(1000, self._tick_relogio)

    # ---------- CORPO ----------
    def _construir_corpo(self):
        corpo = tk.Frame(self.root, bg=COR_FUNDO)
        corpo.pack(fill="both", expand=True, padx=20, pady=20)
        self._construir_formulario(corpo)
        self._construir_carrinho(corpo)

    def _construir_formulario(self, parent):
        card = tk.Frame(parent, bg=COR_PAINEL,
                        highlightbackground=COR_BORDA, highlightthickness=1)
        card.pack(side="left", fill="y", padx=(0, 15), ipadx=10, ipady=10)

        tk.Label(card, text="➕ Adicionar Produto", font=FONTE_SUBTITULO,
                 bg=COR_PAINEL, fg=COR_TEXTO).pack(anchor="w", padx=18,
                                                   pady=(14, 10))

        # Combobox de produtos (vem do catálogo → objetos Produto reais)
        tk.Label(card, text="Produto", font=FONTE_NORMAL,
                 bg=COR_PAINEL, fg=COR_TEXTO_MUTED).pack(anchor="w", padx=18)
        self.cmb_produto = ttk.Combobox(
            card, values=list(self.catalogo.keys()),
            font=FONTE_NORMAL, state="readonly")
        self.cmb_produto.pack(fill="x", padx=18, pady=(2, 8), ipady=4)
        self.cmb_produto.bind("<<ComboboxSelected>>",
                              self._mostrar_info_produto)

        self.lbl_info = tk.Label(card, text="Selecione um produto",
                                 font=("Segoe UI", 9), bg=COR_PAINEL,
                                 fg=COR_TEXTO_MUTED, justify="left",
                                 anchor="w")
        self.lbl_info.pack(fill="x", padx=18, pady=(0, 12))

        # Quantidade
        tk.Label(card, text="Quantidade", font=FONTE_NORMAL,
                 bg=COR_PAINEL, fg=COR_TEXTO_MUTED).pack(anchor="w", padx=18)
        self.ent_qtd = tk.Entry(
            card, font=FONTE_NORMAL, bg="#0b1220", fg=COR_TEXTO,
            insertbackground=COR_TEXTO, relief="flat",
            highlightbackground=COR_BORDA, highlightcolor=COR_DESTAQUE,
            highlightthickness=1)
        self.ent_qtd.insert(0, "1")
        self.ent_qtd.pack(fill="x", padx=18, pady=(2, 12), ipady=6)

        tk.Button(card, text="Adicionar ao carrinho",
                  bg=COR_DESTAQUE, fg="#052e16",
                  font=("Segoe UI", 11, "bold"), relief="flat",
                  cursor="hand2", pady=10, activebackground="#16a34a",
                  command=self._adicionar_produto).pack(fill="x", padx=18,
                                                       pady=(6, 18))

        # Painel de total (valor base da Venda)
        total_card = tk.Frame(card, bg="#0b1220")
        total_card.pack(fill="x", padx=18, pady=(0, 12))
        tk.Label(total_card, text="TOTAL (base)", font=("Segoe UI", 10, "bold"),
                 bg="#0b1220", fg=COR_TEXTO_MUTED).pack(pady=(10, 0))
        self.lbl_total = tk.Label(total_card, text="R$ 0,00",
                                  font=("Segoe UI", 26, "bold"),
                                  bg="#0b1220", fg=COR_DESTAQUE)
        self.lbl_total.pack(pady=(0, 10))

    def _mostrar_info_produto(self, _=None):
        nome = self.cmb_produto.get()
        if nome not in self.catalogo:
            return
        p = self.catalogo[nome]
        self.lbl_info.config(
            text=f"Preço: R$ {p.preco_unitario:.2f}   •   Estoque: {p.estoque} un.")

    def _construir_carrinho(self, parent):
        card = tk.Frame(parent, bg=COR_PAINEL,
                        highlightbackground=COR_BORDA, highlightthickness=1)
        card.pack(side="left", fill="both", expand=True, ipadx=10, ipady=10)

        topo = tk.Frame(card, bg=COR_PAINEL)
        topo.pack(fill="x", padx=15, pady=(14, 8))
        tk.Label(topo, text="🛍️  Carrinho", font=FONTE_SUBTITULO,
                 bg=COR_PAINEL, fg=COR_TEXTO).pack(side="left")
        tk.Button(topo, text="Remover selecionado", bg=COR_PERIGO, fg="white",
                  font=("Segoe UI", 9, "bold"), relief="flat",
                  cursor="hand2", padx=10, activebackground="#b91c1c",
                  command=self._remover_item).pack(side="right")

        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Mercado.Treeview", background="#0b1220",
                        fieldbackground="#0b1220", foreground=COR_TEXTO,
                        rowheight=32, font=FONTE_NORMAL, borderwidth=0)
        style.configure("Mercado.Treeview.Heading", background=COR_PAINEL,
                        foreground=COR_DESTAQUE,
                        font=("Segoe UI", 10, "bold"), relief="flat")
        style.map("Mercado.Treeview",
                  background=[("selected", COR_DESTAQUE)],
                  foreground=[("selected", "#052e16")])

        cols = ("produto", "preco", "qtd", "subtotal")
        self.tree = ttk.Treeview(card, columns=cols, show="headings",
                                 style="Mercado.Treeview")
        for c, t in zip(cols, ("PRODUTO", "PREÇO", "QTD", "SUBTOTAL")):
            self.tree.heading(c, text=t)
            self.tree.column(c,
                             anchor="center" if c != "produto" else "w",
                             width=110 if c != "produto" else 260)
        self.tree.pack(fill="both", expand=True, padx=15, pady=8)
        self.tree.tag_configure("par",   background="#0f1a2e")
        self.tree.tag_configure("impar", background="#0b1220")

    # ---------- RODAPÉ ----------
    def _construir_rodape(self):
        rodape = tk.Frame(self.root, bg=COR_PAINEL, height=70)
        rodape.pack(fill="x", side="bottom")
        rodape.pack_propagate(False)

        tk.Button(rodape, text="🗑️  Limpar carrinho", bg=COR_PAINEL,
                  fg=COR_TEXTO_MUTED, font=FONTE_NORMAL, relief="flat",
                  cursor="hand2", activebackground=COR_BORDA,
                  command=self._limpar).pack(side="left", padx=20)

        # Seletor de forma de pagamento (aciona o polimorfismo de Pagamento)
        tk.Label(rodape, text="Pagamento:", font=FONTE_NORMAL,
                 bg=COR_PAINEL, fg=COR_TEXTO_MUTED
                 ).pack(side="right", padx=(0, 8))
        self.cmb_pag = ttk.Combobox(
            rodape, state="readonly", width=18, font=FONTE_NORMAL,
            values=["Dinheiro (-3%)", "Débito", "Pix (-5%)", "Cartão (+5%)"])
        self.cmb_pag.current(1)  # Débito por padrão
        self.cmb_pag.pack(side="right", padx=(0, 15), pady=18)

        tk.Button(rodape, text="💳  Finalizar Compra", bg=COR_DESTAQUE2,
                  fg="#451a03", font=("Segoe UI", 12, "bold"),
                  relief="flat", cursor="hand2", padx=25, pady=8,
                  activebackground="#d97706",
                  command=self._finalizar).pack(side="right", padx=10, pady=12)

    # ---------- AÇÕES ----------
    def _adicionar_produto(self):
        nome = self.cmb_produto.get()
        if not nome:
            messagebox.showwarning("Atenção", "Selecione um produto.")
            return
        try:
            qtd = int(self.ent_qtd.get())
            if qtd <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Atenção", "Quantidade inválida.")
            return

        produto = self.catalogo[nome]
        antes = len(self.venda_atual.itens)

        # Venda.adicionar_item já valida estoque e decrementa via Produto
        self.venda_atual.adicionar_item(produto, qtd)
        depois = len(self.venda_atual.itens)

        if depois == antes:
            messagebox.showerror(
                "Estoque insuficiente",
                f"'{produto.descricao}' só tem {produto.estoque} un. disponíveis.")
            return

        self._atualizar_tree()
        self._mostrar_info_produto()
        self.ent_qtd.delete(0, tk.END)
        self.ent_qtd.insert(0, "1")

    def _atualizar_tree(self):
        self.tree.delete(*self.tree.get_children())
        for i, item in enumerate(self.venda_atual.itens):
            tag = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", iid=str(i), tags=(tag,), values=(
                item.produto.descricao,
                f"R$ {item.produto.preco_unitario:.2f}",
                item.quantidade,
                f"R$ {item.calcular_subtotal():.2f}"))
        total = self.venda_atual.calcular_total()
        self.lbl_total.config(text=self._brl(total))

    def _remover_item(self):
        sel = self.tree.selection()
        if not sel:
            return
        item = self.venda_atual.itens[int(sel[0])]
        self.venda_atual.remover_item(item.produto)  # devolve ao estoque
        self._atualizar_tree()
        self._mostrar_info_produto()

    def _limpar(self):
        if not self.venda_atual.itens:
            return
        if messagebox.askyesno("Confirmar", "Limpar todo o carrinho?"):
            for item in list(self.venda_atual.itens):
                self.venda_atual.remover_item(item.produto)
            self._atualizar_tree()
            self._mostrar_info_produto()

    def _finalizar(self):
        if not self.venda_atual.itens:
            messagebox.showinfo("Carrinho vazio",
                                "Adicione produtos antes de finalizar.")
            return

        modalidade = self.cmb_pag.get()
        mapa = {
            "Dinheiro (-3%)": PagamentoDinheiro,
            "Débito":         PagamentoDebito,
            "Pix (-5%)":      PagamentoPix,
            "Cartão (+5%)":   PagamentoCartao,
        }
        pagamento = mapa[modalidade](0)

        # Chama Venda.finalizar() → usa polimorfismo de Pagamento
        self.venda_atual.finalizar(pagamento)
        resumo = self.venda_atual.resumo()

        # Monta recibo formatado para a MessageBox
        linhas = [f"📅 {resumo['data']}", ""]
        for it in resumo["itens"]:
            linhas.append(f"  {it['qtd']}x {it['descricao']:<18}"
                          f"R$ {it['subtotal']:>8.2f}")
        linhas += [
            "",
            "─" * 42,
            f"Valor base:      R$ {resumo['valor_base']:>8.2f}",
            f"Modalidade:      {resumo['modalidade']}",
            f"VALOR FINAL:     R$ {resumo['valor_final']:>8.2f}",
        ]
        messagebox.showinfo(
            f"✅ Venda #{Venda.quantidade_vendas} finalizada",
            "\n".join(linhas))

        # Cria nova venda (estoque já foi decrementado pelo Produto)
        self.venda_atual = Venda()
        self.lbl_vendas.config(
            text=f"Caixa 01  •  Vendas no sistema: {Venda.quantidade_vendas}")
        self._atualizar_tree()
        self._mostrar_info_produto()

    @staticmethod
    def _brl(valor: float) -> str:
        return (f"R$ {valor:,.2f}"
                .replace(",", "X").replace(".", ",").replace("X", "."))


if __name__ == "__main__":
    root = tk.Tk()
    InterfaceSupermercado(root)
    root.mainloop()
