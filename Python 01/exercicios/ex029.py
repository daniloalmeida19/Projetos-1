velocidade = float(input('Qual é a vcelocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade-80) * 7
    print('Você devepagar uma multa de R$ {:.2f}!'.format(multa))
print('Tenha um Bom Dia! Dirija com Segurança!:')

# não precisa do else por ser condição simples




