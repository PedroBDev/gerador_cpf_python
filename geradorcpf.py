import random
#primeiro código github

def gerador_cpf():
    # Gerando 9 números aleatórios
    numeros_conta = []
    while len(numeros_conta) < 9:
        cpf = random.randint(0, 9)
        numeros_conta.append(cpf)

    # Calculando o primeiro dígito verificador
    multiplicador = 10
    soma = 0
    for a in numeros_conta:
        soma += a * multiplicador
        multiplicador -= 1

    digito_1 = (soma * 10) % 11
    digito_1 = digito_1 if digito_1 < 10 else 0

    # Adicionando o primeiro dígito à lista
    numeros_conta.append(digito_1)

    # Calculando o segundo dígito verificador
    multiplicador_2 = 11
    soma_2 = 0
    for a in numeros_conta:
        soma_2 += a * multiplicador_2
        multiplicador_2 -= 1

    digito_2 = (soma_2 * 10) % 11
    digito_2 = digito_2 if digito_2 < 10 else 0

    # Adicionando o segundo dígito à lista
    numeros_conta.append(digito_2)

    # Convertendo a lista de números em uma string formatada
    cpf_gerado = ''.join(map(str, numeros_conta))
    cpf_formatado = f"{cpf_gerado[:3]}.{cpf_gerado[3:6]}.{cpf_gerado[6:9]}-{cpf_gerado[9:]}"

    print('Aqui está o CPF gerado:', cpf_formatado)


#início do programa
print("BEM VINDO AO GERADOR DE CPF'S")
print('-'*30)

qtd= input("Digite quantos cpf's você quer gerar:")

#Verificando se o usuário digitou um número
try:
    qtd = int(qtd)
    if qtd <= 0:
        raise ValueError("Digite um número positivo.")
except ValueError:
    print('Você não digitou um número válido.')

#Início do gerador
for _ in range(qtd):    
    gerador_cpf()