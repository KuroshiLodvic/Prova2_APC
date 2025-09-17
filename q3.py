notas = [8, 6, 4, 9, 1, 7, 6, 8, 9, 3]
novas_notas = []
nota_max = nota_min = notas[1]

for nota in notas:
    if nota > nota_max:
        nota_max = nota
    elif nota < nota_min:
        nota_min = nota

for i in range(len(notas)):
    nota_nova = 10 * ((notas[i] - nota_min) / (nota_max - nota_min))
    novas_notas.append(nota_nova)

print(f'As novas notas ficaram assim: {novas_notas}')