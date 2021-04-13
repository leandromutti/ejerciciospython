def lencustom(cadena):
    cantidad = 0
    for letra in cadena:
        cantidad += 1

    return cantidad


def findcustom(palabra, caracterbusqueda):
    posicion = 0
    for caracter in palabra:
        posicion += 1
        if caracter == caracterbusqueda:
             return posicion - 1


    return -1

def Abcedaria(stringvalidar):

    abcedario="abcdefghijklmnñopqrstuvwxyz"

    # Primera letra desde del string a validar
    primeraLetraValidar = stringvalidar[0]

    # Primera letra del abcedario desde donde empieza
    # AbcPos = abcedario.find(primeraLetraValidar)

    AbcPos = findcustom(abcedario,primeraLetraValidar)

    StringPos = 0
    valida = True


    while StringPos <= lencustom(stringvalidar) - 1:
        letra = stringvalidar[StringPos]
        letraAbcedario = abcedario[AbcPos]


        if letra != letraAbcedario:
            # Pasa a la siguiente letra en el abcedario y vuelve a comparar.
            AbcPos += 1
            letraAbcedario = abcedario[AbcPos]
            if letra != letraAbcedario:
                valida = False
                break
        StringPos += 1

    return valida


valor = Abcedaria("abcd")
print("abcd: " + str(valor))

valor = Abcedaria("cdee")
print("cdee: " + str(valor))

valor = Abcedaria("aaaa")
print("aaaa: " + str(valor))

valor = Abcedaria("vaed")
print("vaed: " + str(valor))

valor = Abcedaria("baqw")
print("baqw: " + str(valor))

valor = Abcedaria("1234")
print("1234: " + str(valor))

valor = Abcedaria("aabbccddddddddeeeffffggghijkkkkkklmnnnnnnñoooooo")
print("aabbccddddddddeeeffffggghijkkkkkklmnnnnnnñoooooo: " + str(valor))

valor = Abcedaria("ax")
print("ax: " + str(valor))