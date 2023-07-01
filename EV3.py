from tkinter import *
from tkinter import messagebox
from pymongo import MongoClient

# Función que se ejecuta al hacer clic en el botón "Alumnos"
def mostrar_alumnos():
    # Conectarse a la base de datos
    client = MongoClient('mongodb://'+user.get()+':'+password.get()+'@localhost:27017/Base2')
    db = client.Base2
    alumnos_collection = db.Alumnos

    # Obtener todos los alumnos
    alumnos = alumnos_collection.find()

    # Mostrar los datos en una ventana nueva
    ventana_alumnos = Toplevel()
    ventana_alumnos.title("Alumnos")

    # Crear un widget Text para mostrar los datos de los alumnos
    text_alumnos = Text(ventana_alumnos, wrap=NONE)
    text_alumnos.pack(side=LEFT, fill=Y)

    # Crear una barra de desplazamiento y asociarla al widget Text
    scroll = Scrollbar(ventana_alumnos, command=text_alumnos.yview)
    scroll.pack(side=RIGHT, fill=Y)
    text_alumnos.configure(yscrollcommand=scroll.set)

    for alumno in alumnos:
        # Eliminar el campo '_id' del diccionario del alumno
        alumno.pop('_id')

        # Crear un string con la información del alumno
        alumno_str = "Nombre: {}\nApellidos: {}\nFecha de Nacimiento: {}\nCarrera: {}\nEstatus: {}\nEmail: {}\nTeléfono: {}\nDirección: {}\n\n".format(
            alumno['nombre'], alumno['apellidos'], alumno['fecha_nacimiento'], alumno['carrera'], alumno['estatus'], alumno['email'], alumno['telefono'], alumno['direccion']
        )

        # Agregar el string al widget Text
        text_alumnos.insert(END, alumno_str)

def mostrar_carreras():
    # Conectarse a la base de datos
    client = MongoClient('mongodb://'+user.get()+':'+password.get()+'@localhost:27017/Base2')
    db = client.Base2
    carreras_collection = db.Carreras

    # Obtener todos las carreras
    carreras = carreras_collection.find()

    # Mostrar los datos en una ventana nueva
    ventana_carrera = Toplevel()
    ventana_carrera.title("Carreras")

    # Crear un widget Text para mostrar los datos de las carreras
    text_carrera = Text(ventana_carrera, wrap=NONE)
    text_carrera.pack(side=LEFT, fill=Y)

    # Crear una barra de desplazamiento y asociarla al widget Text
    scroll = Scrollbar(ventana_carrera, command=text_carrera.yview)
    scroll.pack(side=RIGHT, fill=Y)
    text_carrera.configure(yscrollcommand=scroll.set)

    for carreras in carreras:
        # Eliminar el campo '_id' del diccionario del alumno
        carreras.pop('_id')

    # Crear un string con la información del alumno
        carrera_str = "Abreviatura: {}\nNombre largo: {}\nDepartamento: {}\n\n".format(
        carreras['abreviatura'], carreras['nombre_largo'], carreras['departamento']
        )

        # Agregar el string al widget Text
        text_carrera.insert(END, carrera_str)

