from sys import argv

def retrieveInput():
    if len(argv) != 2:
        return int(input("Please enter an upper bound: "))
    return int(argv[1])


upperbound = 0
while upperbound == 0:
    try:
        upperbound = retrieveInput()
        break
    except ValueError:
        print("You must enter a valid integer for your upper bound")

for i in range(1, upperbound+1):
    result = ""
    if i % 3 == 0:
        result += "Fizz"
    if i % 5 == 0:
        result += "Buzz"
    if result == "":
        result = i
    print("{0}".format(result))