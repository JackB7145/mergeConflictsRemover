def removeAllConflicts(inputPath, outputPath):
    logFile = open('./logs/log.txt', 'w')
    with open(inputPath, 'r') as file:
        data = file.read().split("\n")

    name = input("Enter the name of your branch: ")
    upstream = input("Enter the name of the upstream branch: ")

    newContent = []
    stack = []

    for index, line in enumerate(data):

        if line == f"<<<<<<< {name}":
            logFile.write(f"{name} changes passed at line {index}\n")

        elif line == "=======":
            logFile.write(f"{upstream} Changes started at line {index}\n")
            stack.append(line)

        elif line == f">>>>>>> {upstream}":
            logFile.write(f"{upstream} Changes ended at line {index}\n")
            stack.pop()

        elif not stack:
            newContent.append(line)
        
    with open(outputPath, "w") as outFile:
        outFile.write('\n'.join(newContent))


if __name__ == "__main__":
    removeAllConflicts("./bin/input.txt", "./bin/input.txt")