def agregar_alumno():
    # Crear ventana para agregar un nuevo alumno
    ventana_agregar_alumno = Toplevel()
    ventana_agregar_alumno.title("Agregar Alumno")

    # Etiquetas y campos de texto para ingresar los datos del nuevo alumno
    etiqueta_nombre = Label(ventana_agregar_alumno, text="Nombre")
    etiqueta_nombre.pack()
    nombre = Entry(ventana_agregar_alumno)
    nombre.pack()

    etiqueta_apellidos = Label(ventana_agregar_alumno, text="Apellidos")
    etiqueta_apellidos.pack()
    apellidos = Entry(ventana_agregar_alumno)
    apellidos.pack()

    etiqueta_fecha_nacimiento = Label(ventana_agregar_alumno, text="Fecha de Nacimiento (DD/MM/AAAA)")
    etiqueta_fecha_nacimiento.pack()
    fecha_nacimiento = Entry(ventana_agregar_alumno)
    fecha_nacimiento.pack()

    etiqueta_carrera = Label(ventana_agregar_alumno, text="Carrera")
    etiqueta_carrera.pack()
    carrera = Entry(ventana_agregar_alumno)
    carrera.pack()

    etiqueta_estatus = Label(ventana_agregar_alumno, text="Estatus")
    etiqueta_estatus.pack()
    estatus = Entry(ventana_agregar_alumno)
    estatus.pack()

    etiqueta_email = Label(ventana_agregar_alumno, text="Email")
    etiqueta_email.pack()
    email = Entry(ventana_agregar_alumno)
    email.pack()

    etiqueta_telefono = Label(ventana_agregar_alumno, text="Teléfono")
    etiqueta_telefono.pack()
    telefono = Entry(ventana_agregar_alumno)
    telefono.pack()

    etiqueta_direccion = Label(ventana_agregar_alumno, text="Dirección")
    etiqueta_direccion.pack()
    direccion = Entry(ventana_agregar_alumno)
    direccion.pack()

    # Función para agregar el nuevo alumno a la base de datos
    def agregar():
        # Conectarse a la base de datos
        client = MongoClient('mongodb://'+user.get()+':'+password.get()+'@localhost:27017/Base2')
        db = client.Base2
        alumnos_collection = db.Alumnos

        # Crear el nuevo alumno con los datos ingresados
        nuevo_alumno = {
            "nombre": nombre.get(),
            "apellidos": apellidos.get(),
            "fecha_nacimiento": fecha_nacimiento.get(),
            "carrera": carrera.get(),
            "estatus": estatus.get(),
            "email": email.get(),
            "telefono": telefono.get(),
            "direccion": direccion.get()
        }

        # Insertar el nuevo alumno en la base de datos
        result = alumnos_collection.insert_one(nuevo_alumno)

        # Cerrar la ventana de agregar alumno
        ventana_agregar_alumno.destroy()

    # Botón para agregar el nuevo alumno
    boton_agregar = Button(ventana_agregar_alumno, text="Agregar", command=agregar)
    boton_agregar.pack()

def agregar_carrera():
    # Crear ventana para agregar una nueva carrea
    ventana_agregar_carrera = Toplevel()
    ventana_agregar_carrera.title("Agregar Carrera")

    # Etiquetas y campos de texto para ingresar los datos de la carrera
    etiqueta_abreviatura = Label(ventana_agregar_carrera, text="Abreviatura")
    etiqueta_abreviatura.pack()
    carrera = Entry(ventana_agregar_carrera)
    carrera.pack()

    etiqueta_nombre_largo = Label(ventana_agregar_carrera, text="Nombre largo")
    etiqueta_nombre_largo.pack()
    nombre_largo = Entry(ventana_agregar_carrera)
    nombre_largo.pack()

    etiqueta_departamento = Label(ventana_agregar_carrera, text="Departamento")
    etiqueta_departamento.pack()
    departamento = Entry(ventana_agregar_carrera)
    departamento.pack()

    # Función para agregar la nueva carrera a la base de datos
    def agregar():
        # Conectarse a la base de datos
        client = MongoClient('mongodb://'+user.get()+':'+password.get()+'@localhost:27017/Base2')
        db = client.Base2
        carreras_collection = db.Carreras

        # Crear la nueva carrera con los datos ingresados
        nueva_carrera = {
            "abreviatura": carrera.get(),
            "nombre_largo": nombre_largo.get(),
            "departamento": departamento.get(),
        }

        # Insertar la nueva carerra en la base de datos
        result1 = carreras_collection.insert_one(nueva_carrera)

        # Cerrar la ventana de agregar carrera
        ventana_agregar_carrera.destroy()

    # Botón para agregar la nueva carrera
    boton_agregar1 = Button(ventana_agregar_carrera, text="Agregar", command=agregar)
    boton_agregar1.pack()

