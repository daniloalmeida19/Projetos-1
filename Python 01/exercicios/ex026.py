frase = str(input('Digite uma frase: ')).upper().strip()
print('A letra A aparece {} vezes na frase.' .format(frase.count('A')))
print('Em que Posição {} aparece a primeira vez.'.format(frase.find('A')+1))
print('Em que posiçao {} ela aprece a ultima vez.' .format(frase.rfind('A')+1))


