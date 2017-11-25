# Your task today is simple: given an array of strings words and a string text, return, for each word w in words, how many occurrences of w are in text.

# Example

# For text = "aaaa" and words = ["a", "aa", "aaa", "aaaa"],
# the output should be
# countingOccurrences(text, words) = [4, 3, 2, 1].
# There are 4 occurrences of "a" in "aaaa", 3 occurrences of "aa" in "aaaa", 2 occurrences of "aaa" in "aaaa" and 1 occurrence of "aaaa" in "aaaa".


def countingOccurrences(text, words):
    length = len(text)
    alist = []
    result = []
    for i in range(length):
        for j in range(i, length):
            alist.append(text[i:j + 1]) # alist will have all substrings of text

    for w in words:
        count = 0
        for items in alist:  # to match words in alist
            if w == items:
                count += 1

        result.append(count)

    return result

text = ""       # enter the text here
words= ["","",""]   # Enter the words you want to search in text

print(countingOccurrences(text,words))