def esEntero(numero):
    parametroEntero = int(numero)
    if numero > parametroEntero:
        return False
    else:
        return True


def esPar(numero):

        if esEntero(numero):
            # si el numero es Entero, lo divido por dos
            numero = numero / 2
            # Si el numero divido 2 a su vez es entero, es par.
            if esEntero(numero):
                return(True)
            else:
                return (False)
        else:
            print("Debe ingresar un número entero")
            return False

valor = 88
print (esPar(valor))

valor = 87
print (esPar(valor))