def eliminar_alumno():
    ventana_eliminar = Toplevel()
    ventana_eliminar.title("Eliminar Alumno")

    # Etiqueta y campo de entrada para el nombre del alumno a eliminar
    etiqueta_nombre = Label(ventana_eliminar, text="Nombre del alumno:")
    etiqueta_nombre.pack()
    campo_nombre = Entry(ventana_eliminar)
    campo_nombre.pack()

    # Función para eliminar el alumno y cerrar la ventana
    def eliminar():
        # Conectarse a la base de datos
        client = MongoClient('mongodb://'+user.get()+':'+password.get()+'@localhost:27017/Base2')
        db = client.Base2
        alumnos_collection = db.Alumnos

        nombre = campo_nombre.get()
        # Buscar el alumno en la base de datos
        alumno = alumnos_collection.find_one({"nombre": nombre})
        if alumno:
            # Eliminar el alumno de la base de datos
            alumnos_collection.delete_one({"_id": alumno["_id"]})
            mensaje = f"El alumno {nombre} ha sido eliminado."
        else:
            mensaje = f"No se encontró al alumno {nombre}."
        # Mostrar un mensaje al usuario
        messagebox.showinfo("Eliminar Alumno", mensaje)
        ventana_eliminar.destroy()

    # Botón para eliminar el alumno
    boton_eliminar = Button(ventana_eliminar, text="Eliminar", command=eliminar)
    boton_eliminar.pack()

    ventana_eliminar.mainloop()

def eliminar_carrera():
    ventana_eliminarC = Toplevel()
    ventana_eliminarC.title("Eliminar Carrera")

    # Etiqueta y campo de entrada para el nombre del alumno a eliminar
    etiqueta_Ab_carrea = Label(ventana_eliminarC, text="Abreviatura de la carrea")
    etiqueta_Ab_carrea.pack()
    campo_Ab_carrera = Entry(ventana_eliminarC)
    campo_Ab_carrera.pack()

    # Función para eliminar el alumno y cerrar la ventana
    def eliminar1():
        # Conectarse a la base de datos
        client = MongoClient('mongodb://'+user.get()+':'+password.get()+'@localhost:27017/Base2')
        db = client.Base2
        carreras_collection = db.Carreras

        abreviatura = campo_Ab_carrera.get()
        # Buscar el alumno en la base de datos
        carrea2 = carreras_collection.find_one({"abreviatura": abreviatura})
        if carrea2:
            # Eliminar el alumno de la base de datos
            carreras_collection.delete_one({"_id": carrea2["_id"]})
            mensaje = f"La carrera {abreviatura} ha sido eliminada."
        else:
            mensaje = f"No se encontró la carrera {abreviatura}."
        # Mostrar un mensaje al usuario
        messagebox.showinfo("Eliminar Alumno", mensaje)
        ventana_eliminarC.destroy()

    # Botón para eliminar el alumno
    boton_eliminar3 = Button(ventana_eliminarC, text="Eliminar", command=eliminar1)
    boton_eliminar3.pack()

    ventana_eliminarC.mainloop()
   
 # Función para buscar y mostrar los datos del alumno y permitir su edición

