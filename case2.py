notas = [7.5, 8.0, 6.5, 9.0, 8.5]
# Como faço para calcular a média dessas notas?
media = sum(notas) / len(notas)
print(media)
# Além disso, gostaria de saber como adicionar uma nova nota na lista e recalcular a média.
notas.append(10)
media = sum(notas) / len(notas)
print(media)
