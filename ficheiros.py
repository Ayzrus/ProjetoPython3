import os.path

path = 'Ficheiros/teste.txt'

check_file = os.path.isfile(path)

dados = {
    "DadosFicheiro1": []
}

if check_file:
    f = open("Ficheiros/teste.txt", "a")
    f.write(input('Digite algo\n') + "\n")
    f.write(input('Digite algo\n') + "\n")
    f.write(input('Digite algo\n') + "\n")
    f.write(input('Digite algo\n') + "\n")
    f.write(input('Digite algo\n') + "\n")
    f.write(input('Digite algo\n') + "\n")
    f.write(input('Digite algo\n') + "\n")
    f.write(input('Digite algo\n') + "\n")
    f.write(input('Digite algo\n') + "\n")
    f.write(input('Digite algo\n'))
    f = open("Ficheiros/teste.txt", "r")
    i = 0
    for x in f:
        dados["DadosFicheiro1"].append({
            i: x
        })
        i += 1
    f.close()
    print(dados["DadosFicheiro1"])
else:
    print(check_file)
    new = open("Ficheiros/teste.txt", "x")
