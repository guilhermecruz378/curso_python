"""lista = ['Maria', 'Pedro', 'Pompom']

for indice in range(0, len(lista)):
    print(f'{lista[indice]}, Esta no indicie: {indice}')
"""

lista = ['Maria', 'Pedro', 'Pompom']


indices = range(len(lista))
for indice in indices:
    print(indice, lista[indice], type(lista[indice]))