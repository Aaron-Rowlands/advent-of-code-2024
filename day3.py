import re
import sys

def main():
    enableString  = "do()"
    disableString = "don't()"
    mulPattern = r"mul\([0-9]{1,3},[0-9]{1,3}\)"

    with open(sys.argv[1]) as inputfile:
        inputString = inputfile.read()

    multiplicationSum = evaluateString(inputString, mulPattern, (enableString, disableString))

    # TODO: Restore part 1 solution calculation
    print(f"Sum of all multiplication instructions: {multiplicationSum}")

def evaluateString(input, mulPattern, enableAndDisableStr):
    enableStr, disableStr = enableAndDisableStr

    patternList = [mulPattern, re.escape(enableStr), re.escape(disableStr)]
    combinedPattern = "|".join(patternList)

    expressionList = re.findall(combinedPattern, input)

    multiplicationSum = 0
    currentlyEnabled = True
    for expression in expressionList:
        if expression == enableStr:
            currentlyEnabled = True
        elif expression == disableStr:
            currentlyEnabled = False
        else: # multiplication expression
            if currentlyEnabled:
                multiplicationSum += evaluateMulExpression(expression)

    return multiplicationSum

def evaluateMulExpression(expression):
    numberStrings = re.findall(r"[0-9]+", expression)
    a = int(numberStrings[0])
    b = int(numberStrings[1])

    return a * b

main()
