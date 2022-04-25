boletim = []
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    boletim.append([nome, [nota1, nota2], media])
    quest = input('Quer continuar? [S/N] ').upper()
    status = ''
    if quest == 'N':
        break
for pos,c in enumerate(boletim):
    print(f'{pos+1} - Nome: {c[0]} ->> Média: {c[2]}')
    if c[2] > 6:
       print('Aprovado')
    else:
        print('Reprovado')