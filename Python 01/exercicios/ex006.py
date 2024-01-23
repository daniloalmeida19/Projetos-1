n = int(input('Digite um Numero:'))
d = n * 2
t = n * 3
r = n ** (1/2)
print('O doblo de {} vale {}.'.format(n, d))
print('O triplo de {}vale {}. \nA Raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, r))

#este são 2 modelos iguais mais com diferenças

n = int(input('Digite outro Numero:'))
print('O doblo de {} vale {}.'.format(n, d))
print('O triplo de {}vale {}. \nA Raiz quadrada de {} é igual a {:.2f}.'.format(n, (n*3), n, pow(n,(1/2))))


