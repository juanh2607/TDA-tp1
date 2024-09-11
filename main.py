DIR_PRUEBAS = "Pruebas/"


def ganar_siempre(monedas):
    cant_turnos = len(monedas)

    i_izq = 0
    j_der = cant_turnos - 1
    turno_actual = 0
    puntaje_sophia = 0
    puntaje_mateo = 0

    while turno_actual < cant_turnos:
        if turno_actual % 2 == 0:
            # Turno Sophia -> agarramos la moneda mayor
            if monedas[i_izq] > monedas[j_der]:
                puntaje_sophia += monedas[i_izq]
                i_izq += 1
            else:
                puntaje_sophia += monedas[j_der]
                j_der -= 1
        else:
            # Turno Mateo -> agarramos la moneda menor
            if monedas[i_izq] < monedas[j_der]:
                puntaje_mateo += monedas[i_izq]
                i_izq += 1
            else:
                puntaje_mateo += monedas[j_der]
                j_der -= 1

        turno_actual += 1

    return puntaje_sophia, puntaje_mateo


def main():
    pruebas = [
        "20.txt",
        "25.txt",
        "50.txt",
        "100.txt",
        "1000.txt",
        "10000.txt",
        "20000.txt",
    ]

    for prueba in pruebas:
        with open(DIR_PRUEBAS + prueba) as archivo_prueba:
            archivo_prueba.readline()
            monedas = [int(moneda) for moneda in archivo_prueba.readline().split(";")]
            puntaje_sophia, puntaje_mateo = ganar_siempre(monedas)

            print(f"\n--- {prueba} ---")
            print(f"Total monedas: {sum(monedas)}")
            print(f"Puntaje Sophia: {puntaje_sophia} - Puntaje Mateo: {puntaje_mateo}")

            # Comparar ganancia de Sophia
            total_monedas = sum(monedas)
            assert (
                puntaje_sophia + puntaje_mateo == total_monedas
            ), f"Error en {prueba}: la suma de puntajes ({puntaje_sophia + puntaje_mateo}) no coincide con el total de las monedas ({total_monedas})."

            assert (
                puntaje_sophia >= puntaje_mateo
            ), f"Error en {prueba}: Puntaje de Sophia ({puntaje_sophia}) es menor que el de Mateo ({puntaje_mateo})."

            print(f"Prueba {prueba} exitosa.")


if __name__ == "__main__":
    main()
