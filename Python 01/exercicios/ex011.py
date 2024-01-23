larg = float(input('Largura da Parede: '))
alt = float(input('Altura da Parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {} m2.'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))