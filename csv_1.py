import csv
op = 12938129831
while op != 0:
    op = str(input(
        'Digite 1 para registar Clientes\nDigite 2 para listar clientes\n'
        'Digite 3 para registar produtos\nDigite 4 para listar produtos\n'
        'Digite 5 para fazer orcamento\nDigite 6 para listar orcamento\nDigite 0 para sair\n'))
    if op == '1':
        with open('Ficheiros/clientes.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([input('Digite o seu nome \n'), input(
                'Digite seu nif \n'), input('Digite sua morada \n'), input('Digite seu Telefone \n'), input('Digite seu email \n')])
    elif op == '2':
        with open('Ficheiros/clientes.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    elif op == '3':
        with open('Ficheiros/Produtos.csv', 'a+', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([input('Digite o nome do produto\n'), input('Digite a referencia do produto \n'), input('Digite o preço sem iva do produto \n')])
    elif op == '4':
        with open('Ficheiros/Produtos.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    elif op == '5':
        ref = str(input('Insira a referencia do produto\n'))
        nif = str(input('Insira o nif do cliente\n'))
        with open('Ficheiros/Produtos.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[1] == ref:
                    iva = 1.23
                    preco = float(row[2])
                    print('Preço sem iva: ' + row[2])
                    print('Preço Com Iva: ' + str(preco * iva))
                    with open('Ficheiros/clientes.csv', 'r') as file:
                        reader2 = csv.reader(file)
                        for row2 in reader2:
                            if row2[1] == nif:
                                print('Cliente: ' + row2[0])
                                with open('Ficheiros/Orcamentos.csv', 'a+', newline='') as file:
                                    writer = csv.writer(file)
                                    writer.writerow([nif, ref, preco, str(preco * iva)])
    elif op == '6':
        with open('Ficheiros/Orcamentos.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
    elif op == '0':
        break
    else:
        print('erro opção invalida')
