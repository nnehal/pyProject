class TimeCard:
    def __init__(self, name, clockIn, clockOut) -> None:
        self.name = name
        self.clockIn = clockIn
        self.clockOut = clockOut

    def hoursWorked(self):
        (hourIn, minIn) = self.clockIn.split(":")
        (hourOut, minOut) = self.clockOut.split(":")

        hourIn = int(hourIn)
        hourOut = int(hourOut)

        minIn = int(minIn)
        minOut = int(minOut)

        (totalHr, totalMin) = (hourOut-hourIn, minOut-minIn)

        if totalMin < 0:
            totalMin = 60 - abs(totalMin)
            totalHr -= 1

        return f"Total hours: {totalHr} min: {totalMin}"

def getEmployeeHours():
    name = input("Enter employee name: ")
    clockIn = input("Enter time in (24hr): ")
    clockOut = input("Enter time out (24hr): ")
    employee = TimeCard(name, clockIn, clockOut)

    return employee

def main():

    e1 = getEmployeeHours()

    print(e1.hoursWorked())

if __name__ == "__main__":
    main()

