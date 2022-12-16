import json

# Este programa sirve para gestionar las calificaciones de los alumnos
# permitiendo la visualización de todos los alumnos existentes, la adición
# de nuevos alumnos y la eliminación de los existentes. Además, permite la 
# gestión de sus cursos, correos electrónicos y notas, clasificadas en 
# asignaturas y tareas, y mostrará la nota media de todas sus notas



###############################   FUNCIONES  ###############################


#######   MANIPULACIÓN DE DATOS    #########################################


# 1) Función que comprueba la existencia de un archivo 
# anterior o crea uno nuevo

def Comprobar_fichero():
    try:
        f = open('datos.json','r')
        f.close
        
    except:
        relleno = {'alumnos': []}
        f = open('datos.json','w')
        json.dump(relleno, f)
        f.close

# 2) Función que carga los datos guardados

def Cargar_datos():
    f = open('datos.json','r')
    alumnos = json.load(f)
    f.close

    return alumnos

# 3) Función que guarda los cambios realizados

def Guardar_datos(dic):
    f = open('datos.json','w')
    json.dump(dic, f)
    f.close


###########   MENÚ PRINCIPAL   #######################################################################


# 4) Función que muestra el menú principal del programa. Se verá al principio 
# del mismo y cada vez que se retroceda en el programa

def menu():
    ret = '''
================================
         MENU PRINCIPAL
================================
Este programa gestiona las 
calificaciones de los alumnos.

Seleccione la opción que desee

    Opciones:

    1) Ver alumno
    2) Añadir alumno
    3) Eliminar alumno 
    4) Salir
---------------------------------
        Lista de alumnado:
''' 
    return ret

# 5) Función que permite visualizar solo los nombres por pantalla y en vertical

def Visualizar_alumnos(dic):
    lista_alumnos = dic['alumnos']
    alumnos = []

    for diccionario in lista_alumnos:
        alumno = diccionario['nombre']
        alumnos.append(alumno)

    for i in alumnos:
        print(i)

# 6) Función que permite elegir entre las opciones del terminal

def Elegir_opcion_menu():
    while True:
        opcion = input('''
    Introduzca opción: ''')

        try: int(opcion)
        except: print('''
    {} no es una opción válida. Por favor, elija un número de 1 a 4'''.format(opcion))
        else: 
            if int(opcion) in range(1,5):
                print('Ha seleccionado opcion {}'.format(opcion))
                break
            else:
                print('''
    {} no es una opción válida. Por favor, elija un número de 1 a 4'''.format(opcion))

    return int(opcion)

# 7) Función que permite crear nuevos alumnos

def Añadir_alumno(dic):
    print('''
    Siga las instrucciones para crear un nuevo alumno
    ''')
    nombre = input('Introduzca nombre completo: ')
    curso = input('Introduzca el curso: ')
    gmail = input('Introduzca correo electrónico: ')
    calificaciones = []

    alumno = {
        'nombre': nombre, 
        'curso': curso, 
        'correo electrónico': gmail, 
        'calificaciones': calificaciones}

    alumnos = dic['alumnos']
    
    return alumnos.append(alumno)

# 7) Función que permite eliminar alumnos existentes

def Eliminar_alumno(dic):
    nombre = input('''
    Escriba el alumno a eliminar: ''')
    alumnos = dic['alumnos']
    contador = 0
    verdad = False

    for i in alumnos:
        if i['nombre'] == nombre:
            alumnos.pop(contador)
            verdad = True
        contador+=1
    
    if verdad == False:
        print('''
    Alumno no existente o fallo de escritura
    ''')



##########   MENU ALUMNO   ############################################################################


# 8) Función que añade los datos del alumno a un valor para su más rápido acceso si existe el alumno

def datos_alumno(nombre, dic):
    lista_alumnos = dic['alumnos']
    for diccionario in lista_alumnos:
        if diccionario['nombre'] == nombre:
            ficha = diccionario.copy()
    
    return ficha

# 9) Función que hace una lista de tuplas de las claves y valores del alumno

def objetos_alumno(ficha):
    objetos = ficha.items()

    return objetos

# 10) Función que permite visualizar la ficha de un alumno

def Visualizar_alumno(objetos):
    for i in objetos:
        print(i)

# 11) Función que permite seleccionar entre las opciones en el menu del alumno 

