"""
Interpolação de strings é usado com o simbolo de %
s - string
d e i - int
f - float
x e X - Hexadecimal (ABCDEF0123456789)

"""

nome = 'Guilherme'
preco = 64410.4857575
variavel = 'Sr %s, o preço da sua divida é no valor de %.2f' % (nome, preco)
print(variavel)
print('O Hexadecimal de %d é %08x'%(1500, 1500))
