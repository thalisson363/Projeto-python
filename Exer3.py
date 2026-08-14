#Calculo de aposentadoria.

from datetime import date
#Ano atual
ano_atual = date.today().year
dados = {}

dados['nome'] = str(input('Nome: '))
dados['nascimento'] = int(input('Ano de nascimento: '))

idade = ano_atual - dados['nascimento']

dados['carteira'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['carteira'] !=0:
    dados['contrataçao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salario: '))

    print(f'Nome: {dados["nome"]}')
    print(f'Idade: {idade}')
    print(f'CTPS: {dados["carteira"]}')
    print(f'Ano de contratação: {dados["contrataçao"]}')

    #Calculo
    aposento = dados['contrataçao'] - dados['nascimento'] + 35

    print(f'Salario: {dados["salario"]}')
    print(f'Idade de aposentadoria: {aposento}')


else:
  print(f'Nome: {dados["nome"]}')
  print(f'Idade: {idade}')
  print(f'CTPS: {dados["carteira"]}')


