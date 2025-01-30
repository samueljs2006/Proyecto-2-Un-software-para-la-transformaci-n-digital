# Proyecto-2-Un-software-para-la-transformaci-n-digital
Se ejecuta con python task_manager.py

La idea que propuse inicialmente es crear una aplicación de gestión de tareas utilizando Python. Esta aplicación sería una herramienta sencilla para que los usuarios puedan gestionar sus tareas diarias o proyectos. La aplicación tiene un menú de línea de comandos (CLI) y permite a los usuarios interactuar con él para agregar, ver, completar y eliminar tareas.


#Objetivo del software:

La idea es construir una herramienta funcional de gestión de tareas que pueda ser utilizada en cualquier entorno que soporte Python (como una computadora personal o un servidor), donde los usuarios puedan:

-Ver todas sus tareas actuales: Esto incluye ver el estado de cada tarea (pendiente o completada).
-Agregar nuevas tareas: Permite a los usuarios agregar nuevas tareas a la lista, describiendo brevemente lo que necesitan hacer.
-Marcar tareas como completadas: Los usuarios pueden actualizar el estado de las tareas para reflejar si ya están hechas.
-Eliminar tareas: Los usuarios pueden borrar tareas que ya no necesiten o hayan completado.

#Detalles de la implementación:

1.Interfaz de usuario:

-Se utilizará un menú de línea de comandos (CLI), lo que significa que el usuario interactuará con el software a través de texto en la terminal o consola.
-El menú le ofrecerá varias opciones, como ver tareas, agregar nuevas tareas, marcar tareas como completadas, eliminar tareas y salir de la aplicación.

2.Almacenamiento de datos:

-Las tareas se almacenarán en un archivo JSON. Este es un formato de almacenamiento común y fácil de leer/escribir en Python, lo que permitirá a la aplicación mantener un registro persistente de las tareas, incluso después de que se cierre o se reinicie el programa.
-El archivo tasks.json almacenará una lista de diccionarios, donde cada diccionario representará una tarea con su ID único, descripción y estado de completado.

3.Funcionalidades principales:

-Ver tareas: El usuario puede ver todas las tareas con su estado actual, ya sea pendiente o completada. Cada tarea tendrá un identificador único para facilitar la manipulación.

-Agregar tarea: Los usuarios pueden agregar nuevas tareas ingresando una descripción. La tarea será asignada con un ID único y será marcada como "pendiente" inicialmente.

-Marcar tarea como completada: El usuario puede ingresar el ID de la tarea que desea marcar como completada. La aplicación actualizará el estado de la tarea para reflejar que está terminada.

-Eliminar tarea: El usuario puede eliminar una tarea que ya no necesite. Esto se hace ingresando el ID de la tarea que se desea borrar.

4.Manejo de archivos:

-El programa verificará si el archivo tasks.json existe. Si no existe, lo creará automáticamente al momento de agregar la primera tarea.
-Las tareas se cargarán desde el archivo cada vez que se inicie la aplicación para garantizar que no se pierdan, y se guardarán de nuevo cada vez que se agregue, modifique o elimine una tarea.

#Flujo de trabajo del programa:

1.Inicio: Cuando el usuario ejecute el programa, verá un menú con las siguientes opciones:

-Ver tareas
-Agregar tarea
-Marcar tarea como completada
-Eliminar tarea
-Salir

2.Interacción con el menú:

-El usuario elige una opción ingresando un número (por ejemplo, "1" para ver tareas, "2" para agregar una tarea, etc.).
-Dependiendo de la opción elegida, el programa ejecutará una de las funciones (como mostrar las tareas, agregar una tarea nueva, etc.).
-Si el usuario decide salir, el programa terminará.

3.Persistencia de datos:

-Las tareas estarán almacenadas en un archivo tasks.json que se actualizará automáticamente cada vez que se realice una modificación.

#Posibles mejoras y expansión:

Este software es solo un punto de partida. Aquí algunas ideas para ampliarlo en el futuro:

-Interfaz gráfica (GUI): Usar Tkinter o PyQt para crear una interfaz visual en lugar de una interfaz de línea de comandos.
-Soporte para fechas: Permitir a los usuarios agregar fechas límite a las tareas.
-Prioridades: Poder asignar diferentes niveles de prioridad (alta, media, baja) a las tareas.
-Recordatorios y notificaciones: Enviar recordatorios al usuario cuando una tarea esté próxima a vencer.
