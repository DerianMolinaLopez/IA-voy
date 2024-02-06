lista_archivo = []
categoria = 0

# abrir el dataset.txt y lo guarda en la variable lista_archivo
def cargar_archivo():
    global lista_archivo
    with open("dataset.txt", 'r') as archivo:
        lista_archivo = archivo.readlines()
        lista_archivo = [linea.strip() + '\n' for linea in lista_archivo]

# opcion 1: ordenar por nombre
def orden_nombre():
    global lista_archivo
    global categoria

    # ordenar por nombre
    lista_archivo = sorted(lista_archivo, key=lambda x: x.split(', ')[0])

    print(lista_archivo)

    print()
    categoria = 1

# opcion 2: ordenar por peso
def orden_peso():
    global lista_archivo
    global categoria

    # ordenar por peso
    lista_archivo = sorted(lista_archivo, key=lambda x: int(x.split(', ')[1]))

    print(lista_archivo)

    print()
    categoria = 2

# opcion 3: odenar por estatura
def orden_estatura():
    global lista_archivo
    global categoria

    # ordenar por estatura
    lista_archivo = sorted(lista_archivo, key=lambda x: float(x.split(', ')[2]))

    print(lista_archivo)

    print()
    categoria = 3

# opcion 4: insertar dato
def insertar():
    global lista_archivo
    global categoria

    nuevo_nombre = input("Ingresa nombre completo: ")
    nuevo_peso = input("Ingresa el peso de " + nuevo_nombre + ": ")
    nueva_estatura = input("Ingresa la estatura de " + nuevo_nombre + ": ")

    print()

    # guarda un nuevo elemento para el txt
    nuevo_registro = nuevo_nombre + ", " + nuevo_peso + ", " + nueva_estatura + "\n"

    # NOMBRE
    if categoria == 1:
        # si es el menor, lo pone hasta arriba
        if nuevo_nombre < lista_archivo[0].split(', ')[0]:
            lista_archivo.insert(0, nuevo_registro)

        # si es el mayor, lo pone hasta abajo
        elif nuevo_nombre > lista_archivo[-1].split(', ')[0]:
            lista_archivo.append(nuevo_registro)
    
        # busqueda lineal para encontrar en donde debe de ir
        else:
            for i in range(len(lista_archivo) - 1):
                nombre_actual = lista_archivo[i].split(', ')[0]
                nombre_siguiente = lista_archivo[i + 1].split(', ')[0]
                if nombre_actual < nuevo_nombre < nombre_siguiente:
                    lista_archivo.insert(i + 1, nuevo_registro)
                    break

        print(lista_archivo)

        print()
    
    # PESO
    if categoria == 2:
        # si es el menor, lo pone hasta arriba
        if int(nuevo_peso) < int(lista_archivo[0].split(', ')[1]):
            lista_archivo.insert(0, nuevo_registro)
        # si es el mayor, lo pone hasta abajo
        elif int(nuevo_peso) > int(lista_archivo[-1].split(', ')[1]):
            lista_archivo.append(nuevo_registro)
    
        # busqueda lineal para encontrar en donde debe de ir
        else:
            for i in range(len(lista_archivo) - 1):
                peso_actual = int(lista_archivo[i].split(', ')[1])
                peso_siguiente = int(lista_archivo[i + 1].split(', ')[1])
                if peso_actual < int(nuevo_peso) < peso_siguiente:
                    lista_archivo.insert(i + 1, nuevo_registro)
                    break

        print(lista_archivo)

        print()

    # ESTATURA
    if categoria == 3:
        # si es el menor, lo pone hasta arriba
        if float(nueva_estatura) < float(lista_archivo[0].split(', ')[2]):
            lista_archivo.insert(0, nuevo_registro)
        # si es el mayor, lo pone hasta abajo
        elif float(nueva_estatura) > float(lista_archivo[-1].split(', ')[2]):
            lista_archivo.append(nuevo_registro)
    
        # busqueda lineal para encontrar en donde debe de ir
        else:
            for i in range(len(lista_archivo) - 1):
                estatura_actual = float(lista_archivo[i].split(', ')[2])
                estatura_siguiente = float(lista_archivo[i + 1].split(', ')[2])
                if estatura_actual < float(nueva_estatura) < estatura_siguiente:
                    lista_archivo.insert(i + 1, nuevo_registro)
                    break

        print(lista_archivo)

        print()

# opcion 5: eliminar dato
def eliminar():
    global lista_archivo
    
    registro_eliminar = input("Ingresa el nombre completo del registro a eliminar: ")

    # borra el elemento de la lista (haciendo un filtro) y lo guarda en una nueva variable
    lista_nueva = [linea for linea in lista_archivo if registro_eliminar.casefold() != linea.split(', ')[0].casefold()]
    
    lista_archivo = lista_nueva
    
    print()
    print("LISTA NUEVA")
    print(lista_nueva)
    print() 

# carga los datos antes de entrar al menu
cargar_archivo()

while True:
    print("Practica 1:")
    print("1. Orden por nombre")
    print("2. Orden por peso")
    print("3. Orden por estatura")
    print("4. Insertar un registro")
    print("5. Eliminar un registro")
    print("6. Salir")

    opcion = input("Ingresa el numero para la opcion que quiera realizar: ")
    print()

    if opcion == '1':
        orden_nombre()
    elif opcion == '2':
        orden_peso()
    elif opcion == '3':
        orden_estatura()
    elif opcion == '4':
        insertar()
    elif opcion == '5':
        eliminar()
    elif opcion == '6':
        break
    else:
        print("dato no valido!")
        print()