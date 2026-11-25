import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ============ PALETA DE CORES ============
COR_FUNDO       = "#0f172a"   # azul-noite
COR_PAINEL      = "#1e293b"   # painel
COR_DESTAQUE    = "#22c55e"   # verde (sucesso)
COR_DESTAQUE2   = "#f59e0b"   # laranja (alertas)
COR_PERIGO      = "#ef4444"   # vermelho
COR_TEXTO       = "#f1f5f9"
COR_TEXTO_MUTED = "#94a3b8"
COR_BORDA       = "#334155"

FONTE_TITULO   = ("Segoe UI", 22, "bold")
FONTE_SUBTITULO= ("Segoe UI", 12, "bold")
FONTE_NORMAL   = ("Segoe UI", 11)
FONTE_MONO     = ("Consolas", 11)


class InterfaceSupermercado:
    def __init__(self, root):
        self.root = root
        self.root.title("🛒 Mercado Bom Preço - Sistema de Caixa")
        self.root.geometry("1100x680")
        self.root.configure(bg=COR_FUNDO)
        self.root.minsize(900, 600)

        # Carrinho: lista de (nome, preço, qtd)
        self.carrinho = []

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
        tk.Label(dir_, text="Operador: Layane  •  Caixa 01",
                 font=FONTE_SUBTITULO, bg=COR_PAINEL,
                 fg=COR_DESTAQUE).pack(anchor="e")
        self._tick_relogio()

    def _tick_relogio(self):
        agora = datetime.now().strftime("%d/%m/%Y  %H:%M:%S")
        self.lbl_relogio.config(text=agora)
        self.root.after(1000, self._tick_relogio)

    # ---------- CORPO ----------
    def _construir_corpo(self):
        corpo = tk.Frame(self.root, bg=COR_FUNDO)
        corpo.pack(fill="both", expand=True, padx=20, pady=20)

        # Coluna esquerda: formulário de adicionar produto
        self._construir_formulario(corpo)

        # Coluna direita: lista/carrinho
        self._construir_carrinho(corpo)

    def _construir_formulario(self, parent):
        card = tk.Frame(parent, bg=COR_PAINEL,
                        highlightbackground=COR_BORDA, highlightthickness=1)
        card.pack(side="left", fill="y", padx=(0, 15), ipadx=10, ipady=10)

        tk.Label(card, text="➕ Adicionar Produto", font=FONTE_SUBTITULO,
                 bg=COR_PAINEL, fg=COR_TEXTO).pack(anchor="w", padx=18, pady=(14, 10))

        self.ent_nome = self._campo(card, "Nome do produto")
        self.ent_preco = self._campo(card, "Preço unitário (R$)")
        self.ent_qtd   = self._campo(card, "Quantidade", default="1")

        btn = tk.Button(card, text="Adicionar ao carrinho",
                        bg=COR_DESTAQUE, fg="#052e16",
                        font=("Segoe UI", 11, "bold"),
                        relief="flat", cursor="hand2", pady=10,
                        activebackground="#16a34a",
                        command=self._adicionar_produto)
        btn.pack(fill="x", padx=18, pady=(6, 18))

        # Painel de total
        total_card = tk.Frame(card, bg="#0b1220")
        total_card.pack(fill="x", padx=18, pady=(0, 12))

        tk.Label(total_card, text="TOTAL", font=("Segoe UI", 10, "bold"),
                 bg="#0b1220", fg=COR_TEXTO_MUTED).pack(pady=(10, 0))
        self.lbl_total = tk.Label(total_card, text="R$ 0,00",
                                  font=("Segoe UI", 26, "bold"),
                                  bg="#0b1220", fg=COR_DESTAQUE)
        self.lbl_total.pack(pady=(0, 10))

    def _campo(self, parent, label, default=""):
        tk.Label(parent, text=label, font=FONTE_NORMAL,
                 bg=COR_PAINEL, fg=COR_TEXTO_MUTED).pack(anchor="w", padx=18)
        e = tk.Entry(parent, font=FONTE_NORMAL, bg="#0b1220", fg=COR_TEXTO,
                     insertbackground=COR_TEXTO, relief="flat",
                     highlightbackground=COR_BORDA, highlightcolor=COR_DESTAQUE,
                     highlightthickness=1)
        if default:
            e.insert(0, default)
        e.pack(fill="x", padx=18, pady=(2, 12), ipady=6)
        return e

    def _construir_carrinho(self, parent):
        card = tk.Frame(parent, bg=COR_PAINEL,
                        highlightbackground=COR_BORDA, highlightthickness=1)
        card.pack(side="left", fill="both", expand=True, ipadx=10, ipady=10)

        topo = tk.Frame(card, bg=COR_PAINEL)
        topo.pack(fill="x", padx=15, pady=(14, 8))
        tk.Label(topo, text="🛍️  Carrinho", font=FONTE_SUBTITULO,
                 bg=COR_PAINEL, fg=COR_TEXTO).pack(side="left")

        btn_rem = tk.Button(topo, text="Remover selecionado",
                            bg=COR_PERIGO, fg="white",
                            font=("Segoe UI", 9, "bold"), relief="flat",
                            cursor="hand2", padx=10,
                            activebackground="#b91c1c",
                            command=self._remover_item)
        btn_rem.pack(side="right")

        # Estilo da Treeview
        style = ttk.Style()
        style.theme_use("clam")
        style.configure("Mercado.Treeview",
                        background="#0b1220", fieldbackground="#0b1220",
                        foreground=COR_TEXTO, rowheight=32,
                        font=FONTE_NORMAL, borderwidth=0)
        style.configure("Mercado.Treeview.Heading",
                        background=COR_PAINEL, foreground=COR_DESTAQUE,
                        font=("Segoe UI", 10, "bold"), relief="flat")
        style.map("Mercado.Treeview",
                  background=[("selected", COR_DESTAQUE)],
                  foreground=[("selected", "#052e16")])

        colunas = ("produto", "preco", "qtd", "subtotal")
        self.tree = ttk.Treeview(card, columns=colunas, show="headings",
                                 style="Mercado.Treeview")
        titulos = {"produto": "PRODUTO", "preco": "PREÇO",
                   "qtd": "QTD", "subtotal": "SUBTOTAL"}
        for c in colunas:
            self.tree.heading(c, text=titulos[c])
            self.tree.column(c, anchor="center" if c != "produto" else "w",
                             width=110 if c != "produto" else 260)
        self.tree.pack(fill="both", expand=True, padx=15, pady=8)

        self.tree.tag_configure("par", background="#0f1a2e")
        self.tree.tag_configure("impar", background="#0b1220")

    # ---------- RODAPÉ ----------
    def _construir_rodape(self):
        rodape = tk.Frame(self.root, bg=COR_PAINEL, height=70)
        rodape.pack(fill="x", side="bottom")
        rodape.pack_propagate(False)

        tk.Button(rodape, text="🗑️  Limpar carrinho",
                  bg=COR_PAINEL, fg=COR_TEXTO_MUTED,
                  font=FONTE_NORMAL, relief="flat", cursor="hand2",
                  activebackground=COR_BORDA,
                  command=self._limpar).pack(side="left", padx=20)

        tk.Button(rodape, text="💳  Finalizar Compra",
                  bg=COR_DESTAQUE2, fg="#451a03",
                  font=("Segoe UI", 12, "bold"), relief="flat",
                  cursor="hand2", padx=25, pady=8,
                  activebackground="#d97706",
                  command=self._finalizar).pack(side="right", padx=20, pady=12)

    # ---------- AÇÕES ----------
    def _adicionar_produto(self):
        nome = self.ent_nome.get().strip()
        try:
            preco = float(self.ent_preco.get().replace(",", "."))
            qtd = int(self.ent_qtd.get())
            if not nome or preco <= 0 or qtd <= 0:
                raise ValueError
        except ValueError:
            messagebox.showwarning("Atenção",
                "Preencha nome, preço (>0) e quantidade (>0) corretamente.")
            return

        self.carrinho.append((nome, preco, qtd))
        self._atualizar_tree()
        self.ent_nome.delete(0, tk.END)
        self.ent_preco.delete(0, tk.END)
        self.ent_qtd.delete(0, tk.END)
        self.ent_qtd.insert(0, "1")
        self.ent_nome.focus()

    def _atualizar_tree(self):
        self.tree.delete(*self.tree.get_children())
        total = 0.0
        for i, (nome, preco, qtd) in enumerate(self.carrinho):
            sub = preco * qtd
            total += sub
            tag = "par" if i % 2 == 0 else "impar"
            self.tree.insert("", "end", iid=str(i), tags=(tag,),
                             values=(nome, f"R$ {preco:.2f}",
                                     qtd, f"R$ {sub:.2f}"))
        self.lbl_total.config(text=f"R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))

    def _remover_item(self):
        sel = self.tree.selection()
        if not sel:
            return
        idx = int(sel[0])
        del self.carrinho[idx]
        self._atualizar_tree()

    def _limpar(self):
        if self.carrinho and messagebox.askyesno("Confirmar",
                "Deseja limpar todo o carrinho?"):
            self.carrinho.clear()
            self._atualizar_tree()

    def _finalizar(self):
        if not self.carrinho:
            messagebox.showinfo("Carrinho vazio",
                                "Adicione produtos antes de finalizar.")
            return
        total = sum(p * q for _, p, q in self.carrinho)
        itens = len(self.carrinho)
        msg = (f"Compra finalizada!\n\n"
               f"Itens: {itens}\n"
               f"Total: R$ {total:,.2f}".replace(",", "X").replace(".", ",").replace("X", "."))
        messagebox.showinfo("✅ Sucesso", msg)
        self.carrinho.clear()
        self._atualizar_tree()


if __name__ == "__main__":
    root = tk.Tk()
    InterfaceSupermercado(root)
    root.mainloop()
