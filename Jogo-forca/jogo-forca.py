import random

def inicializa_letras_acertadas(palavra):
    return ["_" for letra in palavra] # A "List Comprehensions" é para colocar o traço de acordo com a palavra secreta

def jogar():
    #chamar mensagem
    imprimir_mensagem_abertura()

    #chamar as codigo da palavra secreta
    palavra_secreta = carrega_palavra_secreta()

    #
    letras_acertadas = inicializa_letras_acertadas(palavra_secreta)

    #


    enforcou = False
    acertou = False
    tentativas = 0

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Digite uma letra de A - Z:")
        chute = chute.strip().upper() #tratamento de espaços e letras maiusculas

        if(chute in palavra_secreta):
            index = 0

            for letra in palavra_secreta:
                if(chute == letra):
                    letras_acertadas[index] = letra
                index += 1
        else:
            tentativas += 1
        
        enforcou = tentativas == 6
        acertou = "_" not in letras_acertadas # para parar o jogo quando acertar tudo.

        print(letras_acertadas)
    
    if(acertou):
        print("PARABENS você acertou!")
    else:
        print("GAMER OVER! Tente novamente.")
        print("A palavra era secreta era: {}".format(palavra_secreta))


    print("Fim de jogo.")





def imprimir_mensagem_abertura():
    print("*****************************")
    print("Bemvindo ao jogo de Forca!")
    print("*****************************")

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


