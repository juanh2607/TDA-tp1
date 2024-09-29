import sys

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
    if len(sys.argv) > 1:
        nombre_archivo = sys.argv[1]
    else:
        nombre_archivo = input("Por favor ingrese el nombre de su set de datos: ")

    with open(DIR_PRUEBAS + nombre_archivo) as archivo:
        archivo.readline()
        monedas = [int(moneda) for moneda in archivo.readline().split(";")]
        puntaje_sophia, puntaje_mateo = ganar_siempre(monedas)

        print(f"\n--- {nombre_archivo} ---")
        print(f"Total monedas: {sum(monedas)}")
        print(f"Puntaje Sophia: {puntaje_sophia} - Puntaje Mateo: {puntaje_mateo}")

        # Comparar ganancia de Sophia
        total_monedas = sum(monedas)
        assert (
            puntaje_sophia + puntaje_mateo == total_monedas
        ), f"Error en {nombre_archivo}: la suma de puntajes ({puntaje_sophia + puntaje_mateo}) no coincide con el total de las monedas ({total_monedas})."

        assert (
            puntaje_sophia >= puntaje_mateo
        ), f"Error en {nombre_archivo}: Puntaje de Sophia ({puntaje_sophia}) es menor que el de Mateo ({puntaje_mateo})."

        print(f"Prueba {nombre_archivo} exitosa.")


if __name__ == "__main__":
    main()
