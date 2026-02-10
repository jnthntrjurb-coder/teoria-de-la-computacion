def afd(cadena):
    estado = "q0"

    for simbolo in cadena:
        if estado == "q0":
            if simbolo == "0":
                estado = "q1"
            elif simbolo == "1":
                estado = "q0"
            else:
                return False

        elif estado == "q1":
            if simbolo == "0":
                estado = "q1"
            elif simbolo == "1":
                estado = "q2"
            else:
                return False

        elif estado == "q2":
            if simbolo == "0":
                estado = "q1"
            elif simbolo == "1":
                estado = "q0"
            else:
                return False

    return estado == "q2"


cadena = input("Cadena 0 y 1: ")

if afd(cadena):
    print("ACEPTADA")
else:
    print("RECHAZADA")

