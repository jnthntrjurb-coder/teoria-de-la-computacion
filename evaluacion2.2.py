def afd(cadena):
    estado = "q0"  # q0: número de a's par, último símbolo NO fue b

    for simbolo in cadena:
        if estado == "q0":  # par, no b
            if simbolo == "a":
                estado = "q1"
            elif simbolo == "b":
                estado = "q2"
            elif simbolo == "c":
                estado = "q0"
            else:
                return False

        elif estado == "q1":  # impar, no b
            if simbolo == "a":
                estado = "q0"
            elif simbolo == "b":
                estado = "q3"
            elif simbolo == "c":
                estado = "q1"
            else:
                return False

        elif estado == "q2":  # par, último fue b
            if simbolo == "a":
                estado = "q1"
            elif simbolo == "b":
                estado = "q2"
            elif simbolo == "c":
                return False  # aparece subcadena bc
            else:
                return False

        elif estado == "q3":  # impar, último fue b
            if simbolo == "a":
                estado = "q0"
            elif simbolo == "b":
                estado = "q3"
            elif simbolo == "c":
                return False  # aparece subcadena bc
            else:
                return False

    return estado in ["q0", "q2"]  # número de a's par


cadena = input("Ingresa una cadena con símbolos a, b, c: ")

if afd(cadena):
    print("ACEPTADA")
else:
    print("RECHAZADA")
