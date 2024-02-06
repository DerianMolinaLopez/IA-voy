lista_archivo = []
categoria = 0

# abrir el dataset.txt y lo guarda en la variable lista_archivo
def cargar_archivo():
    global lista_archivo
    with open("dataset.txt", 'r') as archivo:
        lista_archivo = archivo.readlines()        
        lista_archivo = [linea.strip().lower() + '\n' for linea in lista_archivo]#agregando el lower al strip ya convierte en minuscula
        print(lista_archivo)

# opcion 1: ordenar por nombre
def orden_nombre():
    global lista_archivo
    global categoria

    # ordenar por nombre
    lista_archivo = sorted(lista_archivo, key=lambda x: x.split(', ')[0].lower())#aqui con el lower te ignora si hay una entrada en mayusucla

    print(lista_archivo)

    print()
    categoria = 1

#este es un poco opcional, solo lo use para testear si se ordena correctamente
def mostrarFormato ():
    for linea in lista_archivo:
      print(linea)
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

    #ordenamos por medio de la categoria que este activa
    #si hay una categoria agregamos y ordenamos, si no, lo mandamos al final
    if categoria !=0:
        lista_archivo.append(nuevo_registro)
        categorias[categoria]()
        
    else:
        lista_archivo.append(nuevo_registro)
    print(lista_archivo)

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
#con este diccionario podemos agilizar el proceso de seleccion con unas lineas
categorias  = {
    1: orden_nombre,
    2: orden_peso,
    3: orden_estatura,
    4: insertar,
    5: eliminar
}
while True:
    print("Practica 1:")
    print("1. Orden por nombre")
    print("2. Orden por peso")
    print("3. Orden por estatura")
    print("4. Insertar un registro")
    print("5. Eliminar un registro")
    print("6. Salir")
    opcion = input("Elige una opcion: ")
    #validar los rangos
    if opcion >= '1' and opcion <= '6':
        categorias[int(opcion)]()
    else:
        print("dato no valido!")
        print()
    '''
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
    '''
    