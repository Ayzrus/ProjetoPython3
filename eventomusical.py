import os

clear = lambda: os.system('cls')

eventos = []

bandas = []

eventosBandas = []

publico = []

eventoPublico = []

idss = []

x = 1


def validarBanda(Nome, Codigo):
    debounce = True

    for b in bandas:
        if b[1] == Nome or b[2] == Codigo:
            debounce = False

    return debounce


while x != 0:
    x = str(input('Digite 1 para registar Eventos \nDigite 2 para registrar Bandas \nDigite 3 para registrar Uma '
                  'Banda num Evento \nDigite 4 para registrar Publico: \nDigite 5 para listar os Eventos com as bandas '
                  '\nDigite 6 para listar os Eventos com o publico \n'
                  'Digite 0 para sair: \n'))
    if x == '1':
        clear()
        eventos.append({
            1: str(input('Digite o Numero de registro: \n')),
            2: str(input('Digite o Local do Evento: \n')),
            3: str(input('Digite a Coordenada latitude: \n')),
            4: str(input('Digite a Coordenada latitude: \n')),
            5: str(input('Digite o Horário do Evento: \n')),
            6: str(input('Digite o Tipo do Evento: \n'))
        })
        clear()
    elif x == '2':
        clear()
        nome = str(input('Digite o Nome da Banda: \n'))

        codigo = str(input('Digite o Código da Banda: \n'))

        if validarBanda(nome, codigo):
            bandas.append({
                1: nome,
                2: codigo,
                3: str(input('Digite o Tipo da Banda: \n')),
            })
        else:
            print('Banda Inserida já existe!')
        clear()
    elif x == '3':
        clear()
        i = 0
        print('--- Lista de Eventos ---')
        while i < len(eventos):
            print('--- Codigo Do Evento: ' + str(eventos[i][1]) + ' Local do Evento: ' + str(eventos[i][2]) + ' ---')
            i += 1
        for e in eventos:
            opc = input('Digite um codigo de evento: \n')
            if opc == e[1]:
                for ba in bandas:
                    if e[6] == ba[3]:
                        print('Bandas disponíveis para serem adicionadas ao evento: Nome: ' + ba[1] + ' Codigo: '
                              + ba[2] + ' Tipo: ' + ba[3] + '.')
                        obc = input('Digite o nome da banda: \n')
                        eventosBandas.append({
                            1: opc,
                            2: obc
                        })
        clear()
    elif x == '4':
        clear()
        nome = str(input('Digite o Nome: \n'))
        publico.append({
            1: nome,
            2: str(input('Digite o Nif: \n')),
            3: str(input('Digite o Telefone: \n')),
            4: str(input('Digite o Email: \n')),
        })
        clear()
        i = 0

        id = []

        print('--- Lista de Eventos ---')
        while i < len(eventos):
            print(
                '--- Codigo Do Evento: ' + str(eventos[i][1]) + ' Local do Evento: ' + str(eventos[i][2]) + ' ---')
            id.append({
                1: eventos[i][1],
                2: eventos[i][2]
            })
            i += 1
        opce = input('Digite um codigo de evento: \n')
        oo = 0
        while oo < len(id):
            if opce == id[oo][1]:
                eventoPublico.append({
                    1: id[oo][1],
                    2: input('Digite o Nome da pessoa registrada: \n')
                })
                idss.append({
                    1: id[oo][1],
                    2: id[oo][2],
                    3: nome
                })
            oo += 1
        print(idss)
    elif x == '5':
        clear()
        i = 0
        j = 0
        ids = []
        while i < len(eventosBandas):
            while j < len(eventos):
                if eventosBandas[i][1] == eventos[j][1]:
                    print('Codigo do Evento:' + str(eventos[j][1]) + ' Nome da Banda: ' + str(eventosBandas[i][2])
                          + ' Local do Evento: ' + str(eventos[j][2]))
                    ids.append({
                        1: eventos[j][1],
                        2: eventos[j][2],
                        3: eventosBandas[i][2]
                    })
                j += 1
                break
            i += 1
        ope = str(input('Filtar por codigo de evento: \n'))
        clear()
        jj = 0
        while jj < len(ids):
            if ids[jj][1] == ope:
                print('Codigo do Evento:' + str(ids[jj][1]) + ' Nome da Banda: ' + str(ids[jj][3])
                      + ' Local do Evento: ' + str(ids[jj][2]))
            jj += 1
    elif x == '6':
        clear()
        i = 0
        j = 0
        k = 0

        ope = str(input('Filtar por codigo de evento: \n'))
        clear()
        jj = 0
        while jj < len(idss):
            if idss[jj][1] == ope:
                print('Codigo do Evento: ' + str(idss[jj][1]) + ' Nome Pessoa Publico: ' + str(idss[jj][3])
                      + ' Local do Evento: ' + str(idss[jj][2]))
                break
            jj += 1

    else:
        print(str('Digite uma opção valida do menu!'))
