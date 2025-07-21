toDoList = [
    # {"id": 1, "name": "Kup bułki", "status": "pending"},
    # {"id": 2, "name": "Zamów karty", "status": "done"},
    # {"id": 3, "name": "Zmień żarówkę", "status": "pending"}
]


def showTasks():
    print("Your task(s):")
    print(toDoList)
    for list in toDoList:
        print(
            f"ID: {list["id"]} NAME: {list["name"]} STATUS: {list["status"]}")
    print(f"\n")


def addTask():
    taskName = input("Task name: ")
    if toDoList:
        curId = max(list["id"] for list in toDoList)
    else:
        curId = 0
    curId = curId + 1
    toDoList.append({"id": curId, "name": taskName, "status": "new"})


def deleteTask(toDoListToDel):
    idTaskToDelete = int(input("Type id task to delete: "))
    lenBefore = len(toDoListToDel)
    toDoListToDel = [
        task for task in toDoListToDel if task["id"] != idTaskToDelete]
    lenAfter = len(toDoListToDel)
    if lenBefore == lenAfter:
        print("Task id does not exist.")
    return toDoListToDel


def markTask(toDoListToMark):
    idTaskToMark = int(input("Type id task to mark as done: "))
    statusName = input("Type status name: ")
    done = 0
    for task in toDoListToMark:
        if task["id"] == idTaskToMark:
            task["status"] = statusName
            done = 1
            break
    if done == 0:
        print("Task id does not exist.")
    return toDoListToMark


def switch(option):
    global toDoList
    match option:
        case "1":
            showTasks()
        case "2":
            addTask()
        case "3":
            toDoList = markTask(toDoList)
        case "4":
            toDoList = deleteTask(toDoList)
        case "9":
            print("Bye!")
        case _:
            print("Invalid choice!")


option = 0
while (option != "9"):
    print("Type 1 to View all tasks. Type 2 to Add new task. Type 3 to Mark task. Type 4 to Delete task. Type 9 to quit")
    option = input("Option: ")
    switch(option)
