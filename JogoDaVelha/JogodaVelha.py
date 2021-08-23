class JogoDaVelha:
  # declarando função no python
  def __init__(self):
    self.tamanho = 3 # dimensão do tabuleiro
    self.total_jogadas = 1 # contador de jogadas (limite = 9)
    self.jogador_atual = 1 # verificar se jogador atual é o jogador nº 1 ou 2

    # criação do tabuleiro
    self.tabuleiro = [['-' for x in range(self.tamanho)] for y in range(self.tamanho)]

  def jogo(self):
    while True:
      resposta = int(input("Ola! Gostaria de jogar?\n1 - SIM\n2 - NAO\n"))
      if resposta == 1:
        self.iniciarPartida()
      elif resposta == 2:
        exit(0)
      else:
        print("Opcao invalida!!!")


  def iniciarPartida(self):
    while self.total_jogadas != 9:
      self.exibirJogo()
      linha = int(input("\nJogador %s, faca a sua jogada, selecionando uma linha de numero entre 1 e 3\n" %self.jogador_atual))
      coluna = int(input("\nJogador %s, faca a sua jogada, selecionando uma coluna de numero entre 1 e 3\n" %self.jogador_atual))
      linha = linha - 1
      coluna = coluna - 1
      self.jogar(linha, coluna)

  def exibirJogo(self):
    print(" %s | %s | %s     1 | 2 | 3" %(self.tabuleiro[0][0],self.tabuleiro[0][1],self.tabuleiro[0][2]))
    print("-----------")
    print(" %s | %s | %s     4 | 5 | 6" %(self.tabuleiro[1][0],self.tabuleiro[1][1],self.tabuleiro[1][2]))
    print("-----------")
    print(" %s | %s | %s     7 | 8 | 9" %(self.tabuleiro[2][0],self.tabuleiro[2][1],self.tabuleiro[2][2]))

  def jogar(self, linha, coluna):
    if self.tabuleiro[linha][coluna] == '-':
      # verificar qual jogador fez a jogada
      if self.jogador_atual == 1:
        self.tabuleiro[linha][coluna] = "X"
      else:
        self.tabuleiro[linha][coluna] = "O"
      
      # verificar se houve um vencedor
      print("\nJogada feita pelo jogador %s efetuada com sucesso." %self.jogador_atual)
      temVencedor = self.verificarVencedor()
      if temVencedor == True:
        self.exibirJogo()
        print("\nFim de jogo.")
        exit(0)

      # verificar quem vai fazer a próxima jogada
      if self.jogador_atual == 1:
        self.jogador_atual = 2
      else:
        self.jogador_atual = 1

      return True
    else:
      print("\nJogada do jogador %s invalida. Tente outra!" %self.jogador_atual)
      return False

  def verificarVencedor(self):
    for i in range(self.tamanho):
      if self.tabuleiro[i][0] == "X" and self.tabuleiro[i][1] == "X" and self.tabuleiro[i][2] == "X" or self.tabuleiro[i][0] == "O" and self.tabuleiro[i][1] == "O" and self.tabuleiro[i][2] == "O":
        print("\nJogador %s venceu!!!\n" %self.jogador_atual)
        return True
      elif self.tabuleiro[0][i] == "X" and self.tabuleiro[1][i] == "X" and self.tabuleiro[2][i] == "X" or self.tabuleiro[0][i] == "O" and self.tabuleiro[1][i] == "O" and self.tabuleiro[2][i] == "O":
        print("\nJogador %s venceu!!!\n" %self.jogador_atual)
        return True

    if self.tabuleiro[0][0] == "X" and self.tabuleiro[1][1] == "X" and self.tabuleiro[2][2] == "X" or self.tabuleiro[0][0] == "O" and self.tabuleiro[1][1] == "O" and self.tabuleiro[2][2] == "O":
      print("\nJogador %s venceu!!!\n" %self.jogador_atual)
      return True

    elif self.tabuleiro[0][2] == "X" and self.tabuleiro[1][1] == "X" and self.tabuleiro[2][0] == "X" or self.tabuleiro[0][2] == "O" and self.tabuleiro[1][1] == "O" and self.tabuleiro[2][0] == "O":
      print("\nJogador %s venceu!!!\n" %self.jogador_atual)
      return True
