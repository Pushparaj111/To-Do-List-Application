import os
def clear_screen():
    os.system("cls" if os.name=='nt' else 'clear')
def display_menu():
    print('To-Do List application')
    print("1.View TO-Do List")
    print("2. Add Task")
    print("3. Mark Task as complted")
    print("4.Delete Task")
    print('5. Exit')

def view_todo_list(todo_list):
    print('\n Your TO-Do List ')
    for index,task in enumerate(todo_list,start=1):
        print(f'{index}.{task}')
    print()

def add_task(todo_list):
    task=input('\n Enter the task:')
    todo_list.append(task)
    print('Task added sccessfully!')

def mark_completed(todo_list):
    view_todo_list(todo_list)
    try:
        task_index=int(input('\n Enter the index of the task to mark as completed:'))-1
        todo_list.pop(task_index)
        print('task marked as completed!')
    except IndexError:
        print('Invalid task index!')
def delete_task(todo_list):
    view_todo_list(todo_list)
    try:
        task_index=int(input('\n enter the index of the task to delete:'))-1
        todo_list.pop(task_index)
        print('task deleted successfully!')
    except IndexError:
        print('Invalid task index!')

def main():
    todo_list=[]
    while True:
        clear_screen()
        display_menu()
        choice=input('enter your choice:')
        if  choice=='1':
          view_todo_list(todo_list)
        elif choice=='2':
            add_task(todo_list)
        elif choice=='3':
           mark_completed(todo_list)
        elif choice=='4':
          delete_task(todo_list)
        elif choice=='5':
           print("Exiting...")
           break
        else:
         input('Invalid choice! Press Enter to continue...')
if  __name__=="__main__":
    main()