frase = '  olha só que   , coisa interssante  '
listas_frases_cruas = frase.split(',')

listas_frase = []
for i, frases in enumerate(listas_frases_cruas):
    listas_frase.append(listas_frases_cruas[i].strip())

print(listas_frase)


frases_unidas = '-'.join('abcdefg')
print(frases_unidas)