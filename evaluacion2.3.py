def afd(cadena):
    estado = "q0"  # sin 1's, ceros pares

    for simbolo in cadena:
        if estado == "q0":  # 0 unos, ceros pares
            if simbolo == "0":
                estado = "q1"
            elif simbolo == "1":
                estado = "q2"
            else:
                return False

        elif estado == "q1":  # 0 unos, ceros impares
            if simbolo == "0":
                estado = "q0"
            elif simbolo == "1":
                estado = "q3"
            else:
                return False

        elif estado == "q2":  # unos impares, ceros pares
            if simbolo == "0":
                estado = "q4"
            elif simbolo == "1":
                estado = "q5"
            else:
                return False

        elif estado == "q3":  # unos impares, ceros impares
            if simbolo == "0":
                estado = "q2"
            elif simbolo == "1":
                estado = "q4"
            else:
                return False

        elif estado == "q4":  # unos pares (>0), ceros pares
            if simbolo == "0":
                estado = "q5"
            elif simbolo == "1":
                estado = "q2"
            else:
                return False

        elif estado == "q5":  # unos pares (>0), ceros impares
            if simbolo == "0":
                estado = "q4"
            elif simbolo == "1":
                estado = "q3"
            else:
                return False

    # Estados de aceptación según las reglas
    return estado in ["q0", "q5", "q4"]


cadena = input("Ingresa una cadena con símbolos 0 y 1: ")

if afd(cadena):
    print("ACEPTADA")
else:
    print("RECHAZADA")
