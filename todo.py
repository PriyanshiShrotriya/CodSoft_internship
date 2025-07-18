from tkinter import *
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task == "":
        messagebox.showwarning("Warning!", "Please enter a task.")
    else:
        tasks.append(task)
        listbox_tasks.insert(END, task)
        entry_task.delete(0, END)

def delete_task():
    selected = listbox_tasks.curselection()
    if not selected:
        messagebox.showwarning("Warning!", "Please select a task to delete.")
    else:
        listbox_tasks.delete(selected[0]) 
        del tasks[selected[0]]

def mark_done():
    selected=listbox_tasks.curselection()
    if selected:
        task=tasks[selected[0]] + " [Done] "
        tasks[selected[0]] = task
        listbox_tasks.delete(selected[0])
        listbox_tasks.insert(selected[0],task)


# main window
window = Tk()
window.title("To-Do List App")
window.geometry("350x450")
window["bg"] = "black"

tasks = []
# Frame for the listbox and scrollbar
frame_tasks = Frame(window)
frame_tasks.pack(pady=10)

# Listbox to display tasks
listbox_tasks = Listbox(frame_tasks, width=35, height=15, bg="pink")
listbox_tasks.pack(side=LEFT, fill=BOTH)

# Scrollbar for the listbox
scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

# Entry box for new tasks
entry_task = Entry(window, width=30)
entry_task.pack(pady=10)

# Buttons 
button_add_task = Button(window, text="Add Task", font="timesnewroman 10 bold", width=15, command=add_task, bg="pink")
button_add_task.pack(pady=5)

button_delete_task = Button(window, text="Delete Task", font="timesnewroman 10 bold",width=15, command=delete_task, bg="pink")
button_delete_task.pack(pady=5)

done_btn = Button(window,text = "Marks as Done",font="timesnewroman 10 bold", width = 15, command = mark_done, bg="pink")
done_btn.pack(pady=5)

window.mainloop()