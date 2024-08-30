import csv
csv.rea
x = float(input('Introduza a primeiro nota: '))

y = float(input('Introduza a segunda nota: '))

z = float(input('Introduza a terceira nota: '))

res = (x + y + z) / 3

if res >= 9.5:
    print('O aluno foi aprovado com uma media de: ' + str(round(res, 2)))
else:
    print('O aluno foi reprovado com uma media de: ' + str(round(res, 2)))

