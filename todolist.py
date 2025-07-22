import ast


def showTasks():
    print("Your task(s):")
    for list in toDoList:
        print(
            f"ID: {list["id"]} NAME: {list["name"]} STATUS: {list["status"]}")
    print(f"\n")


def addTask():
    taskName = input("New task name: ")
    if toDoList:
        curId = max(list["id"] for list in toDoList)
    else:
        curId = 0
    curId = curId + 1
    toDoList.append({"id": curId, "name": taskName, "status": "new"})


def deleteTask(toDoListToDel):
    idTaskToDelete = int(input("Type Task Id to delete: "))
    lenBefore = len(toDoListToDel)
    toDoListToDel = [
        task for task in toDoListToDel if task["id"] != idTaskToDelete]
    lenAfter = len(toDoListToDel)
    if lenBefore == lenAfter:
        print("Task id does not exist.")
    return toDoListToDel


def markTask(toDoListToMark):
    idTaskToMark = int(input("Type Task Id to mark as done: "))
    statusName = "done"
    done = 0
    for task in toDoListToMark:
        if task["id"] == idTaskToMark:
            task["status"] = statusName
            done = 1
            break
    if done == 0:
        print("Task id does not exist.")
    return toDoListToMark


def saveTaskListToFile(toDoList):
    with open("todofile.txt", "w", encoding="utf-8") as f:
        f.write(str(toDoList))
    print("Bye!")


def openFile():
    try:
        with open("todofile.txt", "r", encoding="utf-8") as f:
            content = f.read()
            toDoList = ast.literal_eval(content)
    except FileNotFoundError:
        with open("todofile.txt", "a") as f:
            f.write("[]")
            toDoList = []
    return toDoList


def findTasks(toDoList):
    searchSentense = input("Type key word to find in task(s): ")
    found = 0
    for list in toDoList:
        if searchSentense in str(list["name"]):
            found += 1
            print("Your searched task(s)")
            print(
                f"ID: {list["id"]} NAME: {list["name"]} STATUS: {list["status"]}")
    print(f"Found {found} task(s).")


def switch(option, toDoList):
    match option:
        case "1":
            showTasks()
        case "2":
            addTask()
        case "3":
            toDoList = markTask(toDoList)
        case "4":
            toDoList = deleteTask(toDoList)
        case "5":
            findTasks(toDoList)
        case "9":
            saveTaskListToFile(toDoList)
        case _:
            print("Invalid choice!")
    return toDoList


toDoList = openFile()
option = 0
while (option != "9"):
    print("Type 1 to View all tasks. Type 2 to Add new task. Type 3 to Mark task. Type 4 to Delete task. Type 5 to find task(s). Type 9 to quit")
    option = input("Option: ")
    switch(option, toDoList)
