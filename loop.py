from read import readDataFromConsole


def main():
    endNumber = readDataFromConsole()
    sumInt = 0
    if endNumber is None:
        return
    if endNumber < 0:
        print("Max number must be greater than 0")
        return
    for index in range(endNumber):
        sumInt += index  # It's the same with sum = sum + index
    print("Sum: %d\n" % sumInt)
    number = 0
    while number < 5:
        number += 1
        if number == 3:
            continue
        print("index: " + str(number))
    print("Count: %d\n" % number)


if __name__ == '__main__':
    main()
