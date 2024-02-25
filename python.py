# Todo App 
from typing import Any
from datetime import datetime
import pandas as pd

class App:
    def __init__(self)->None:
        self.tasks: list[dict[str,Any]] = []
        
    def addTask(self, task:str)->None:
        newTask:dict[str,Any] = {"id":str(len(self.tasks)+1),"task":task,"date":datetime.now().strftime("%y/%m/%d/%I:%M %p"),"lastUpdated":"Not Updated"}
        if task.strip() != "":
            self.tasks.append(newTask)
            print("Task Added Successfully")
        else:
            raise Exception("Task is empty")    
    def viewTasks(self)->None:
        if self.tasks:
            tasks_df: pd.DataFrame = pd.DataFrame(self.tasks)
            print(tasks_df)        
        else:
            print("No tasks available.")
    def removeTask(self,id:str)->None:
        for item in self.tasks:
            if item["id"] == id:
                self.tasks.remove(item)
                print("Task Removed Successfully")
            else:
                print("Invalid Id")
    def update_task(self, newTask:str,id:str)->None:
        for item in self.tasks:
            if item["id"] == id:
                item["task"] = newTask
                item["lastUpdated"] = datetime.now().strftime("%y/%m/%d/%I:%M %p")
                print("Task with ID {} updated successfully.".format(id))
                break
            else:
                print("Task with ID {} not found.".format(id))

    
app:App=App()    
while True:
    print("\n===== Task Management System =====")
    print("1. Add Task")
    print("2. Delete Task")
    print("3. Update Task")
    print("4. Display Tasks")
    print("5. Exit")

    choice = input("Enter your choice: ")
    match choice:
        case '1':
            task=input("Enter Task:  ")
            app.addTask(task)
        case '2':
            id=input("Enter Id:  ")
            app.removeTask(id)
        case '3':
            id=input("Enter Id:  ")
            newTask=input("Enter Task To Update:  ")
            app.update_task(newTask, id)  
        case '4':
            app.viewTasks()
        case '5':
            break              
        case _:
            print("Invalid Choice\n Please Enter A Valid Choice")        