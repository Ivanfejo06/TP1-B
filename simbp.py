def simBP(n: int, m: int) -> int:
    ''' Requiere: n > 0, m > 0
        Devuelve: la longitud del prefijo binario común más largo entre n y m. '''
    
    if n > 0 and m > 0:
        bin_n = bin(n).replace('0b', '')
        bin_m = bin(m).replace('0b', '')
        
        len_n = len(bin_n)
        len_m = len(bin_m)
        min_len = len_n if len_n < len_m else len_m

        count = 0
        i = 0
        while i < min_len:
            if bin_n[i] == bin_m[i]:
                count += 1
                i += 1
            else:
                break
        return count
    else:
        print("Entrada inválida: asegúrate de que n, m > 0")
        return -1


def cantidad_con_simBP_en_intervalo(n: int, a: int, b: int, k: int) -> int:
    ''' Requiere: n>0, a>0, b>0, k>0, a<=b
        Devuelve: la cantidad de números entre a y b (inclusive)
        cuya simBP con n es k.'''
    
    if n > 0 and a > 0 and b > 0 and k > 0 and a <= b:
        count = 0
        i = a
        while i <= b:
            if simBP(n, i) == k:
                count += 1
            i += 1
        return count
    else:
        print("Entrada inválida: asegúrate de que n, a, b, k > 0 y a <= b")
        return -1


def existe_con_simBP_en_intervalo(n: int, a: int, b: int, k: int) -> bool:
    ''' Requiere: n>0, a>0, b>0, k>0, a<=b
        Devuelve: True si existe algún número entre a y b (inclusive)
        cuya simBP con n es k; False en caso contrario.'''

    return cantidad_con_simBP_en_intervalo(n, a, b, k) > 0


def numero_con_mayor_simBP_en_intervalo(n: int, a: int, b: int) -> int:
    ''' Requiere: n>0, a>0, b>0, a<=b
        Devuelve: el número entre a y b (inclusive) con mayor simBP con n.
        En caso de empate, devuelve el menor de ellos.'''
    
    if n > 0 and a > 0 and b > 0 and a <= b:
        i = a
        max_simBP = -1
        mejor_numero = a

        while i <= b:
            actual_simBP = simBP(n, i)
            if actual_simBP > max_simBP:
                max_simBP = actual_simBP
                mejor_numero = i
            elif actual_simBP == max_simBP and i < mejor_numero:
                mejor_numero = i
            i += 1

        return mejor_numero
    else:
        print("Entrada inválida: asegúrate de que n, a, b > 0 y a <= b")
        return -1