# This list will store our tasks
tasks = []

# Load tasks from file when program starts
try:
    file = open("tasks.txt", "r")
    for line in file:
        tasks.append(line.strip())
    file.close()
except:
    print("No saved tasks found. Starting fresh.")

# Keep running until user chooses to exit
while True:
    print("\n--- My To-Do List ---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")
    
    choice = input("Pick a number: ")
    
    if choice == "1":
        new_task = input("Type your task: ")
        tasks.append(new_task)
        print("Task added!")
        
    elif choice == "2":
        print("\nYour tasks:")
        if len(tasks) == 0:
            print("No tasks yet")
        else:
            for i in range(len(tasks)):
                print(i + 1, ".", tasks[i])
                
    elif choice == "3":
        for i in range(len(tasks)):
            print(i + 1, ".", tasks[i])
        num = int(input("Which task number to delete? "))
        if num > 0 and num <= len(tasks):
            tasks.pop(num - 1)
            print("Task deleted!")
        else:
            print("That number is not in the list")
            
    elif choice == "4":
        # Save tasks to file before exiting
        file = open("tasks.txt", "w")
        for task in tasks:
            file.write(task + "\n")
        file.close()
        print("Tasks saved. Bye!")
        break
        
    else:
        print("Please pick 1, 2, 3, or 4")