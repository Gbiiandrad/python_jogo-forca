def jogar():
    print("*****************************")
    print("Bemvindo ao jogo de Forca!")
    print("*****************************")

    palavra_secreta = "banana"
    letras_acertadas = ["_", "_","_", "_","_", "_"]

    enforcou = False
    acertou = False

    print(letras_acertadas)

    while (not enforcou and not acertou):

        chute = input("Digite uma letra de A - Z:")
        chute = chute.strip() #tratamento de espaços

        index = 0

        # O "upper" irá colocar a letras em maiusculas
        for letra in palavra_secreta:
            if(chute.upper() == letra.upper()):
                letras_acertadas[index] = letra
            index = index + 1

        print(letras_acertadas)

    #tratrando a entrada de letras maiusculas e minúsculas
        


    print("Fim de jogo.")

if(__name__ == "__main__"):
    jogar()
