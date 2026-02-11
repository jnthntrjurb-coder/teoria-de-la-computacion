def afd(cadena):
    estado = "q0"  # estado inicial

    for simbolo in cadena:
        if estado == "q0":
            if simbolo == "0":
                estado = "q1"
            elif simbolo == "1":
                estado = "q2"
            else:
                return False

        elif estado == "q1":  # se leyó 0
            if simbolo == "1":
                estado = "q3"  # reconoce 01
            else:
                return False

        elif estado == "q2":  # se leyó 1
            if simbolo == "0":
                estado = "q3"  # reconoce 10
            else:
                return False

        elif estado == "q3":  # estado principal (aceptación)
            if simbolo == "1":
                estado = "q3"  # (11)*
            elif simbolo == "0":
                estado = "q0"  # cierra el bloque con 0
            else:
                return False

    return estado == "q3"


cadena = input("Ingresa una cadena con símbolos 0 y 1: ")

if afd(cadena):
    print("La cadena es ACEPTADA por el AFD")
else:
    print("La cadena es RECHAZADA por el AFD")
