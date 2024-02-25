altura = float(input('digite aqui sua altura: '))
peso = float(input('digite aqui seu peso: '))
idade = int(input('digite aqui sua idade: '))

imc = peso / (altura*altura)
print(f"O seu imc é: {imc:.2f}")