def editar_alumno():
    ventana_editar = Toplevel()
    ventana_editar.title("Editar Alumno")

    # Etiqueta y campo de entrada para el nombre del alumno a editar
    etiqueta_nombre = Label(ventana_editar, text="Nombre del alumno:")
    etiqueta_nombre.pack()
    campo_nombre = Entry(ventana_editar)
    campo_nombre.pack()

    # Función para buscar al alumno y mostrar sus datos en la ventana
    def buscar_alumno():
        nombre = campo_nombre.get()

        # Conexión a la base de datos MongoDB
        client = MongoClient('mongodb://'+user.get()+':'+password.get()+'@localhost:27017/Base2')
        db = client.Base2
        alumnos_collection = db.Alumnos

        # Buscar al alumno por nombre
        alumno = alumnos_collection.find_one({'nombre': nombre})

        if alumno is not None:
            # Crear etiquetas y campos de entrada para cada campo de información del alumno
            etiqueta_nombre1 = Label(ventana_editar, text="Nombre:")
            etiqueta_nombre1.pack()
            campo_nombre1 = Entry(ventana_editar)
            campo_nombre1.insert(END, alumno['nombre'])
            campo_nombre1.pack()

            etiqueta_apellidos = Label(ventana_editar, text="Apellidos:")
            etiqueta_apellidos.pack()
            campo_apellidos = Entry(ventana_editar)
            campo_apellidos.insert(END, alumno['apellidos'])
            campo_apellidos.pack()

            etiqueta_fecha_nacimiento = Label(ventana_editar, text="Fecha de Nacimiento:")
            etiqueta_fecha_nacimiento.pack()
            campo_fecha_nacimiento = Entry(ventana_editar)
            campo_fecha_nacimiento.insert(END, alumno['fecha_nacimiento'])
            campo_fecha_nacimiento.pack()

            etiqueta_carrera = Label(ventana_editar, text="Carrera:")
            etiqueta_carrera.pack()
            campo_carrera = Entry(ventana_editar)
            campo_carrera.insert(END, alumno['carrera'])
            campo_carrera.pack()

            etiqueta_estatus = Label(ventana_editar, text="Estatus:")
            etiqueta_estatus.pack()
            campo_estatus = Entry(ventana_editar)
            campo_estatus.insert(END, alumno['estatus'])
            campo_estatus.pack()

            etiqueta_direccion = Label(ventana_editar, text="Dirección:")
            etiqueta_direccion.pack()
            campo_direccion = Entry(ventana_editar)
            campo_direccion.insert(END, alumno['direccion'])
            campo_direccion.pack()

        # Función para guardar los cambios en los datos del alumno
        def guardar():
            # Actualizar los datos del alumno en la base de datos
            alumnos_collection.update_one(
                {'nombre': nombre},
                {'$set': {
                    'nombre': campo_nombre1.get(),
                    'apellidos': campo_apellidos.get(),
                    'fecha_nacimiento': campo_fecha_nacimiento.get(),
                    'carrera': campo_carrera.get(),
                    'estatus': campo_estatus.get(),
                    'direccion': campo_direccion.get()
                }}
            )

            # Cerrar la ventana
            ventana_editar.destroy()
        # Botón para guardar los cambios en los datos del
        boton_guardar = Button(ventana_editar, text="Guardar Cambios", command=guardar)
        boton_guardar.pack()
 
    # Botón para buscar al alumno y mostrar sus datos en la ventana
    boton_buscar = Button(ventana_editar, text="Buscar", command=buscar_alumno)
    boton_buscar.pack()
    ventana_editar.mainloop()

def editar_carrera():
    ventana_editar = Toplevel()
    ventana_editar.title("Editar Carrera")

    # Etiqueta y campo de entrada para la abreviatura de la carrea a editar
    etiqueta_abrev = Label(ventana_editar, text="Abreviatura de la carrera:")
    etiqueta_abrev.pack()
    campo_abrev = Entry(ventana_editar)
    campo_abrev.pack()

    # Función para buscar la carrera y mostrar sus datos en la ventana
    def buscar_alumno():
        Abreviatura1 = campo_abrev.get()

        # Conectarse a la base de datos
        client = MongoClient('mongodb://'+user.get()+':'+password.get()+'@localhost:27017/Base2')
        db = client.Base2
        carreras_collection = db.Carreras

        # Buscar la carrera por su abreciatura
        carrea = carreras_collection.find_one({'abreviatura': Abreviatura1})

        if carrea is not None:
            # Crear etiquetas y campos de entrada para cada campo de información de la carrera
            etiqueta_ab1 = Label(ventana_editar, text="Abreviatura:")
            etiqueta_ab1.pack()
            campo_ab1 = Entry(ventana_editar)
            campo_ab1.insert(END, carrea['abreviatura'])
            campo_ab1.pack()

            etiqueta_nombre_largo = Label(ventana_editar, text="Nombre Largo:")
            etiqueta_nombre_largo.pack()
            campo_nom_largo = Entry(ventana_editar)
            campo_nom_largo.insert(END, carrea['nombre_largo'])
            campo_nom_largo.pack()

            etiqueta_departamento = Label(ventana_editar, text="Departamento:")
            etiqueta_departamento.pack()
            campo_departamento = Entry(ventana_editar)
            campo_departamento.insert(END, carrea['departamento'])
            campo_departamento.pack()

        # Función para guardar los cambios en los datos de la carrera
        def guardar():
            # Actualizar los datos del alumno en la base de datos
            carreras_collection.update_one(
                {'abreviatura': Abreviatura1},
                {'$set': {
                    'abreviatura': campo_ab1.get(),
                    'nombre_largo': campo_nom_largo.get(),
                    'fecha_nacimiento': campo_departamento.get(),
                }}
            )

            # Cerrar la ventana
            ventana_editar.destroy()
        # Botón para guardar los cambios en los datos de la carrer
        boton_guardar1 = Button(ventana_editar, text="Guardar Cambios", command=guardar)
        boton_guardar1.pack()
 
    # Botón para buscar la carrera y mostrar sus datos en la ventana
    boton_buscar1 = Button(ventana_editar, text="Buscar", command=buscar_alumno)
    boton_buscar1.pack()
    ventana_editar.mainloop()

