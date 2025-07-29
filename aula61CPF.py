#CPF: 746.824.890-70

cpf = '746.824.890'

cpf_sem_ponto = cpf.split('.')

cpf_junto = ''.join(cpf_sem_ponto)

cpf_numerico = int(cpf_junto)

soma = 0
contador = 10
for num in cpf_junto:
    soma += int(num) * contador
    contador -=1


total = soma * 10
if total % 11 < 9:
    digito = total % 11
    print('O primeiro digito é ', digito)
elif total % 11 > 9:
    digito = 0
    print('O primeiro digito é ', digito)
else:
    print('Erro')