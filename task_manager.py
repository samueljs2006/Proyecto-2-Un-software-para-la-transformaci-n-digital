import json
import os
import tkinter as tk
from tkinter import messagebox
import subprocess

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def get_next_id(tasks):
    return max((task["id"] for task in tasks), default=0) + 1

def add_task():
    task_description = task_entry.get().strip()
    if not task_description:
        messagebox.showerror("Error", "La descripción no puede estar vacía.")
        return
    tasks = load_tasks()
    new_task = {"id": get_next_id(tasks), "task": task_description, "completed": False, "tags": []}
    tasks.append(new_task)
    save_tasks(tasks)
    task_entry.delete(0, tk.END)
    update_task_list()

def complete_task():
    try:
        selected_item = task_listbox.curselection()[0]
        tasks = load_tasks()
        tasks[selected_item]["completed"] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Selecciona una tarea para completar.")

def delete_task():
    try:
        selected_item = task_listbox.curselection()[0]
        tasks = load_tasks()
        del tasks[selected_item]
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Selecciona una tarea para eliminar.")

def update_task_list():
    task_listbox.delete(0, tk.END)
    tasks = load_tasks()
    for task in tasks:
        status = "✅" if task["completed"] else "⏳"
        color = "#90EE90" if task["completed"] else "#FFFFE0"  # Verde claro si está completada, amarillo si no
        task_listbox.insert(tk.END, f"{task['task']} {status}")
        task_listbox.itemconfig(tk.END, {'bg': color})

def is_ollama_available():
    """Verifica si Ollama está disponible en el sistema."""
    try:
        result = subprocess.run(["ollama", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def activate_ai():
    """Activar IA para autoetiquetar tareas."""
    if not is_ollama_available():
        messagebox.showerror("Error", "Ollama no está disponible en el sistema.")
        return

    tasks = load_tasks()
    for task in tasks:
        task["tags"] = get_task_tags_from_ai(task["task"])
    save_tasks(tasks)
    update_task_list()

def get_task_tags_from_ai(task_description):
    """Obtiene etiquetas para una tarea utilizando Ollama."""
    try:
        result = subprocess.run(
            ["ollama", "run", "model_name", "--input", task_description],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            output = result.stdout.strip()
            if "urgente" in output.lower():
                return ["Urgente", "Alta Prioridad"]
            elif "reunión" in output.lower():
                return ["Reunión", "Trabajo"]
            else:
                return ["General"]
        else:
            return ["Sin Etiquetas"]
    except FileNotFoundError:
        print("Ollama no está instalado o no es accesible.")
        return ["Error"]
    except Exception as e:
        print(f"Error al ejecutar Ollama: {e}")
        return ["Error"]

def recommend_task_based_on_mood():
    """Recomienda tareas basadas en el estado de ánimo y prioridades."""
    tasks = load_tasks()
    tasks_sorted = sorted(tasks, key=lambda x: "Urgente" in x.get("tags", []), reverse=True)
    recommended_task = tasks_sorted[0] if tasks_sorted else None
    if recommended_task:
        messagebox.showinfo("Recomendación", f"Te recomendamos empezar con: {recommended_task['task']}")
    else:
        messagebox.showinfo("Recomendación", "No hay tareas urgentes para recomendar.")

def main():
    global root, task_entry, task_listbox
    
    root = tk.Tk()
    root.title("Gestor de Tareas")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    task_entry = tk.Entry(frame, width=40)
    task_entry.pack(side=tk.LEFT, padx=10)

    add_button = tk.Button(frame, text="Agregar", command=add_task, bg="#4CAF50", fg="white")
    add_button.pack(side=tk.LEFT)

    task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
    task_listbox.pack(pady=10)

    complete_button = tk.Button(root, text="Completar", command=complete_task, bg="#008CBA", fg="white")
    complete_button.pack(side=tk.LEFT, padx=10)

    delete_button = tk.Button(root, text="Eliminar", command=delete_task, bg="#f44336", fg="white")
    delete_button.pack(side=tk.RIGHT, padx=10)

    ai_button = tk.Button(root, text="Activar IA", command=activate_ai, bg="#FF9800", fg="white")
    ai_button.pack(pady=5)

    recommend_button = tk.Button(root, text="Recomendar Tarea", command=recommend_task_based_on_mood, bg="#9C27B0", fg="white")
    recommend_button.pack(pady=5)

    update_task_list()
    root.mainloop()

if __name__ == "__main__":
    main()