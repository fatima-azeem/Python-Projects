import pickle
import tkinter 
import tkinter.messagebox 

root = tkinter.Tk()
root.title("TO-DO-LIST")

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_task.insert(tkinter.END, task)
        entry_task.delete(0, tkinter.END)
    else: 
        tkinter.messagebox.showwarning(title="warning!", message="You must enter a task.")  

def delete_task():
    try:
        task_index = listbox_task.curselection()[0]
        listbox_task.delete(task_index)
    except:
        tkinter.messagebox.showwarning(title="warning!", message="You must select a task.")   



# Create GUI
frame_tasks = tkinter.Frame(root)
frame_tasks.pack()

listbox_task = tkinter.Listbox(frame_tasks, height=15, width=55)
listbox_task.pack(side=tkinter.LEFT)

scrollbar_task = tkinter.Scrollbar(frame_tasks)
scrollbar_task.pack(side= tkinter.RIGHT, fill=tkinter.Y)

listbox_task.config(yscrollcommand = scrollbar_task.set)
scrollbar_task.config(command=listbox_task.yview)

entry_task = tkinter.Entry(root, width=50)
entry_task.pack()

button_add_task = tkinter.Button(root, text='Add Task', width=53, height=3, command= add_task)
button_add_task.pack()

button_delete_task = tkinter.Button(root, text='Delete Task', width=53, height=3, command= delete_task)
button_delete_task.pack()






root.mainloop()
