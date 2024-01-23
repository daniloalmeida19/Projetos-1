n = int(input('Digite um numero: '))
a = n - 1
s = n + 1
print('analisando o valor {}, seu antecessor é {} e o sucessor {}.' .format(n,a,s))

#este modelo são iguais mais diferentes formatos
n = int(input('Digite um numero: '))
print('analisando o valor {}, seu antecessor é {} e o sucessor {}.' .format(n, (n-1), (n+1)))