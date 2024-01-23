distancia = float(input('Qual é a Distancia da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km.'.format(distancia))
if distancia <= 200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print('E o preço da sua passagem será de R$ {:.2f}'.format(preço))  

# ou este de baixo

distancia = float(input('A Distancia deste novo vai ser o mesmo: '))
print('Voce vai percorrer esta distancia {}'.format(distancia))
preço = distancia * 0.50 if distancia<=200 else distancia * 0.45
print('E o preço da sua passagem vai ser R$ {:.2f}'.format(preço))    

