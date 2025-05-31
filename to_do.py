# simple to do list

print('------------------------------\nWelcome to the to do list!\n------------------------------')

while True:
    print('\nMenu\n------------------------------\n1.View tasks \n2.Add task \n3.Remove Task \n4.Exit\n------------------------------')
    choice = int(input('Enter your choice: '))
    if choice == 1:
        print('\nTasks to Complete:\n------------------------------')
        file = open('to_do_list.txt', 'r')
        read = file.readlines()
        tasks = [line.strip() for line in read]
        print(tasks)
        file.close()

    elif choice == 2:
        new_task = input('New task: ')
        new_input = new_task.lower()
        file = open('to_do_list.txt', 'a')
        file.write('\n' + new_input)
        file.close()

    elif choice == 3:
        with open('to_do_list.txt', 'r') as file:
            tasks = [line.strip() for line in file.readlines()]

        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')

        task_num = int(input('Choose task number to remove: '))

        removed_task = tasks.pop(task_num - 1)
        with open('to_do_list.txt', 'w') as file:
            for task in tasks:
                file.write(task + '\n')
        print(f'Task "{removed_task}" removed.')

    elif choice == 4:
        print('Goodbye!')
        break

    else:
        print('\nINVALID INPUT, ENTER AN INTEGER FROM 1 TO 4')
