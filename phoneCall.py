#Some phone usage rate may be described as follows:

#first minute of a call costs min1 cents,
#each minute from the 2nd up to 10th (inclusive) costs min2_10 cents
#each minute after 10th costs min11 cents.
#You have s cents on your account before the call. What is the duration of the
# longest call (in minutes rounded down to the nearest integer) you can have?
def phoneCall(min1, min2_10, min11, s):
    count = 0
    if min1 > s:
        return 0

    else:
        count += 1
        s -= min1
        if min2_10 * 9 >= s:
            a = s // min2_10
            a += 0.5
            b = s / min2_10
            if a == b:
                count = count + (s // min2_10)
                return count
            else:
                count = count + round(s / min2_10, 0)
                return count
        else:
            count += 9
            s -= min2_10 * 9
            y = s // min11
            y += 0.5
            x = s / min11

            if x == y:
                count = count + (s // min11)
                return count
            else:
                count = count + round(s / min11, 0)
                return count