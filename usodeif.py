idade = int(input('digite sua idade: '))
if (idade >= 18): print ('você é maior de idade')
if (idade < 18): print ('você é menor de idade')

print('Responda a pergunta a seguir com sim ou não')
resposta = input('Seu time venceu a ultima partida que disputou ?')

if ((resposta == 'Sim') or (resposta == 'sim')):
    print ('Que ótima notícia para você')
else:
    print('Que pena')