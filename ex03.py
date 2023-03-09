numero_secreto = 42
tentativa = 1
while tentativa <= 3:
    palpite = int(input("Adivinhe o numero secreto: "))
    if palpite == numero_secreto:
       print("Parabéns, você acertou!")
       break
    else:
        if palpite > numero_secreto:
            print ("o número secreto é menor do que", palpite)
        else:
            print ("o número secreto é maior do que", palpite)
    tentativa += 1
    
    
    if tentativa > 3:
        print("Suas tentativas acabaram. O número secreto era", numero_secreto)
        