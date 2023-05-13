import random


class JuegoAhorcado:
    Estados = [
        r"""
     +--+
     |  |
        |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
        |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
     |  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|  |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
        |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    /   |
        |
    =====""",
        r"""
     +--+
     |  |
     O  |
    /|\ |
    / \ |
        |
    ====="""]

    Salvado = [
        r"""
     +--+
        |
        |
    \O/ |
     |  |
    / \ |
    ====="""]

    categorias = ['FRUTAS', 'PAISES', 'ANIMALES']
    opciones = {
        'FRUTAS': 'PERA PLATANO UVA MANZANA MELOCOTON KIWI ALBARICOQUE CEREZA CIRUELA FRESA GRANADA HIGO LIMA LIMON '
                  'MANDARINA NARANJA MELON MORA NISPERO PIÑA POMELO SANDIA'.split(),
        'PAISES': 'ALEMANIA ARGENTINA AUSTRALIA BRASIL CANADA CHINA COLOMBIA ESPAÑA FRANCIA INDIA ITALIA JAPON MEXICO '
                  'RUSIA SUDAFRICA SUECIA TURQUIA'.split(),
        'ANIMALES': 'LEON TIGRE ELEFANTE CANGURO JIRAFA PINGÜINO LOBO SERPIENTE RINOCERONTE CAMALEON MURCIELAGO '
                    'COCODRILO DROMEDARIO PANTERA HORMIGA ESCORPION'.split()
    }

    def obtener_intentos_restantes(self, intentos):
        return len(self.Estados) - 1 - len(intentos)

    def jugar(self):

        intentos = []
        letra_correcta = []
        categoria = random.choice(self.categorias)
        PalabraSecreta = random.choice(self.opciones[categoria])

        while True:
            self.dibujar(intentos, letra_correcta, PalabraSecreta, categoria)

            nueva_letra = self.dame_letra(intentos + letra_correcta)

            if nueva_letra == "TERMINAR":
                print(self.Estados[6])
                print('Has decidido terminar el juego.')
                print('La palabra era "{}"'.format(PalabraSecreta))
                break

            if nueva_letra in PalabraSecreta:
                letra_correcta.append(nueva_letra)
                puedeGanar = True
                for sin_intentos in PalabraSecreta:
                    if sin_intentos not in letra_correcta:
                        puedeGanar = False
                        break
                if puedeGanar:
                    print(self.Salvado[0])
                    print('¡Bien hecho! la palabra secreta es :', PalabraSecreta)
                    print('Has ganado!,', nombre)
                    break
            else:
                intentos.append(nueva_letra)

            if len(intentos) == len(self.Estados) - 1:
                self.dibujar(intentos, letra_correcta, PalabraSecreta, categoria)
                print('Demasiados intentos!')
                print('La palabra era "{}"'.format(PalabraSecreta))
                break

    def dibujar(self, intentos, letra, palabra_secreta, categoria):
        print(self.Estados[len(intentos)])
        print('La categoría es: ', categoria)
        intentos_restantes = self.obtener_intentos_restantes(intentos)
        print('Intentos restantes:', intentos_restantes)
        print('Letras incorrectas: ', end='')

        for let in intentos:
            print(let, end=' ')
        if len(intentos) == 0 and 0 == len(intentos):
            print('No hay letras incorrectas.')
        if len(intentos) == len(intentos) + 1:
            print('Letras diferentes.')
        if len(intentos) == len(intentos) + 2:
            print('No coinciden.')

        print()

        espacios = ['_'] * len(palabra_secreta)

        for i in range(len(palabra_secreta)):
            if palabra_secreta[i] in letra:
                espacios[i] = palabra_secreta[i]

        print(' '.join(espacios))

    @staticmethod
    def dame_letra(letra):
        while True:
            adivina = input('Adivina una letra.\n> ').upper()
            if adivina == "TERMINAR":
                return adivina
            if len(adivina) != 1:
                print('Introduce una única letra.')
            elif adivina in letra:
                print('Esa letra ya la sabías. Elige otra vez.')
            elif not adivina.isalpha():
                print('Introduce una LETRA.')
            else:
                return adivina


if __name__ == '__main__':
    nombre = input("Dime tu nombre:")
    JuegoAhorcado().jugar()
