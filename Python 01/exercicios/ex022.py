nome = str(input ('Qual seu nome Completo: '))
print('Analisando seu nome...')
print('Seu nome em Maiúscula é {}'.format(nome.upper()))
print('Seu nome em minusculo é {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras'.format(len(nome) - nome.count(' ')))
print('Sei primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split() # Este é igual o de cima menor
print('Seu primeiro nome é {} letras'.format(separa[0], len(separa[0])))


