pesos = [90, 90, 91, 90, 93, 90, 89, 90, 87, 90, 85, 91, 90, 90, 86]
recomendado = 90
cont = 0

fora_do_recomendado = []

for peso in pesos:
    diff = abs(recomendado - peso)
    cont += 1

    if diff > 2:
        fora_do_recomendado.append(cont - 1)

print(f'Os produtos que estão fora do peso recomendado são: {fora_do_recomendado}')