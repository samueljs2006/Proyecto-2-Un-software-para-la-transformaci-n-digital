import json
import os

# Archivo donde se almacenarán las tareas
TASKS_FILE = "tasks.json"

# Función para cargar las tareas desde el archivo JSON
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

# Función para guardar las tareas en el archivo JSON
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Función para agregar una tarea
def add_task(task_description):
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {"id": task_id, "task": task_description, "completed": False}
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Tarea '{task_description}' agregada exitosamente.")

# Función para marcar una tarea como completada
def complete_task(task_id):
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            save_tasks(tasks)
            print(f"Tarea {task_id} marcada como completada.")
            return
    print(f"Tarea con ID {task_id} no encontrada.")

# Función para eliminar una tarea
def delete_task(task_id):
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Tarea con ID {task_id} eliminada.")

# Función para mostrar todas las tareas
def show_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No hay tareas en la lista.")
    else:
        for task in tasks:
            status = "Completada" if task["completed"] else "Pendiente"
            print(f"ID: {task['id']} - {task['task']} ({status})")

# Función principal para mostrar el menú y recibir la acción del usuario
def main():
    while True:
        print("\n--- Gestión de Tareas ---")
        print("1. Ver tareas")
        print("2. Agregar tarea")
        print("3. Marcar tarea como completada")
        print("4. Eliminar tarea")
        print("5. Salir")
        
        choice = input("Selecciona una opción: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            task_description = input("Introduce la descripción de la tarea: ")
            add_task(task_description)
        elif choice == "3":
            task_id = int(input("Introduce el ID de la tarea a marcar como completada: "))
            complete_task(task_id)
        elif choice == "4":
            task_id = int(input("Introduce el ID de la tarea a eliminar: "))
            delete_task(task_id)
        elif choice == "5":
            print("Saliendo...")
            break
        else:
            print("Opción no válida, por favor elige una opción válida.")

# Ejecutar la aplicación
if __name__ == "__main__":
    main()
