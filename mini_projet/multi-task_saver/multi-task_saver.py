
if __name__ == '__main__':

    task = input("Enter a task: ")
    file_location = ".\mini_projet\multi-task_saver\\tasks.txt"
    file = open(file_location, "a")
    file.write(f"{task}\n")
    print("Task saved!")
    file.close()
    file = open(file_location, "r")

    print("All saved tasks: \n")
    j = 0
    for i in file:
        line = file.readline()
        print(f"{j+1}. {line.strip()}")
        j += 1
    file.close()
    
    

