import os 
palavra_secreta = 'cavaleiro'
letras_acertadas = ''
tentativas = 0 

while True:
    letra_usuario = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_usuario) > 1:
        print('Digite apenas uma letra')
        continue

    if tentativas >= 2:
        os.system('clear')
        tentativas = 0
        print('Você excediu suas tentativas: max12')

    if letra_usuario in palavra_secreta:
        letras_acertadas += letra_usuario
        
    palavra_formada =''
    for letra_secreta in palavra_secreta:
        if letra_secreta in letras_acertadas:
             palavra_formada += letra_secreta
        else: 
             palavra_formada += '*'

    print(palavra_formada)

    if palavra_formada == palavra_secreta:
        os.system('clear')
        print(f'Você ganhou a palavra secreta é: {palavra_secreta}')
        print(f'Tentativas: {tentativas}')
        letras_acertadas = ''
        tentativas = 0 
