import random

palavras = ["fatecads", "python", "english"]

palavra = random.choice(palavras)

print(palavra)

tentativas = 0

chances = 4

letras_escolhidas = []

estado_atual = ["_"] * len(palavra)

print("\nBem-vindo ao Jogo da Forca!")
print("\n\nSeu objetivo é tentar ACERTAR a palavra secreta...")
print("Você terá que tentar uma letra por vez.")
print("Caso você acerte, a LETRA será colocada na palavra para que você chegue mais próximo possível de ACERTAR!")
print("Caso você erre, você terá mais uma chance, você tem no MÁXIMO", chances, "tentativas.")

while tentativas < chances and ''.join(estado_atual) != palavra:

  letra = input("\n\nQual letra você quer escolher? ")

  while letra in letras_escolhidas:
    print("Você escolheu uma letra que já tinha tentado. \nTente novamente!")
    letra = input("\n\nQual letra você quer escolher? ")

letras_escolhidas.append(letra)

if letra in palavra:
  print("MUITO BEM, MISERAVI... Você acertou a letra dessa bagaceira!")
  for i in range(len(palavra)):
      if letra == palavra[i]:
        estado_atual[i] = letra
      else:
        print("Aí não, meu jovem... Você ERROOOUUU!")
        tentativas = tentativas + 1

      # Quantas tentativas o miseravi já tem...
      print("Você já fez", tentativas,"tentativas erradas e ainda tem", chances-tentativas, "tentativas.")
      
      # Qual o estado atual da palavra
      print("Esse é o estado atual: ")
      print(estado_atual)
      
      # Quais as letras que o MISERAVI já tentou...
      print("As letras que você já tentou são: ")
      for item in letras_escolhidas:
          print(item, end=" ")

      # Fazer um final para o Joguinho
      if tentativas == chances:
          print("\n\nVocê perdeu...")
          print("\n\nAcabaram suas tentativas...")
      else:
        print("\n\nVocê ganhou!")
    
      print("A palavra era", palavra)
