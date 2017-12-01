# Ticket numbers usually consist of an even number of digits. A ticket number is considered lucky
# if the sum of the first half of the digits is equal to the sum of the second half.

# Given a ticket number n, determine if it's lucky or not.

# Example

# For n = 1230, the output should be
# isLucky(n) = true;
# For n = 239017, the output should be
# isLucky(n) = false.


def isLucky(n):
    l = []
    while n > 0:
        l.append(n % 10)
        n = n // 10
    length=len(l)
    return sum([l[x] for x in range(0, length//2)]) == sum([l[y] for y in range((length//2), length)])