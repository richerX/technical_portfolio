# from itertools import permutations
# from itertools import combinations

def permutations(array):
    if len(array) == 0:
        return []
    elif len(array) == 1:
        return [array]
    else:
        answer = []
        for i in range(len(array)):
            element = array[i]
            remaining_array = array[:i] + array[i+1:]
            for p in permutations(remaining_array):
                answer.append([element] + p)
        return answer


for p in permutations([1, 2, 3]):
    print(p)
