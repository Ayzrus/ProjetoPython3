z = []
x = 1
iva = float(1.23)
res = ''
while x != 0:
    x = int(input('Digite 1 para registar produto \nDigite 2 para listar: \nDigite 0 para sair: \n'))
    if x == 1:
        y = str(input('Digite o nome do produto: '))
        r = str(input('Digite a referencia do produto: '))
        u = float(input('O preço do produto: '))
        z.append({
            1: y,
            2: u,
            3: r
        })
    elif x == 2:
        for h in z:
            res = h[2] * iva
            print('Nome do produto: ' + h[1])
            print('Preço sem iva: ' + str(h[2]))
            print('Preço com iva: ' + str(res))
            print('Referencia: ' + h[3])
    elif x == 0:
        break
    else:
        print('erro insira uma opção valida!')
