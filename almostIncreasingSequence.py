#Given a sequence of integers as an array, determine whether it is possible to obtain a strictly
# increasing sequence by removing no more than one element from the array.

#Example

#For sequence = [1, 3, 2, 1], the output should be
#almostIncreasingSequence(sequence) = false;

#There is no one element in this array that can be removed in order to get a strictly increasing sequence.

#For sequence = [1, 3, 2], the output should be
#almostIncreasingSequence(sequence) = true.

#You can remove 3 from the array to get the strictly increasing sequence [1, 2].
# Alternately, you can remove 2 to get the strictly increasing sequence [1, 3].
def almostIncreasingSequence(sequence):
    inc = False
    nb = 0
    while not inc:
        if nb > 1:
            return False
        inc = True
        i = 0
        while i < len(sequence)-1:
            if sequence[i] > sequence[i+1]:
                inc = False
                try:
                    if sequence[i] < sequence[i+2]:
                        del sequence[i+1]
                        nb += 1
                        break
                except:
                    pass
                try:
                    if (i == len(sequence)-2) and sequence[i] > sequence[i+1]:
                        del sequence[i+1]
                        nb += 1
                        break
                except:
                    pass
                del sequence[i]
                nb += 1
                break
            elif sequence[i] == sequence[i+1]:
                inc = False
                del sequence[i]
                nb +=1
                break
            else:
                inc = True
            i += 1
    if nb > 1:
        return False
    return True