"""
Task Manager Application with AI Integration

A GUI-based task management system with automatic AI tagging capabilities using Ollama.
"""

import json
import os
import tkinter as tk
from tkinter import messagebox
import subprocess
import requests

TASKS_FILE = "tasks.json"

def get_task_tags_from_ai(task_description):
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "mistral", "prompt": f"Etiqueta esta tarea: {task_description}"},
            timeout=5
        )
        return response.json().get("tags", ["General"])
    except requests.exceptions.RequestException:
        return ["Error"]

def load_tasks():
    """
    Load tasks from the JSON file.
    
    Returns:
        list: A list of task dictionaries. Returns empty list if file doesn't exist or is invalid.
    """
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []
    return []

def save_tasks(tasks):
    """
    Save tasks to the JSON file.
    
    Args:
        tasks (list): List of task dictionaries to save.
    """
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def get_next_id(tasks):
    """
    Generate the next available task ID.
    
    Args:
        tasks (list): List of existing tasks.
        
    Returns:
        int: The next available task ID.
    """
    return max((task["id"] for task in tasks), default=0) + 1

def add_task():
    """Add a new task from the input field to the task list."""
    task_description = task_entry.get().strip()
    if not task_description:
        messagebox.showerror("Error", "Task description cannot be empty.")
        return
    tasks = load_tasks()
    new_task = {
        "id": get_next_id(tasks),
        "task": task_description,
        "completed": False,
        "tags": []
    }
    tasks.append(new_task)
    save_tasks(tasks)
    task_entry.delete(0, tk.END)
    update_task_list()

def complete_task():
    """Mark the selected task as completed."""
    try:
        selected_item = task_listbox.curselection()[0]
        tasks = load_tasks()
        tasks[selected_item]["completed"] = True
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Select a task to complete.")

def delete_task():
    """Delete the selected task from the list."""
    try:
        selected_item = task_listbox.curselection()[0]
        tasks = load_tasks()
        del tasks[selected_item]
        save_tasks(tasks)
        update_task_list()
    except IndexError:
        messagebox.showerror("Error", "Select a task to delete.")

def update_task_list():
    """Update the task listbox with current tasks and their status."""
    task_listbox.delete(0, tk.END)
    tasks = load_tasks()
    for task in tasks:
        status = "✅" if task["completed"] else "⏳"
        color = "#90EE90" if task["completed"] else "#FFFFE0"
        task_listbox.insert(tk.END, f"{task['task']} {status}")
        task_listbox.itemconfig(tk.END, {'bg': color})

def is_ollama_available():
    """
    Check if Ollama is available on the system.
    
    Returns:
        bool: True if Ollama is installed and accessible, False otherwise.
    """
    try:
        result = subprocess.run(["ollama", "--version"], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def activate_ai():
    """Activate AI to auto-tag all tasks."""
    if not is_ollama_available():
        messagebox.showerror("Error", "Ollama is not available on the system.")
        return

    tasks = load_tasks()
    for task in tasks:
        task["tags"] = get_task_tags_from_ai(task["task"])
    save_tasks(tasks)
    update_task_list()

def get_task_tags_from_ai(task_description):
    """
    Get tags for a task using Ollama AI.
    
    Args:
        task_description (str): The task description to analyze.
        
    Returns:
        list: List of tags for the task.
    """
    try:
        result = subprocess.run(
            ["ollama", "run", "model_name", "--input", task_description],
            capture_output=True, text=True
        )
        if result.returncode == 0:
            output = result.stdout.strip()
            if "urgente" in output.lower():
                return ["Urgent", "High Priority"]
            elif "reunión" in output.lower():
                return ["Meeting", "Work"]
            else:
                return ["General"]
        else:
            return ["No Tags"]
    except FileNotFoundError:
        print("Ollama is not installed or accessible.")
        return ["Error"]
    except Exception as e:
        print(f"Error running Ollama: {e}")
        return ["Error"]

def recommend_task_based_on_mood():
    """Recommend tasks based on mood and priority tags."""
    tasks = load_tasks()
    tasks_sorted = sorted(tasks, key=lambda x: "Urgent" in x.get("tags", []), reverse=True)
    recommended_task = tasks_sorted[0] if tasks_sorted else None
    if recommended_task:
        messagebox.showinfo("Recommendation", f"We recommend starting with: {recommended_task['task']}")
    else:
        messagebox.showinfo("Recommendation", "No urgent tasks to recommend.")

def main():
    """Initialize and run the main application window."""
    global root, task_entry, task_listbox
    
    root = tk.Tk()
    root.title("Task Manager")

    frame = tk.Frame(root)
    frame.pack(pady=10)

    task_entry = tk.Entry(frame, width=40)
    task_entry.pack(side=tk.LEFT, padx=10)

    add_button = tk.Button(frame, text="Add", command=add_task, bg="#4CAF50", fg="white")
    add_button.pack(side=tk.LEFT)

    task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
    task_listbox.pack(pady=10)

    complete_button = tk.Button(root, text="Complete", command=complete_task, bg="#008CBA", fg="white")
    complete_button.pack(side=tk.LEFT, padx=10)

    delete_button = tk.Button(root, text="Delete", command=delete_task, bg="#f44336", fg="white")
    delete_button.pack(side=tk.RIGHT, padx=10)

    ai_button = tk.Button(root, text="Activate AI", command=activate_ai, bg="#FF9800", fg="white")
    ai_button.pack(pady=5)

    recommend_button = tk.Button(root, text="Recommend Task", command=recommend_task_based_on_mood, bg="#9C27B0", fg="white")
    recommend_button.pack(pady=5)

    update_task_list()
    root.mainloop()

if __name__ == "__main__":
    main()