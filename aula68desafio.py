def multiplicador(*args):
    acumulador = 1
    for me_multiplica in args:
        acumulador *= me_multiplica
    return acumulador

multi = 1,2,3,4,5,6,7,8,9
multi_desempacotado = multiplicador(*multi)
print(multi_desempacotado)

print('-='*20)

# def par_ou_impar(x):
#     if x % 2 == 0:
#         return f"{x} é par!"
#     else:
#         return f"{x} é impar!"

def par_ou_impar(x):
    multiplo_de_dois = x % 2 == 0

    if multiplo_de_dois:
        return f"{x} é par!"
    return f"{x} é impar!"

print(par_ou_impar(98))