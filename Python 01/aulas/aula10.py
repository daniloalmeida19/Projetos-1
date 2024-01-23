# chamado: Condição
# se carro.esquerda ()= bloco_v_
# senão bloco_f_
# if carro.esquerda (): = bloco True - Verdade = o if é SE
# else: bloco False - falso = E O ELSE É SENÃO

tempo = int(input('Quantos anos tem seu carro? '))
if tempo<=3:
    print('carro novo')
else:
    print('carro velho')           
print('--FIM--')  

tempo = int(input('Quantos anos tem seu carro? '))
print('carro novo' if tempo<=3 else'carro velho')
print('--FIM--')

# agora o de baixo é outro jeito de fazer

nome = str(input('Qual é seu nome? ')).upper().strip()
if nome == 'Danilo': #este é para esquerda ou se
    print('Que Nome Lindo vc tem! ')
else: # Este é para direita ou senão
    print('Seu Nome é tão normal! ')    
print('Bom dia {}!'.format(nome))

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a Segunda Nota: '))
m = (n1 + n2) / 2
print('S sua média foi {:.1f}'.format(m))
if m >= 6.0:
    print('Sua Média foi boa! PARABÉNS! ')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')    
    

    