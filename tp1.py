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
        # [COMPLETAR]

    elif opcion_seleccionada == 'B':
        # [COMPLETAR]
        pass  # borrar esta línea

    elif opcion_seleccionada == 'C':
        # [COMPLETAR]
        pass  # borrar esta línea

    elif opcion_seleccionada == 'D':
        # [COMPLETAR]
        pass  # borrar esta línea

    elif opcion_seleccionada == 'F':
        finalizar = True

    else:
        print('Opción inválida.')

    if opcion_seleccionada != 'F':
        print()
        input('Presione ENTER para continuar.')

#############################################################################
