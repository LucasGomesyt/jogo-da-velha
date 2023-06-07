def exibir_tabuleiro(tabuleiro):
    print("\nTabuleiro:")
    print("-------------")
    for linha in tabuleiro:
        print("|", end="")
        for elemento in linha:
            print(f"{elemento} ", end="|")
        print("\n-------------")

def verificar_vitoria(tabuleiro, jogador):
    # Verificar linhas
    for linha in tabuleiro:
        if linha.count(jogador) == 3:
            return True

    # Verificar colunas
    for coluna in range(3):
        if tabuleiro[0][coluna] == jogador and tabuleiro[1][coluna] == jogador and tabuleiro[2][coluna] == jogador:
            return True

    # Verificar diagonais
    if tabuleiro[0][0] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][2] == jogador:
        return True
    if tabuleiro[0][2] == jogador and tabuleiro[1][1] == jogador and tabuleiro[2][0] == jogador:
        return True

    return False

def jogar_jogo_da_velha():
    tabuleiro = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    jogador_atual = 'X'

    while True:
        exibir_tabuleiro(tabuleiro)

        linha = int(input("Digite o número da linha (0-2): "))
        coluna = int(input("Digite o número da coluna (0-2): "))

        if tabuleiro[linha][coluna] == ' ':
            tabuleiro[linha][coluna] = jogador_atual
        else:
            print("Posição ocupada. Tente novamente.")
            continue

        if verificar_vitoria(tabuleiro, jogador_atual):
            exibir_tabuleiro(tabuleiro)
            print(f"Jogador {jogador_atual} venceu!")
            break

        if ' ' not in tabuleiro[0] and ' ' not in tabuleiro[1] and ' ' not in tabuleiro[2]:
            exibir_tabuleiro(tabuleiro)
            print("Empate!")
            break

        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

jogar_jogo_da_velha()
