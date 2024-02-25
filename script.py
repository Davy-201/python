altura = input('digite aqui: ')
peso = input('digite aqui: ')
idade = input('digite aqui: ')

altura = float(altura)
peso = float(peso)
idade = int(idade)

imc = peso / (altura*altura)
print(imc)