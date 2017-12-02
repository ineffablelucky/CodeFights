# After they became famous, the CodeBots all decided to move to a new building and live together.
# The building is represented by a rectangular matrix of rooms. Each cell in the matrix contains
# an integer that represents the price of the room. Some rooms are free (their cost is 0), but that's probably
# because they are haunted, so all the bots are afraid of them.
# That is why any room that is free or is located anywhere below a free room in the same column is not
# considered suitable for the bots to live in.
# Help the bots calculate the total price of all the rooms that are suitable for them.

def matrixElementsSum(matrix):
    for i in range(len(matrix)-1):
        for j in range(len(matrix[i])):
            if matrix[i][j]==0:
                matrix[i+1][j]=0 #converting all values below 0 to 0

    totprice=0
    for i in range(len(matrix)): 
           totprice+= sum(matrix[i]) #add the sum of all rows

    return totprice
