#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53
total = sp + rj + mg + es + outros
print(f'O faturamento total foi de: {total}')
psp = (100 * sp)/total
print(f'o Faturamento em porcentagem de sp foi de: {psp:.2f}%')
prj = (100 * rj)/total
print(f'o Faturamento em porcentagem de rj foi de: {prj:.2f}%')
pmg = (100 * mg)/total
print(f'o Faturamento em porcentagem de mg foi de: {pmg:.2f}%')
pes = (100 *es)/total
print(f'o Faturamento em porcentagem de es foi de: {pes:.2f}%')
poutros = (100 * outros)/total
print(f'o Faturamento em porcentagem de outros foi de: {poutros:.2f}%')

