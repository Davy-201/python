contador = 1
soma = 0

while(contador <= 5):
    idade = int(input(f'digite a idade do usuario {contador}'))
    soma = soma + idade
    contador += 1

media = soma/(contador-1)
print(f'a media das idades é: {media}')