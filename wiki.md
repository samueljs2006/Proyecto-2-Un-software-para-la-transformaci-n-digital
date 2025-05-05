# Wiki and Devlog: AI-Powered Task Manager

## Developer Documentation

### Overview
Desktop application for task management with:
-  Create/delete tasks
-  AI-powered auto-tagging 
-  Smart recommendations  

### Project Structure
```bash
task_manager/
├── tasks.json          # Task database
└── task_manager.py     # Logic + GUI
```
##  Dependencies

### Essentials
| Component | Minimum Version| Installation |
|------------|----------------|-------------|
| Python     | 3.7            | `sudo apt install python3` |
| Tkinter    | -              | Included with Python |
| ollama   | -              | optional |

##   Quick Setup
1. Install Python 3.7+
``` bash
sudo apt-get install python3
```
2.Verify Ollama (optional):
```bash
ollama --version
```
##  Key Features

### Basic Management
```python
def add_task():
    """Adds a task with empty field validation"""
    
def complete_task():
    """Marks a task as ✅ completed"""
```
### SAI System
```
graph TD
    A[Activate AI] --> B{Is Ollama installed?}
    B -->|Yes| C[Tag tasks]
    B -->|No| D[Show error]
    C --> E[Update interface]
```
![alt text](deepseek_mermaid_20250502_feaaae.png)

### Recommendation Algorithm
1. Filters tasks with "Urgent" tag
2. Sorts by age
3. Selects the most prioritized task

##  Graphical Interface
| Component | Description | Color |
|------------|----------------|-------------|
| Task list	| Shows status (✅/⏳) |Green/Yellow|
| "Add" button	| Adds new task	| #4CAF50 |
| AI button	|Activates auto-tagging	|#FF9800|

##  Devlog

### v1.0 - Current
- Stable basic functionalities
- Basic Ollama integration
### Roadmap
- Multi-user support
- Cloud sync
- Improved AI analysis

##   How to Contribute
```bash 
git clone https://github.com/your_repo/task_manager.git
cd task_manager
# Create a new branch:
git checkout -b feature/short_description
```
 **Full guide**: [CONTRIBUTING.md](/CONTRIBUTING.md)

##  DevLog: Building a Task Manager with Integrated AI

Today, I’m excited to share the development journey of my AI-Powered Task Manager, a tool designed to boost productivity by organizing tasks and leveraging AI for automatic tagging.

### 🔹 Stage 1: Core Design and Functionality
The project began with implementing the essential features of a task manager:
- Add tasks: Allows users to input new tasks and save them in a JSON file.
-  Complete/Delete tasks: Mark tasks as done (✅) or remove them from the list.
- Data persistence: Tasks are stored in tasks.json to maintain state between sessions.

Tech stack: Python, Tkinter (for the GUI), JSON.

### 🔹 Stage 2: AI Integration with Ollama
To add value, I integrated Ollama, a tool for running local language models. The AI is used for:
- Auto-tagging tasks: Analyzes task descriptions and assigns tags like "Urgent," "Meeting," or "General."
- Availability check: The system verifies if Ollama is installed before enabling AI features.

Example:
- If a task contains "meeting," the AI tags it as ["Meeting", "Work"].
- If the task includes "urgent," it assigns ["Urgent", "High Priority"].

### 🔹 Stage 3: Task Recommendations
To help prioritize work, I added a recommendation system based on:
- Simulated user mood.
- Priority tags: Tasks marked as "Urgent" appear first.

Outcome:
- The interface suggests the most urgent task to the user.

### 🔹 Stage 4: User-Friendly Interface
The GUI was designed to be intuitive and visually appealing:
- Colors: Completed tasks in light green (✅), pending tasks in yellow (⏳).
- Highlighted buttons:
    - Activate AI (orange) for auto-tagging.
    - Recommend Task (purple) for suggestions.

Here is the link to LinkedIn

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Contactar-%230A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/samuel-jiménez-8b6a33363) 

### 🔹 Challenges and Learnings
1. Ollama Integration: Ensuring the system works even if Ollama isn’t installed required robust error handling.
2. Data Persistence: Using JSON simplified storage, but handling edge cases (e.g., corrupt files) was key.
3. Intuitive UI: Tkinter enabled rapid development, though customization options were limited.

### 🔹 Next Steps
- Enhance the AI model: Use a more advanced model for contextual tagging.
- Cloud sync: Enable access to tasks across multiple devices.
- Notifications: Add reminders for urgent tasks.


