## JOGO DA ADIVINHAÇÃO ##

from random import randint
def jogar():

      print("*****************************************\n"
            "*** Bem vindo ao jogo de adivinhação! ***\n"
            "*****************************************")

      num_secreto = (randint(1, 100))
      total_tentativas = 0
      pontos = 1000

      print(f"* Seus pontos são {pontos}! *\n"
            "Qual o nível de dificuldade?\n"
            "(1) Fácil (2) Médio (3) Difícil")

      # Validação do nível de dificuldade.
      nivel = 0
      while (nivel != 1) and (nivel != 2) and (nivel != 3):
          nivel = int(input("Defina o nível: "))
          if nivel != 1 and nivel != 2 and nivel != 3:
              print("Escolha um nível de dificuldade válido!")

      # Atribuindo total de tentativas aos niveis de dificuldade.
      if (nivel == 1):
          total_tentativas = 20
      elif (nivel == 2):
          total_tentativas = 10
      else:
          total_tentativas = 5

      #
      for rodada in range(1, total_tentativas + 1):
          print(f"'Tentativa {rodada} de {total_tentativas}'")

          # Validação do número número digitado pelo usuário.
          chute = 0
          while chute < 1 or chute > 100:
              chute = int(input("Digite um número entre 1 e 100: "))
              if chute < 1 or chute > 100:
                  print("Digite um número entre 1 e 100!")

          print(f"Número digitado -> {chute}")

          # Valida se o número digitado pelo usuário é igual ao número secreto.
          if (chute == num_secreto):
              print("Acertou!")
              print("Fim de jogo")
              break

          # Valida se o número digitado pelo usuário foi maior ou não que o número secreto.
          elif (chute > num_secreto):
              print("! O chute foi maior que o número secreto !")
          elif (chute < num_secreto):
              print("! O chute foi menor que o número secreto !")

          # Calculo de quantos pontos o usuário perde ao errar um número.
          pontos_perdidos = abs(num_secreto - chute)
          pontos = pontos - pontos_perdidos
      print(f"Seus pontos são {pontos}")

      # Se o número de tentativas for igual a zero, essa parte de código vê se o número secreto for diferente do número
      # digitado ai ela printa na tela (fim de jogo.) e também mostra qual era o número secreto.
      if (num_secreto != chute):
          print(f"Fim de jogo. O número secreto era {num_secreto}.")


if (__name__ == "__main__"):
    jogar()
