def menu():
    opcion = ''
    while opcion != '4':
        print('\n--- MENU PRINCIPAL ---')
        print('1. Jugar nueva partida')
        print('2. Ver lista de tematicas')
        print('3. Instrucciones')
        print('4. Salir')
        opcion = input('Seleccione una opción: ')

        # limpiar_consola()

        match opcion:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                break

menu()