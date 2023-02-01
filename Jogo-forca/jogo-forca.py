import random


def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra] # A "List Comprehensions" é para colocar o traço de acordo com a palavra secreta


 #  ABERTURA
def jogar():
    #chamar mensagem
    imprimir_mensagem_abertura()

    #chamar as codigo da palavra secreta
    palavra_secreta = carrega_palavra_secreta()

    #
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)
    print(letras_acertadas)

    enforcou = False
    acertou = False
    erros = 0

    while (not enforcou and not acertou):
        chute = pedir_chute()

        if(chute in palavra_secreta):
            marca_chute_correto(chute, letras_acertadas, palavra_secreta)
        else:
            erros += 1
            desenha_forca(erros)
        
        enforcou = erros == 7
        acertou = "_" not in letras_acertadas # para parar o jogo quando acertar tudo.

        print(letras_acertadas)
    
    if(acertou):
        imprime_mensagem_vencedor()
    else:
        imprime_mensagem_perdedor(palavra_secreta)



#Mensagem de abertura do jogo
def imprimir_mensagem_abertura():
    print("*****************************")
    print("Bemvindo ao jogo de Forca!")
    print("*****************************")


# Desenho da forca
def desenha_forca(erros):
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    if(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    if(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    if(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    if(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    if(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    if (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()




#       MENSAGENS DO JOGO
# mensagem da vitoria
def imprime_mensagem_vencedor():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")


#Mensagem de Gamer over
def imprime_mensagem_perdedor(palavra_secreta):
    print("GAMER OVER! Tente novamente.")
    print("A palavra era secreta era: {}".format(palavra_secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")


# Codigo para pedir o chute do usuario
def pedir_chute():
    chute = input("Digite uma letra de A - Z:")
    chute = chute.strip().upper() #tratamento de espaços e letras maiusculas
    return chute

# Comparação da entrada de dados do usuario com a palavra secreta do jogo
def marca_chute_correto(chute, letras_acertadas, palavra_secreta):
    index = 0
    for letra in palavra_secreta:
        if(chute == letra):
            letras_acertadas[index] = letra
        index += 1

# Codigo da palavra secreta
def carrega_palavra_secreta():
    arquivo = open("palavras.txt", "r") #para abrir o arquivo de texto com as palavras e o "r" para ler
    palavras = []

    for linha in arquivo:
        linha = linha.strip() #para tirar o /n que vai ter no final
        palavras.append(linha)
        
    arquivo.close() # sempre fechar

    #para pelar as palavras aleatoriamente
    # O "upper" irá colocar a letras em maiusculas
    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper() 
    return palavra_secreta # para poder existir fora do bloco


if(__name__ == "__main__"):
    jogar()






