def findSumMultiple(multipleNumber, limitNumber):
    limitNumber = (limitNumber - (limitNumber % multipleNumber)) / multipleNumber
    return int(multipleNumber * limitNumber * (limitNumber + 1) / 2)


def findSumMultiples(limitNumber):
    return  findSumMultiple(3, limitNumber - 1) + \
            findSumMultiple(5, limitNumber - 1) - \
            findSumMultiple(15, limitNumber - 1)


print('The sum of the multiples of 3 and 5 below 10 is:', findSumMultiples(10))
print('The sum of the multiples of 3 and 5 below 1000 is:', findSumMultiples(1000))
