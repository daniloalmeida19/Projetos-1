n = str(input('Digite seu nome completo: ')).strip() #o strip para eliminar os espaços
nome = n.split() # este split vai fatiar os nomes em espaços
print('Muito prazer em te conhecer! ')
print('Seu primeiro nome é {}'.format(nome[0])) #este 0 serve para posição
print('Seu ultimo nome é {}'.format(nome[len(nome)-1])) # Este len e o terceiro é a posição do bloco