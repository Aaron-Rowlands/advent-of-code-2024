import sys

def main():
    leftList = []
    rightList = []
    with open(sys.argv[1]) as inputfile:
        for line in inputfile:
           leftNumberStr, rightNumberStr = line.strip().split("   ")
           leftList.append(int(leftNumberStr))
           rightList.append(int(rightNumberStr))

    leftList.sort()
    rightList.sort()

    differenceSum = 0
    for (leftNumber, rightNumber) in zip(leftList, rightList):
        differenceSum += abs(leftNumber - rightNumber)

    similarityScore = getSimilarityScore(leftList, rightList)

    print(f"Sum of differences: {differenceSum}")
    print(f"Similarity score:   {similarityScore}")

def getSimilarityScore(a, b):
    score = 0
    for element in a:
        occurrencesInB = b.count(element)
        score += element * occurrencesInB

    return score

main()
