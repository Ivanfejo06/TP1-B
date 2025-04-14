from simbp import simBP, cantidad_con_simBP_en_intervalo, \
   existe_con_simBP_en_intervalo, numero_con_mayor_simBP_en_intervalo

def elegir_funcion() -> str:
    '''
    Despliega el menú de funciones disponibles en la pantalla y devuelve
    la opción elegida por el usuario según la siguiente codificación:
        A. Similitud binaria de prefijo [n,m]
        B. Cantidad de enteros con simBP en intervalo [n,a,b,k]
        C. Existe entero con simBP en intervalo [n,a,b,k]
        D. Entero con mayor simBP en intervalo [n,a,b]
        F. Finalizar
    Requiere: Nada.
    Devuelve: La opción elegida por el usuario, en mayúscula y sin espacios adelante y atrás.
    '''
    print()
    print('Funciones disponibles')
    print('---------------------')
    print('A. Similitud binaria de prefijo [n,m]')
    print('B. Cantidad de enteros con simBP en intervalo [n,a,b,k]')
    print('C. Existe entero con simBP en intervalo [n,a,b,k]')
    print('D. Entero con mayor simBP en intervalo [n,a,b]')
    print('F. Finalizar')
    print()
    opción_elegida:str = input('Seleccione una opción: ').upper().strip()
    return opción_elegida

#############################################################################

# Cuerpo principal del programa
finalizar:bool = False
while not finalizar:
    opcion_seleccionada:str = elegir_funcion()

    # Se analiza la opción elegida
    if opcion_seleccionada == 'A':
        n_str:str = input('Ingrese n: ')
        m_str:str = input('Ingrese m: ')
        if(n_str.isdigit() and m_str.isdigit()):
            n:int = int(n_str)
            m:int = int(m_str)
            count:int = simBP(n,m)
            print(f"La cantidad de digitos del simBP es de {count} digitos.") 
        else:
            print("Alguno de los dos caracteres ingresados no es un numero entero.")
        
    elif opcion_seleccionada == 'B':
        n_str:str = input('Ingrese n: ')
        a_str:str = input('Ingrese a: ')
        b_str:str = input('Ingrese b: ')
        k_str:str = input('Ingrese k: ')

        if(n_str.isdigit() and a_str.isdigit() and b_str.isdigit() and k_str.isdigit()):
            n:int = int(n_str)
            a:int = int(a_str)
            b:int = int(b_str)
            k:int = int(k_str)
            count:int = cantidad_con_simBP_en_intervalo(n,a,b,k)
            print(f'La cantidad de enteros con simBP en {n} de los primeros {k} digitos en el intervalo [{a},{b}] es {count}') 
        else:
            print("Alguno de los dos caracteres ingresados no es un numero entero.")

    elif opcion_seleccionada == 'C':
        n_str:str = input('Ingrese n: ')
        a_str:str = input('Ingrese a: ')
        b_str:str = input('Ingrese b: ')
        k_str:str = input('Ingrese k: ')

        if(n_str.isdigit() and a_str.isdigit() and b_str.isdigit() and k_str.isdigit()):
            n:int = int(n_str)
            a:int = int(a_str)
            b:int = int(b_str)
            k:int = int(k_str)
            exists:bool = existe_con_simBP_en_intervalo(n,a,b,k)
            if (exists):
                print(f'Dentro del intervalo [{a},{b}] existen simBP para el numero {n}.')
            else:
                print(f'No existe nungina simBP para {n} en el intervalo [{a},{b}].')
        else:
            print("Alguno de los dos caracteres ingresados no es un numero entero.")

    elif opcion_seleccionada == 'D':
        n_str:str = input('Ingrese n: ')
        a_str:str = input('Ingrese a: ')
        b_str:str = input('Ingrese b: ')

        if(n_str.isdigit() and a_str.isdigit() and b_str.isdigit()):
            n:int = int(n_str)
            a:int = int(a_str)
            b:int = int(b_str)
            best:int = numero_con_mayor_simBP_en_intervalo(n,a,b)
            if(best > 0):
                print(f'EL menor numero posible con mayor simBP para {n} dentro del intervalo [{a},{b}] es el numero {best}.')
            else:
                print("No hay coincidencias")
        else:
            print("Alguno de los dos caracteres ingresados no es un numero entero.")

    elif opcion_seleccionada == 'F':
        finalizar = True

    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'F':
        print()
        input('Presione ENTER para continuar.')

#############################################################################
