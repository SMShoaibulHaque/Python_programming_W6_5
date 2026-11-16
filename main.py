
SEPARATOR = ";"


def readValues(filename):
    values = ""

    file = open(filename, "r")

    for line in file:
        values += line.strip() + SEPARATOR

    file.close()

    return values


def analyseNumbers(values):
    numbers = values.split(SEPARATOR)

    total = 0
    count = 0
    greatest = 0

    for number in numbers:
        if number != "":
            value = int(number)

            total += value
            count += 1

            if value > greatest:
                greatest = value

    average = total / count

    return count, total, greatest, average


def displayResults(filename, count, total, greatest, average):
    print("File \"" + filename + "\" results:")
    print("Count;Sum;Greatest;Average")
    print(f"{count};{total};{greatest};{average:.2f}")


def main():
    print("Program starting.")

    filename = input("Insert filename: ")

    values = readValues(filename)

    print("#### Number analysis - START ####")

    count, total, greatest, average = analyseNumbers(values)

    displayResults(filename, count, total, greatest, average)

    print()
    print("#### Number analysis - END ####")

    print("Program ending.")


main()