def iniciar_sesion():
    # Conectarse a la base de datos
    client = MongoClient('mongodb://'+user.get()+':'+password.get()+'@localhost:27017/Base2')
    db = client.Base2
    try:
        db.command('ping')
    except:
        # Mostrar mensaje de error si no se puede conectar
        mensaje_error = Label(ventana_inicial, text="Error: No se pudo conectar a la base de datos")
        mensaje_error.pack()
    else:
        # Mostrar mensaje de conexión exitosa y botón "Alumnos"
        mensaje_conexion = Label(ventana_inicial, text="Conexión exitosa")
        mensaje_conexion.pack()
        #Botón de mostrar alumnos
        boton_alumnos = Button(ventana_inicial, text="Ver Alumnos", command=mostrar_alumnos)
        boton_alumnos.pack()
        # Botón "Agregar Alumno"
        boton_agregar_alumno = Button(ventana_inicial, text="Agregar Alumno", command=agregar_alumno)
        boton_agregar_alumno.pack()
        #Botón "Eliminar Alumno"
        boton_eliminar_alumno = Button(ventana_inicial, text="Eliminar Alumno", command=eliminar_alumno)
        boton_eliminar_alumno.pack()
        #Botón "Editar Alumno"
        boton_editar_alumno = Button(ventana_inicial, text="Editar Alumno", command=editar_alumno)
        boton_editar_alumno.pack()
        #Botón de Mostrar carreras
        boton_carreras = Button(ventana_inicial, text="Ver Carreras", command=mostrar_carreras)
        boton_carreras.pack()
        #Botón de Agregar carreras
        boton_agregar_carreras = Button(ventana_inicial, text="Agregar carrera", command=agregar_carrera)
        boton_agregar_carreras.pack()
        #Botón de Eliminar carreras
        boton_eliminar_carreras = Button(ventana_inicial, text="Eliminar carrera", command=eliminar_carrera)
        boton_eliminar_carreras.pack()
        #Botón de Eliminar carreras
        boton_editar_carreras = Button(ventana_inicial, text="Editar carrera", command=editar_carrera)
        boton_editar_carreras.pack()

# Ventana de inicio de sesión
ventana_inicial = Tk()
ventana_inicial.title("Iniciar Sesión")

# Etiquetas y campos de texto para usuario y contraseña
etiqueta_user = Label(ventana_inicial, text="Usuario")
etiqueta_user.pack()
user = Entry(ventana_inicial)
user.pack()
etiqueta_password = Label(ventana_inicial, text="Contraseña")
etiqueta_password.pack()
password = Entry(ventana_inicial, show="*")
password.pack()

# Botón "Iniciar Sesión"
boton_iniciar_sesion = Button(ventana_inicial, text="Iniciar Sesión", command=iniciar_sesion)
boton_iniciar_sesion.pack()
ventana_inicial.mainloop()