def Elegir_opcion_alumno():
    while True:
        opcion = input('''
    Introduzca opción: ''')

        try: int(opcion)
        except: print('''
    {} no es una opción válida. Por favor, elija un número de 1 a 4'''.format(opcion))
        else: 
            if int(opcion) in range(1,5):
                print('Ha seleccionado opcion {}'.format(opcion))
                break
            else:
                print('''
    {} no es una opción válida. Por favor, elija un número de 1 a 4'''.format(opcion))

    return int(opcion)


# 12) Función que muestra las opciones de la ficha del alumno

def Menu_alumno():
    ret = '''
    Opciones:

    1) Añadir calificación
    2) Eliminar calificación 
    3) Media calificaciones por asignatura
    4) Atrás
    '''

    return ret

# 13) Función que permite añadir calificaciones a un alumno

def Añadir_calificacion(ficha):
    print('''
    Intoduzca los datos pedidos para añadir la calificación:
    ''')

    asignatura = input('Introduzca la asignatura: ')
    tarea = input('Introduzca la tarea: ')
    while True:
        nota = input('Introduzca nota de la tarea: ')
        try: nota = int(nota)
        except: print('La nota debe ser un número del 1 al 10')
        else: 
            nota = int(nota)
            if 0 <= nota <= 10:
                break
            else: print('''
    La nota debe ser un número del 1 al 10
            ''')
        
    calificacion = [asignatura, tarea, nota]

    ficha['calificaciones'].append(calificacion)

    return objetos
    
# 14) Función que permite quitar calificaciones de un alumno

def Eliminar_calificacion(dic):
    tarea = input('''
    Escriba la tarea de la calificación que desea eliminar: ''')
    calificaciones = dic['calificaciones']
    contador = 0
    verdad = False

    for i in calificaciones:
        if i[1] == tarea:
            verdad = True
            calificaciones.pop(contador)
        contador+=1
    
    if verdad == False:
        print('''
        Tarea no encontrada
        ''')

# 15) Función que crea muestra la nota media de cada asignatura

def media(ficha):
    calificaciones = ficha['calificaciones']
    asignaturas = {}

    for lista in calificaciones:
        clave = lista[0]
        valor = lista[2]
        
        if clave in asignaturas:
            asignaturas[clave].append(valor)
        
        if clave not in asignaturas:
            asignaturas[clave] = []
            asignaturas[clave].append(valor)

    llave = asignaturas.keys()

    for i in llave:
        contador = 0
        suma = 0
        for k in asignaturas[i]:
            suma += k
            contador += 1
            media = k/contador

            print('''
            Media de {} = {}
            '''.format(i, media))

# 16) Función que pasa los datos del alumno a la lista general

def general(ficha,dic):
    alumnos = dic['alumnos']
    nombre = ficha['nombre']
    contador = 0

    for diccionario in alumnos:
        if diccionario['nombre'] == nombre:
            alumnos[contador] = ficha

###############################   PROGRAMA  #########################################


Comprobar_fichero()

d = Cargar_datos()

# Manipulación en menú principal

while True:
    print(menu())

    Visualizar_alumnos(d)

    Eleccion = Elegir_opcion_menu()

    # Selección del menú de un alumno

    if Eleccion == 1: 
        nombre = input('''
    Introduzca el nombre del alumno que busca: ''')

        while True:
            try: datos_alumno(nombre, d)
            except: 
                print('''
    Alumno no existente o  fallo en la escritura
    ''')
                break
            else: 
                ficha = datos_alumno(nombre, d)

            objetos = objetos_alumno(ficha)

            Visualizar_alumno(objetos)

            print(Menu_alumno())

            opcion = Elegir_opcion_alumno()

            if opcion == 1:
                Añadir_calificacion(ficha)

            if opcion == 2:
                Eliminar_calificacion(ficha)

            if opcion == 3:
                media(ficha)

            if opcion == 4:
                general(ficha, d)
                break

    # Función para añadir un alumno

    if Eleccion == 2:
        Añadir_alumno(d)

    if Eleccion == 3:
        Eliminar_alumno(d)

    # Cierre del programa

    if Eleccion == 4:
        break

print('''
Guardando datos...
''')
Guardar_datos(d)
print('''Datos guardados
Cerrando programa''')