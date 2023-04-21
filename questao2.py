# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.
#
# IMPORTANTE:
# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;
import json


def fib(num):

    a = 0
    b = 1
    while (b < num):
        a, b = b, a + b

    if b == num:
        return True

    else:
        return False


num = int(input('digite um numero: '))

if fib(num):
    print(f'O numero {num} pertence a sequencia')
else:
    print(f'O numero {num} não pertence a sequencia')






