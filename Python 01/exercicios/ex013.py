salário = float(input('Qual é o Salário do funcionario? R$ '))
novo = salário +  (salário * 15 / 100)
print('Um funcionario que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}' .format(salário, novo))

