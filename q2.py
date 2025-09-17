peso = [85, 92, 68, 126]
altura = [1.90, 1.73, 1.70, 2]
pessoas = ['Pedro', 'Sérgio', 'Douglas', 'Emesson']

for i in range(len(peso)):
    imc = peso[i] / (altura[i] ** 2)

    if imc <= 18.49:
        print(f'O IMC de {pessoas[i]} é {imc:.2f}, logo ele está abaixo do peso.')
    elif 24.99 > imc > 18.5:
        print(f'O IMC de {pessoas[i]} é {imc:.2f}, logo ele está no peso recomendado.')
    elif 29.99 > imc > 25:
        print(f'O IMC de {pessoas[i]} é {imc:.2f}, logo ele está acima do peso.')
    else:
        print(f'O IMC de {pessoas[i]} é {imc:.2f}, logo ele está obeso.')