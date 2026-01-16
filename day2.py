import sys

def main():
    reportList = []
    with open(sys.argv[1]) as inputfile:
        for line in inputfile:
            numberStrings = line.strip().split(" ")

            report = []
            for numberStr in numberStrings:
                report.append(int(numberStr))

            reportList.append(report)

    safeCounter = 0
    for report in reportList:
        if isSafe(report):
            safeCounter += 1

    print(f"Number of safe reports: {safeCounter}")

def isSafe(report):
    differences = getDifferences(report)

    return (differencesHaveTheRightSize(differences) and differencesHaveTheSameSign(differences))

def getDifferences(report):
    differences = []
    for i in range(len(report) - 1):
        differences.append(report[i] - report[i + 1])

    return differences

def differencesHaveTheRightSize(differences):
    for diff in differences:
        if (abs(diff) > 3) or (abs(diff) < 1):
            return False
    
    return True

def differencesHaveTheSameSign(differences):
    signs = [ -1 if diff < 0 else 1 for diff in differences ]
    return (abs(sum(signs)) == len(differences))

if __name__ == "__main__":
    main()
