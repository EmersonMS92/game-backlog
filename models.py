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
    

def adicionar_jogo(backlog, jogo):
    backlog.append(jogo)

def buscar_jogo(backlog, titulo_buscado):
    for jogo in backlog:
        if jogo.titulo.lower() == titulo_buscado.lower():
            return jogo
    return None

def atualizar_status(backlog, titulo, novo_status):
    jogo = buscar_jogo(backlog, titulo)
    if jogo is not None:
        jogo.status = novo_status
        return True
    return False

def remover_jogo(backlog, titulo):
    jogo = buscar_jogo(backlog, titulo)
    if jogo is not None:
        backlog.remove(jogo)
        return True
    return False


jogo1 = Jogo("The Legend of Zelda: Breath of the Wild", 2017, "Ação/Aventura", "Nintendo Switch", "Nintendo", 10, 70, "Zerado")
jogo2 = Jogo("The Witcher 3: Wild Hunt", 2015, "RPG", "PC, PS4, Xbox One", "CD Projekt Red", 9.5, 120, "Zerado")
jogo3 = Jogo("Cyberpunk 2077", 2020, "RPG de Ação", "PC, PS4, Xbox One", "CD Projekt Red", 7.5, 50, "Em andamento")

backlog = [jogo1, jogo2]
adicionar_jogo(backlog, jogo3)

resultado_busca = buscar_jogo(backlog, "The Witcher 3: Wild Hunt")
print(resultado_busca)

for jogo in backlog:
    print(jogo)

atualizar_status(backlog, "Cyberpunk 2077", "Zerado")
print(buscar_jogo(backlog, "Cyberpunk 2077"))

remover_jogo(backlog, "The Witcher 3: Wild Hunt")
for jogo in backlog:
    print(jogo)