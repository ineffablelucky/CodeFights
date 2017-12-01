# Given two strings, find the number of common characters between them.

# Example

# For s1 = "aabcc" and s2 = "adcaa", the output should be
# commonCharacterCount(s1, s2) = 3.

# Strings have 3 common characters - 2 "a"s and 1 "c".

def commonCharacterCount(s1, s2):
    from collections import Counter
    s1list=[l for l in s1]
    s2list=[l for l in s2]
    s1dict=Counter(s1list)
    s2dict=Counter(s2list)
    count=0
    for i in s1dict.keys():
        for j in s2dict.keys():
            if i==j:
                count+=min(s1dict[i],s2dict[j])

    return count
