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
            if monedas[i_izq] >= monedas[j_der]:
                puntaje_sophia += monedas[i_izq]
                i_izq += 1
            else:
                puntaje_sophia += monedas[j_der]
                j_der -= 1
        else:
            # Turno Mateo -> agarramos la moneda menor
            if monedas[i_izq] <= monedas[j_der]:
                puntaje_mateo += monedas[i_izq]
                i_izq += 1
            else:
                puntaje_mateo += monedas[j_der]
                j_der -= 1
        
        turno_actual += 1
    
    return puntaje_sophia, puntaje_mateo

def main():
    # prueba = [72, 165, 794, 892, 880, 341, 882, 570, 679, 725, 979, 375, 459, 603, 112, 436, 587, 699, 681, 83]
    # Sophia deberia ganar 7165
    # Nos esta dando 7058
    # Puntaje total: 11014 -> Sophia 7165 y Mateo 3849
    pruebas = ["20.txt", "25.txt", "50.txt", "100.txt", "1000.txt", "10000.txt", "20000.txt"]
    for prueba in pruebas:
        with open(DIR_PRUEBAS + prueba) as archivo_prueba:
            archivo_prueba.readline()
            monedas = [int(moneda) for moneda in archivo_prueba.readline().split(";")]
            resultado = ganar_siempre(monedas)
            print("\n")
            print(f"Total monedas: {sum(monedas)}")
            print(f"Puntaje Sophia: {resultado[0]} - Puntaje Mateo: {resultado[1]}")

if __name__ == '__main__':
    main()