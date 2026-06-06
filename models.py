class Jogo:
    def __init__(self, titulo, ano_lancamento, genero, plataforma, desenvolvedor, nota, tempo_jogado, status):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
        self.genero = genero
        self.plataforma = plataforma
        self.desenvolvedor = desenvolvedor
        self.nota = nota
        self.tempo_jogado = tempo_jogado    
        self.status = status

    def __str__(self):
        return f"{self.titulo} ({self.ano_lancamento}) — {self.status}, nota {self.nota}" 
    
jogo1 = Jogo("The Legend of Zelda: Breath of the Wild", 2017, "Ação/Aventura", "Nintendo Switch", "Nintendo", 10, 70, "Zerado")
jogo2 = Jogo("The Witcher 3: Wild Hunt", 2015, "RPG", "PC, PS4, Xbox One", "CD Projekt Red", 9.5, 120, "Zerado")

backlog = [jogo1, jogo2]

for jogo in backlog:
    print(jogo)