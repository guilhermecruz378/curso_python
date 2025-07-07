lista = ['maria', 'joao','matias']
lista.append('Neuza')

#lista_enumerada = list(enumerate(lista))
#print(lista_enumerada)

lista_enumerada = enumerate(lista)

# for item in lista_enumerada:
#     indicie, valor = item
#     print(indicie, valor)

# for indicie, valor in lista_enumerada:# isso é como se fosse um for dentro de um for
#     print(indicie, valor)

for Tupla_enumerada in lista_enumerada:
    print('For da Tupla: ')
    for valor in Tupla_enumerada:
            print(f'\t{valor}')