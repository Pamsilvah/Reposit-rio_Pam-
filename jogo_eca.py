import sqlite3
import customtkinter as ctk

# CONFIG VISUAL
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# =========================
# BANCO DE DADOS
# =========================
conn = sqlite3.connect("eca_game.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS perguntas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT,
    a TEXT,
    b TEXT,
    c TEXT,
    d TEXT,
    correta TEXT
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS jogadores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    pontuacao INTEGER
)
""")

# INSERIR PERGUNTAS (SE TIVER VAZIO)
cursor.execute("SELECT COUNT(*) FROM perguntas")
if cursor.fetchone()[0] == 0:
    perguntas_exemplo = [
        ("Segundo o ECA, é dever da família garantir educação?", "Sim", "Não", "Só do governo", "Depende", "A"),
        ("O trabalho infantil antes dos 16 anos é permitido?", "Sim", "Não", "Só com autorização", "Depende", "B"),
        ("Toda criança tem direito à dignidade e respeito?", "Não", "Só em casa", "Sim", "Depende", "C"),
        ("O ECA protege contra violência física e psicológica?", "Não", "Sim", "Só física", "Depende", "B"),
    ]

    cursor.executemany(
        "INSERT INTO perguntas (pergunta, a, b, c, d, correta) VALUES (?, ?, ?, ?, ?, ?)",
        perguntas_exemplo
    )
    conn.commit()

# =========================
# APP
# =========================
class JogoECA:
    def __init__(self, root):
        self.root = root
        self.root.title("Jogo do ECA")
        self.root.geometry("600x400")

        self.nome = ""
        self.pontuacao = 0
        self.indice = 0
        self.perguntas = cursor.execute("SELECT * FROM perguntas").fetchall()

        self.tela_inicio()

    # =========================
    # TELA INICIAL
    # =========================
    def tela_inicio(self):
        self.limpar()

        titulo = ctk.CTkLabel(self.root, text="Jogo do ECA", font=("Arial", 28, "bold"))
        titulo.pack(pady=20)

        self.entry_nome = ctk.CTkEntry(self.root, placeholder_text="Digite seu nome")
        self.entry_nome.pack(pady=10)

        botao = ctk.CTkButton(self.root, text="Começar", command=self.iniciar_jogo)
        botao.pack(pady=20)

    def iniciar_jogo(self):
        self.nome = self.entry_nome.get()

        if self.nome == "":
            return

        self.pontuacao = 0
        self.indice = 0
        self.tela_jogo()

    # =========================
    # TELA DO JOGO
    # =========================
    def tela_jogo(self):
        self.limpar()

        self.progresso = ctk.CTkProgressBar(self.root, width=400)
        self.progresso.pack(pady=10)

        self.label_pergunta = ctk.CTkLabel(self.root, text="", wraplength=500, font=("Arial", 20, "bold"))
        self.label_pergunta.pack(pady=20)

        self.resposta = ctk.StringVar()

        self.botoes = []
        for letra in ["A", "B", "C", "D"]:
            btn = ctk.CTkRadioButton(self.root, text="", variable=self.resposta, value=letra)
            btn.pack(pady=5)
            self.botoes.append(btn)

        self.btn_responder = ctk.CTkButton(self.root, text="Responder", command=self.responder)
        self.btn_responder.pack(pady=20)

        self.carregar_pergunta()

    def carregar_pergunta(self):
        if self.indice >= len(self.perguntas):
            self.tela_final()
            return

        progresso_valor = self.indice / len(self.perguntas)
        self.progresso.set(progresso_valor)

        p = self.perguntas[self.indice]

        self.label_pergunta.configure(text=p[1], text_color="white")
        self.botoes[0].configure(text=p[2])
        self.botoes[1].configure(text=p[3])
        self.botoes[2].configure(text=p[4])
        self.botoes[3].configure(text=p[5])

        self.resposta.set("")

    def responder(self):
        escolha = self.resposta.get()
        correta = self.perguntas[self.indice][6]

        if escolha == correta:
            self.pontuacao += 10
            self.label_pergunta.configure(text="✅ Acertou!", text_color="green")
        else:
            self.label_pergunta.configure(text="❌ Errou!", text_color="red")

        self.root.after(1000, self.proxima_pergunta)

    def proxima_pergunta(self):
        self.indice += 1
        self.carregar_pergunta()

    # =========================
    # TELA FINAL
    # =========================
    def tela_final(self):
        self.limpar()

        cursor.execute(
            "INSERT INTO jogadores (nome, pontuacao) VALUES (?, ?)",
            (self.nome, self.pontuacao)
        )
        conn.commit()

        titulo = ctk.CTkLabel(self.root, text="Fim de Jogo!", font=("Arial", 26, "bold"))
        titulo.pack(pady=20)

        resultado = ctk.CTkLabel(
            self.root,
            text=f"{self.nome}, sua pontuação foi: {self.pontuacao}",
            font=("Arial", 18)
        )
        resultado.pack(pady=10)

        ranking_btn = ctk.CTkButton(self.root, text="Ver Ranking", command=self.tela_ranking)
        ranking_btn.pack(pady=10)

        sair_btn = ctk.CTkButton(self.root, text="Sair", command=self.root.quit)
        sair_btn.pack(pady=10)

    # =========================
    # RANKING
    # =========================
    def tela_ranking(self):
        self.limpar()

        titulo = ctk.CTkLabel(self.root, text="Ranking", font=("Arial", 26, "bold"))
        titulo.pack(pady=20)

        ranking = cursor.execute(
            "SELECT nome, pontuacao FROM jogadores ORDER BY pontuacao DESC LIMIT 5"
        ).fetchall()

        for nome, pontos in ranking:
            label = ctk.CTkLabel(self.root, text=f"{nome} - {pontos} pts")
            label.pack()

        voltar = ctk.CTkButton(self.root, text="Voltar", command=self.tela_inicio)
        voltar.pack(pady=20)

    # =========================
    def limpar(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# =========================
# EXECUTAR
# =========================
root = ctk.CTk()
app = JogoECA(root)
root.mainloop()

conn.close()