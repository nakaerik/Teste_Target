#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json
with open("dados.json") as tabela:
    dados = json.load(tabela)

faturamento = dados["dados"]
maior = float('-inf')
menor = float('inf')
total = 0
count = 0

for item in faturamento:
    dia = item['dia']
    valor = item['valor']
    if valor < menor and valor != 0:
        menor = valor

    if valor > maior:
        maior = valor

    total = total + valor
    count = count + 1

print(f'O Menor Valor faturado foi de {menor}')
print(f'O Maior Valor faturado foi de {maior}')

media = total / count
acima = 0

for item in faturamento:
    valor2 = item['valor']
   
    if valor2 > media:
        acima = acima + 1

print(f'O numero de dias acima da média foi de: {acima}')






