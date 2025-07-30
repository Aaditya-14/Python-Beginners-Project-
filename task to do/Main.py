task=[]

task_no=int(input("Enter the number of task you want to add :"))

def add_task():
    for i in range(1,task_no+1):
        Tasks=input(f"Enter the {i} task:")
        task.append(Tasks)
        
        
add_task()



while True:
    Task_edit = int(input("\n--------------Menu------------\n"
                      "1. Add a task\n"
                      "2. Delete a task\n"
                      "3. View all tasks\n"
                      "4. Update tasks \n"
                      "5. Exit\n"
                      "Enter your choice (1-4): "))
    if Task_edit==1:
        add=(input("Enter the name of task you want to add: "))
        task.append(add)
        print("New task added")
        
    elif Task_edit==2:
        delete=input("Enter the name of task tha you want to delete :")
        if delete in task:
            task.remove(delete)
            print("Task sucessfully removed")
        else:
            print("No Task found")
    elif Task_edit==3:
        print("---------List of Task----------")
        for t in task:
            print("-",t)
    elif Task_edit == 4:
        update = input("Enter the name of the task you want to update: ")
        if update in task:
            new_update = input("Enter the new task name to update: ")
            index = task.index(update)
            task[index] = new_update
            print(f"✅ Task '{update}' has been updated to '{new_update}'")
        else:
            print("⚠️ Task not found.")

    elif Task_edit==5:
        print("ok i am exiting bye bye")
        break
    else:
        print("please enter valid varaible")
        break
    