def simBP(n: int, m: int) -> int:
    ''' Requiere: n > 0, m > 0
        Devuelve: la similitud binaria de prefijo entre n y m, definida como
        la longitud del prefijo común más largo entre las representaciones
        binarias de n y m. '''
    
    if n > 0 and m > 0:
        # Obtener las representaciones binarias de n y m (sin el prefijo '0b')
        bin_n = bin(n).replace('0b', '')
        bin_m = bin(m).replace('0b', '')
        
        # Igualar longitudes añadiendo ceros a la izquierda
        max_len = max(len(bin_n), len(bin_m))
        bin_n = bin_n.zfill(max_len)
        bin_m = bin_m.zfill(max_len)
        
        # Contar cuántos bits consecutivos son iguales desde el inicio
        count = 0
        i = 0
        while i < max_len and bin_n[i] == bin_m[i]:
            count += 1
            i += 1
        return count
    
    else:
        print("Entrada inválida: asegúrate de que n, m > 0")
        return -1


def cantidad_con_simBP_en_intervalo(n: int, a: int, b: int, k: int) -> int:
    ''' Requiere: n>0, a>0, b>0, k>0, a<=b
        Devuelve: la cantidad de números entre a y b (inclusive)
        cuya simBP con n es k.'''

    if n > 0 and a > 0 and b > 0 and k > 0 and a <= b:
        bin_n = bin(n).replace('0b', '')  # binario de n sin '0b'
        count = 0  # Contador de números que cumplen la condición
        i = a

        while i <= b:
            bin_i = bin(i).replace('0b', '')  # binario de i
            max_len = max(len(bin_n), len(bin_i))
            
            # Rellenar con ceros a la izquierda para igualar longitudes
            bin_n_aligned = bin_n.zfill(max_len)
            bin_i_aligned = bin_i.zfill(max_len)

            # Comparar bits en las mismas posiciones
            simbp = 0
            j = 0
            while j < max_len:
                if bin_n_aligned[j] == bin_i_aligned[j]:
                    simbp += 1
                j += 1

            # Si la similitud es igual a k, se suma al contador
            if simbp == k:
                count += 1

            i += 1

        return count

    else:
        print("Entrada inválida: asegúrate de que n, a, b, k > 0 y a <= b")
        return -1


def existe_con_simBP_en_intervalo(n:int, a:int, b:int, k:int) -> bool:
    ''' Requiere: n>0, a>0, b>0, k>0, a<=b
        Devuelve: True si existe algún número entre a y b (inclusive)
        cuya simBP con n es k; False en caso contrario.'''
    
    # Usa la función anterior para contar cuántos cumplen
    if cantidad_con_simBP_en_intervalo(n, a, b, k) > 0:
        return True
    else: 
        return False


def numero_con_mayor_simBP_en_intervalo(n:int, a:int, b:int) -> int:
    ''' Requiere: n>0, a>0, b>0, a<=b
        Devuelve: el número entre a y b (inclusive) con mayor simBP con n.
        En caso de haber más de uno, devuelve el menor de ellos.'''
    
    if n > 0 and a > 0 and b > 0 and a <= b:
        bin_n = bin(n)[2:]  # binario de n sin '0b'
        i = a
        max_simBP = -1
        mejor_numero = a  # Se empieza con el primer número del intervalo

        while i <= b:
            bin_i = bin(i)[2:]  # binario de i
            max_len = max(len(bin_n), len(bin_i))
            bin_n_aligned = bin_n.zfill(max_len)
            bin_i_aligned = bin_i.zfill(max_len)

            # Contar cuántos bits consecutivos coinciden desde el principio
            simbp = 0
            j = 0
            while j < max_len:
                if bin_n_aligned[j] == bin_i_aligned[j]:
                    simbp += 1
                else:
                    break  # se detiene si hay un bit diferente
                j += 1

            # Actualizar si se encuentra una mejor similitud
            if simbp > max_simBP:
                max_simBP = simbp
                mejor_numero = i
            elif simbp == max_simBP and i < mejor_numero:
                mejor_numero = i  # preferimos el menor si hay empate

            i += 1
        return mejor_numero
    else:
        return print("Entrada inválida: asegúrate de que n, a, b > 0 y a <= b")