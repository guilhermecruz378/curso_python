# par ou impar

'''numero = input('Digite um número para saber se é par ou impar: ')

try:
    numero_int = int(numero) 
    par_ou_impar = numero_int % 2 == 0
    par_ou_impar_texto = 'impar'

    if par_ou_impar:
        par_ou_impar_texto = 'Par'
        print(f'o número {numero_int} é {par_ou_impar_texto}')
    
    else:
        print(f'O número {numero_int} é {par_ou_impar_texto}')

except:
    print('Digite um valor')'''

# hora da saudação 

'''q_horas = input('Que horas são? ')

q_horas_int = int(q_horas)
bom_dia = q_horas_int >= 0 and q_horas_int <= 11
boa_tarde = q_horas_int >= 12 and q_horas_int <= 17
boa_noite = q_horas_int >= 18 and q_horas_int <= 23

try: 

    if bom_dia:
        print('Olá Bom dia!')
    elif boa_tarde:
        print('Boa tarde!')
    else :
        print('Boa noite!')
    
except: 
    print('Digite um número inteiro!')'''

nome = input('Digite seu nome: ')

nome_fat = len(nome)
print(f'Seu nome é {nome} e ele tem {nome_fat}Letras')

if nome_fat <= 4:
    print('Seu nome é curto')
elif nome_fat >= 5 and nome_fat <= 6:
    print('Seu nome é normal')
else:
    print('Seu nome é grande')

