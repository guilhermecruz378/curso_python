"""
#iteravel é um elemento que pode te entregar uma coisa por vez.
iterável -> str, range, etc (ele tem um metodo dentro dele
chamado de __iter__)
iterador -> É quem sabe entregar um valor por vez.
next -> Me entrega o proxímo valor.
iter -> Me entrega seu iterador.
"""



"""'''
#texto = iter('Guilherme') # __iter__() # entrega o objeto  iterador

'''print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(texto.__next__())
print(next(texto))"""

# for letra in texto
texto = 'Guilherme' # iterável
iterador = iter(texto) # iterador

while True:
    try:
        letra = next(iterador)
        print(letra)
    except StopIteration:
        break