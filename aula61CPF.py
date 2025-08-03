#CPF: 746.824.890-70

# cpf = '746.824.890'
# cpf_sem_ponto = cpf.split('.')
# cpf_junto = ''.join(cpf_sem_ponto)

# soma = 0
# contador = 10
# for num in cpf_junto:
#     soma += int(num) * contador
#     contador -=1

# total = soma * 10
# if total % 11 < 9:
#     digito = total % 11
#     print('O primeiro digito é ', digito)
# elif total % 11 > 9:
#     digito = 0
#     print('O primeiro digito é ', digito)
# else:
#     print('Erro')

# cpf_enviado_pelo_usuario = '746.824.890-70' .replace('.','') \
#     .replace('-','')
import re
import sys

entrada = input('CPF[746.824.890-70]:')
cpf_enviado_pelo_usuario = re.sub(
    r'[^0-9]',
    '',
    entrada
)

entrada_sequencial = entrada == entrada[0] * len(entrada)

if entrada_sequencial:
    print('Você enviou dados sequenciais.')
    sys.exit()

nove_digitos = cpf_enviado_pelo_usuario[:9]
contador_regressivo_1 = 10

resultado_digito1 = 0
for digito in nove_digitos:
    resultado_digito1 += int(digito) * contador_regressivo_1
    contador_regressivo_1 -= 1
digito_1 = (resultado_digito1 * 10) % 11
digito_1 = digito_1 if digito_1 < 9 else 0
print(digito_1)

dez_digitos = nove_digitos + str(digito_1)
contador_regressivo_2 = 11

resultado_digito_2 = 0
for digito in dez_digitos:
    resultado_digito_2 += int(digito) * contador_regressivo_2
    contador_regressivo_2 -= 1
digito_2 = (resultado_digito_2 * 10) % 11
digito_2 = digito_2 if digito_2 < 9 else 0
print(digito_2)

cpf_gerado_pelo_calculo = f'{nove_digitos}{digito_1}{digito_2}'

if cpf_enviado_pelo_usuario == cpf_gerado_pelo_calculo:
    print(f'{cpf_enviado_pelo_usuario} é válido')
else:
    print('cpf inválido!')