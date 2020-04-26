def lower_bound(mas, element):
    left, right = 0, len(mas)
    while right - left > 0:
        middle = (right + left) // 2
        if mas[middle] < element:
            left = middle + 1
        else:
            right = middle
    return left


def upper_bound(mas, element):
    left, right = 0, len(mas)
    while right - left > 0:
        middle = (right + left) // 2
        if mas[middle] <= element:
            left = middle + 1
        else:
            left = middle
    return left


def lower_bound_reverse(mas, element):
    left, right = -1, len(mas) - 1
    while right - left > 0:
        middle = (right + left + 1) // 2
        if mas[middle] > element:
            right = middle - 1
        else:
            left = middle
    return left


def upper_bound_reverse(mas, element):
    left, right = -1, len(mas) - 1
    while right - left > 0:
        middle = (right + left + 1) // 2
        if mas[middle] >= element:
            right = middle - 1
        else:
            left = middle
    return left


mas = [1, 2, 3, 3, 3, 5]
print("Binary search")
print("Indexes:  0, 1, 2, 3, 4, 5")
print("List -->", mas)
print()
print("Searching for element = 5")
print("Lower bound -->", lower_bound(mas, 5))
print("Upper bound -->", upper_bound(mas, 5))
print("Lower bound reverse -->", lower_bound_reverse(mas, 5))
print("Upper bound reverse -->", upper_bound_reverse(mas, 5))


# --------------------------------------------
print()
print("-" * 50)
print()
# --------------------------------------------


def getMaxSubSum(mas):
    MaxSum = 0
    PartialSum = 0
    l = 0
    for i in range(len(mas)):
        PartialSum += mas[i]
        if PartialSum > MaxSum:
            MaxSum = PartialSum
            Indexes = [l, i + 1]
        if PartialSum < 0:
            PartialSum = 0
            l = i + 1
    return MaxSum, Indexes


mas = [1, 2, -3, 10, 3, 5]
answer, indexes = getMaxSubSum(mas)
l, r = indexes[0], indexes[1]
print("Maximum subsequence sum")
print("List -->", mas)
print("Answer =", answer, "|", "Part:", mas[l:r], "|", "Indexes:", l, "-->", r - 1, "(Included)")