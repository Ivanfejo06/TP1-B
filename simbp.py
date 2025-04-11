def simBP(n: int, m: int) -> int:
    ''' Requiere: n > 0, m > 0
        Devuelve: la similitud binaria de prefijo entre n y m, definida como
        la longitud del prefijo común más largo entre las representaciones
        binarias de n y m. '''
    
    if n>0 and m>0:
        # Obtener las representaciones binarias sin el prefijo '0b'
        bin_n = bin(n).replace('0b', '')
        bin_m = bin(m).replace('0b', '')
        
        # Igualar longitudes anteponiendo ceros si es necesario
        max_len = max(len(bin_n), len(bin_m))
        bin_n = bin_n.zfill(max_len)
        bin_m = bin_m.zfill(max_len)
        
        # Comparar bit por bit
        count:int = 0
        i:int = 0
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
        bin_n = bin(n).replace('0b', '')  # representación binaria sin '0b'
        count = 0
        i = a

        while i <= b:
            bin_i = bin(i).replace('0b', '')
            max_len = max(len(bin_n), len(bin_i))
            
            # Alineamos los binarios rellenando con ceros a la izquierda
            bin_n_aligned = bin_n.zfill(max_len)
            bin_i_aligned = bin_i.zfill(max_len)

            # Contamos los bits iguales en las mismas posiciones
            simbp = 0
            j = 0
            while j < max_len:
                if bin_n_aligned[j] == bin_i_aligned[j]:
                    simbp += 1
                j += 1

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
    
    if cantidad_con_simBP_en_intervalo(n,a,b,k) > 0:
        return True
    else: 
        return False


def numero_con_mayor_simBP_en_intervalo(n:int, a:int, b:int) -> int:
    ''' Requiere: n>0, a>0, b>0, a<=b
        Devuelve: el número entre a y b (inclusive) con mayor simBP con n. En caso de haber más de uno, devuelve el menor de ellos.'''
    
    if n > 0 and a > 0 and b > 0 and a <= b:
        
    else:
        return print("Entrada inválida: asegúrate de que n, a, b, k > 0 y a <= b")