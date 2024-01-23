# este é para ver o menor valor e maior
a = int(input("Primeiro Valor: "))
b = int(input("Segundo Valor: "))
c = int(input("Terceiro Valor: "))
# Verificando quem é menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#verificando quem é maior
#este and é for em python
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))