import csv
import os.path
op = 12938129831

path = 'Ficheiros/Animais.csv'

path2 = 'Ficheiros/Medicacao.csv'

path3 = 'Ficheiros/Consulta.csv'

check_file = os.path.isfile(path)

check_file2 = os.path.isfile(path2)

check_file3 = os.path.isfile(path3)

if check_file and check_file2 and check_file3:
    while op != 0:

        op = str(input(
            'Insira 1 para registar Animal\nInsira 2 para listar Animais\n'
            'Insira 3 para registar Consulta\nInsira 4 para listar Consultas\n'
            'Insira 5 para registrar Medicamentos\nInsira 6 para listar Medicamentos\nInsira 0 para sair\n'))
        if op == '1':
            with open('Ficheiros/Animais.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([input('Digite o NChip do seu Animal \n'), input(
                    'Digite o nome do seu Animal \n'), input('Digite Espécie do seu Animal \n'), input('Digite o Ano de Nascimento do seu Animal \n')])
        elif op == '2':
            with open('Ficheiros/Animais.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        elif op == '3':
            data = input('Digite a Data da consulta \n')
            medico = input('Digite o nome do Medico \n')
            nchip = input('Digite o Nchip \n')
            codmedicamento = input('Digite o codigo do medicamento \n')
            codmedicamentos = []
            codmedicamentos.append(codmedicamento)
            with open('Ficheiros/Animais.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    if row[0] == nchip:
                        with open('Ficheiros/Medicacao.csv', 'r') as file:
                            reader2 = csv.reader(file)
                            for row2 in reader2:
                                if row2[0] == codmedicamento:
                                    opm = 2131321
                                    while opm != 0:
                                        opm = str(
                                            input('Digite 1 para registrar medicamentos ou digite 0 para sair\n'))
                                        if opm == '1':
                                            codmedicamentos.append(
                                                input('Digite os codigos dos medicamentos \n'))
                                        elif opm == '0':
                                            break
                                        continue
                                    with open('Ficheiros/Consulta.csv', 'a+', newline='') as file:
                                        writer = csv.writer(file)
                                        writer.writerow(
                                            [data, medico, nchip, codmedicamentos])
        elif op == '4':
            with open('Ficheiros/Consulta.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        elif op == '5':
            with open('Ficheiros/Medicacao.csv', 'a+', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([input('Digite o Cod do Medicamento \n'), input(
                    'Digite a descrição do medicamento \n'), input('Digite o Laboratório \n')])
        elif op == '6':
            with open('Ficheiros/Medicacao.csv', 'r') as file:
                reader = csv.reader(file)
                for row in reader:
                    print(row)
        elif op == '0':
            break
        else:
            print('erro opção invalida')
else:
    new = open("Ficheiros/Animais.csv", "x")
    new2 = open("Ficheiros/Medicacao.csv", "x")
    new3 = open("Ficheiros/Consulta.csv", "x")
    print('Os ficheiros não existem entao acabamos de criar!')
