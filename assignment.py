#  Welcome to the To-Do List App!

        # Menu:
        # 1. Add a task
        # 2. View tasks
        # 3. Mark a task as complete
        # 4. Delete a task
        # 5. Quit

task = []

def add_tasks():
    task_name = input("Enter the new task name:")
    task.append(task_name)
    print("New task was added successfully.")
def view_tasks():
    if len(task_name) == 0:
          print("No tasks were added.")
    else:
          print("List your tasks:")
          for int, task_name in enumerate(task):
                print(f"{int + 1}. {task_name}")
def completed_tasks():
     task_completed = input("Is the task completed? (yes/no):")
     if task_completed == "yes":
          print("Task is completed.")
     else:
          print("Task is incomplete.")
def delete_tasks():
        if len(task_name) == 0:
            print("There are no tasks to delete.")
        else:
            print("Pleas enter a task to delete:")
        for int, task_name in enumerate(task):
             print(f"{int + 1}. {task_name}")
        choice = int(input("Enter the task number to delete:"))


        if 0 < choice <= len(task_name):
             del task_name [choice -1]
             print("You deleted a task.")
        else:
             print("Not a valid choice.")

def main():
     while True:
         print("\n To-Do-List")
         print("1. add_task")
         print("2. view_tasks")
         print("3. task_completed")
         print("4. delete_tasks")
         print("5. Quit")
         choice = int(input("Please enter your choice:"))
         if choice == 1:
             add_tasks()
         elif choice == 2:
             view_tasks()
         elif choice == 3:
             completed_tasks()
         elif choice == 4:
             delete_tasks()
         elif choice == 5:
             print("Have a great day.")
             break
         else:
             print("Invalid choice. Please try again.")            
if __name__ == "__main__":
    main()
