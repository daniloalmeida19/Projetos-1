print('-='*20)
print('Analisador de Triangulos')
print('-='*20)
r1 = float(input('primeiro Segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR Triângulo! ')
else:
    print('Os segmentos acima NÃO PODEM FORMAR Triângulo')
    