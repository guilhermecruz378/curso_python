#while/else
# O else pode ser usado com o while fazendo parte do código por exemplo.
# Quando chega no final do código execute tal coisa.

strig = 'Valor qualquer'
i = 0
while i < len(strig):
    letra = strig[i]
    print(letra)
    i += 1

    if letra == ' ': #Quando chegar aqui ele não executará o else.
        break

else:
    print('O else foi executado.')
print('fora do bloco')