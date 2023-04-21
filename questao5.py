#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

str = input('Esvreva a frase que deseja inverter: ')
rts = ''
for i in range(len(str)-1, -1, -1):
    rts += str[i]

print(f'a frase invertida fica: {rts}')