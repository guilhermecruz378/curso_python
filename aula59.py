#Desempacotamento em chamadas 
#De métodos e funções
string = 'ABCD'
lista = ['maria', 'Helena', 1, 2, 3, 'Eduarda']
tupla = ('python', 'é', 'legal')

salas = [
    # 0        1
    ['Maria', 'Helena', ],  # 0
    # 0
    ['Elaine', ],  # 1
    # 0       1       2
    ['Luiz', 'João', 'Eduarda', ],  # 2
]

# p, b, *_, antepenultimo, ultimo = lista
# print(p,ultimo, antepenultimo)

# print('maria', 'Helena', 1, 2, 3, 'Eduarda')
# print(*lista)
print(*string)
# print(*tupla)

print(*salas, end='\n')
print('-='*10)
print(*salas, sep='\n')