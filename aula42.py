# Qual letra apareceu mais vezes na frase
frase = 'O Python é uma linguagem de programação' \
        ' multiparadigma' \
        ' Python foi criado por Guido van Rossum.'

i = 0
mais_vezes_quantidade = 0
mais_vezes_letra = ''
while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue
    
    qtd_atual = frase.count(letra_atual)

    if mais_vezes_quantidade <= qtd_atual:
        mais_vezes_quantidade = qtd_atual
        mais_vezes_letra = letra_atual
    
    i += 1
print(f'A letra que apareceu mais vezes foi a letra "{mais_vezes_letra}" ela apareceu {mais_vezes_quantidade} x')
print('Fim!')
