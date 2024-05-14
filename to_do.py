import tkinter as tk
from tkinter import ttk, messagebox
from ttkbootstrap import Style
import json

class TodoList(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Simple Todo List")
        self.geometry("400x500")
        style = Style(theme="flatly")
        style.configure("Custon.TEntry", foreground="gray")

        # Create input field for adding tasks
        self.input = ttk.Entry(self, font=("TkDefaultFont", 16), width=30, style="Custon.TEntry")
        self.input.pack(pady=10)

        # Set placeholder for input field
        self.input.insert(0, "Enter your todo here...")

        # Bind event to clear placeholder when input field is clicked
        self.input.bind("<FocusIn>", self.clear_placeholder)
        
        # Bind event to restore placeholder when input field loses focus
        self.input.bind("<FocusOut>", self.restore_placeholder)

        # Create button for adding tasks
        ttk.Button(self, text="Add", command=self.add_task).pack(pady=5)

        # Create listbox to display added tasks
        self.list = tk.Listbox(self, font=("TkDefaultFont", 16), height=10, selectmode=tk.NONE)
        self.list.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        # Create buttons for marking tasks as done or deleting them
        ttk.Button(self, text="Done", style="success.TButton",command=self.mark_done).pack(side=tk.LEFT, padx=10, pady=10)
        ttk.Button(self, text="Delete", style="danger.TButton",command=self.delete_task).pack(side=tk.RIGHT, padx=10, pady=10)
        
        # Create buttton for displaying task statistics
        ttk.Button(self, text="View Stats", style="info.TButton",command=self.view_stats).pack(side=tk.BOTTOM, pady=10)
        self.load_tasks()
    
    def view_stats(self):
        done_count = 0
        total_count = self.list.size()
        for i in range(total_count):
            if self.list.itemcget(i, "fg") == "green":
                done_count += 1
        messagebox.showinfo("Task Statistics", f"Total tasks: {count}\nCompleted tasks: {done_count}")

    def add_task(self):
        task = self.task_input.get()
        if task != "Enter your todo here...":
            self.list.insert(tk.END, task)
            self.list.itemconfig(tk.END, fg="orange")
            self.input.delete(0, tk.END)
            self.save_tasks()

    def mark_done(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.list.itemconfig(task_index, fg="green")
            self.save_tasks()
    
    def delete_task(self):
        task_index = self.task_list.curselection()
        if task_index:
            self.list.delete(task_index)
            self.save_tasks()
    
    def clear_placeholder(self, event):
        if self.input.get() == "Enter your todo here...":
            self.input.delete(0, tk.END)
            self.input.configure(style="TEntry")

    def restore_placeholder(self, event):
        if self.input.get() == "":
            self.input.insert(0,"Enter your todo here...")
            self.input.configure(style="Custom.TEntry")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                data = json.load(f)
                for task in data:
                    self.list.insert(tk.END, task["text"])
                    self.list.itemconfig(tk.END, fg=task["color"])
        except FileNotFoundError:
            pass
    
    def save_tasks(self):
        data = []
        for i in range(self.list.size()):
            text = self.list.get(i)
            color = self.list.itemcget(i, "fg")
            data.append({"text": text, "color": color})
        with open("tasks.json", "w") as f:
            json.dump(data, f)

if __name__ == '__main__':
    app = TodoList()
    app.mainloop()
