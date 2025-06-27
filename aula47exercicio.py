palavra_secreta = 's'
print('-- VAMOS JOGAR O JOGO DA ADIVINHAÇÃO -----')
while True:
    print('A dica é... Apenas uma letra minuscula.')
    digit = input('Digite a palavra secreta: ')
    converge = None

    try:
        digit_str = str(digit)
        converge = True
    except:
        converge = None

    if converge == None:
        print('Ocorreu um problema na sua digitação!')
        print('Para facilitar digite apenas letras')
        continue

    tamanho_digit = len(digit_str)
    tamanho_secret = len(palavra_secreta)
    if tamanho_digit > tamanho_secret:
        print('O tamanho de sua palavra está errado, tente uma palavra é MENOR!')
        continue
    elif tamanho_digit < tamanho_secret:
        print('O tamanho de sua palavra está errado, tente uma palavra é MAIOR!')
        continue

    if digit_str != palavra_secreta:
        print('Você errou tente mais uma vez!')
        continue

    if digit == 's':
        print(f'\033;32;40[mA letra correta é "{palavra_secreta}" Você acertou!\033[m')
        break
