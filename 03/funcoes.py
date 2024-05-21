# 3) Desenvolva uma função que receba um número inteiro e positivo N e retorne a soma dos N
# números inteiros existentes entre o número 1 e esse número.

def somar_intervalo(x: int ) -> int:
    num = 0

    for i in range( 1, x+1):
        num+=i

    return num


