import os

animal = []


def clear(): return os.system('cls')


class Animais:

    # Construtor
    def __init__(self, Nchip, Nome, Especie, AnoNascimento):
        self.Nchip = Nchip
        self.Nome = Nome
        self.Especie = Especie
        self.AnoNascimento = AnoNascimento

    # Metodos
    def info(self) -> str:
        return (
            f"Numero Do Chip: {self.Nchip} Nome Do Animal: {self.Nome} Especie Do Animal: {self.Especie} Ano De Nascimento Do Animal: {self.AnoNascimento}")
    # Metodos Estaticos

op = 1

while op != 0:

    op = int(input('1 para registrar: \n2 para listar: \n'))

    if op == 1:
        dados = Animais(str(input('Digite o Nchip do animal: \n')),
                        str(input('Digite o Nome do animal: \n')),
                        str(input('Digite a Especie do animal: \n')),
                        str(input('Digite o Ano De Nascimento do animal: \n')))
        clear()

        animal.append(dados)

    elif op == 2:

        for an in animal:
            print(an.info())
