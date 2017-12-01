
# Given an array of strings, return another array containing all of its longest strings.

# Example

# For inputArray = ["aba", "aa", "ad", "vcd", "aba"], the output should be
# allLongestStrings(inputArray) = ["aba", "vcd", "aba"].

def allLongestStrings(inputArray):
    result = []
    maxlength = len(max(inputArray, key=len))

    for i in inputArray:
        if len(i) == maxlength:
            result.append(i)

    return result