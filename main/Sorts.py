# ----------------------------------------------------------------------------
# Сортировка подсчётом | Average O(n + k) | Best O(n + k) --> O(n + k) Worst |
# ----------------------------------------------------------------------------

def CountSort(mas):
    DictionaryNumbers = dict()
    for i in mas:
        try:
            DictionaryNumbers[i] += 1
        except:
            DictionaryNumbers[i] = 1
    answer = []
    keys = list(DictionaryNumbers.keys())
    keys.sort()
    for key in keys:
        answer += [key] * DictionaryNumbers[key]
    return answer

# ----------------------------------------------------------------------------
# Поразрядная сортировка | Average O(n + k) | Best O(n + k) --> O(n^2) Worst |
# ----------------------------------------------------------------------------

def BucketSort(mas):
    print("Initial array:")
    print(", ".join(map(str, mas)))    
    for i in range(m):  # Phase
        mas1 = [[] for j in range(10)]
        for j in range(n):  # bucket
            mas1[int(mas[j][m - i - 1])].append(mas[j])
        print("**********")
        print("Phase " + str(i + 1))
        mas = []
        for k in range(10):
            for r in range(len(mas1[k])):
                mas.append(mas1[k][r])
            if mas1[k] != []:
                print("Bucket " + str(k) + ": " + ", ".join(map(str, mas1[k])))
            else:
                print("Bucket " + str(k) + ": empty")
    print("**********")
    print("Sorted array:")
    print(", ".join(map(str, mas)))
        
# ----------------------------------------------------------------------------------------------
# Сортировка слиянием и слияние | Average O(n*log(n)) | Best O(n*log(n)) --> O(n*log(n)) Worst |
# ----------------------------------------------------------------------------------------------
    
def MergeSort(mas, left, right):
    if len(mas) == 0:
        return
    if right <= left:
        return
    else:
        mid = (right + left) // 2
        MergeSort(mas, left, mid)
        MergeSort(mas, mid + 1, right)
        Merge(mas, left, mid, right)

def Merge(mas, left, mid, right):
    mas1 = []
    i, j = left, mid + 1
    ind = left
    while ind < right + 1:
        if i > mid:
            mas1.append(mas[j])
            j += 1
        elif j > right:
            mas1.append(mas[i])
            i += 1
        elif mas[j] < mas[i]:
            mas1.append(mas[j])
            j += 1
        else:
            mas1.append(mas[i])
            i += 1
        ind += 1
    ind = 0
    for i in range(left, right + 1):
        mas[i] = mas1[ind]
        ind += 1
        
# ------------------------------------------------------------------------------
# Быстрая сортировка | Average O(n*log(n)) | Best O(n*log(n)) --> O(n^2) Worst |
# ------------------------------------------------------------------------------

def QuickSort(mas, l, r):
    if r > l:
        pivot = random.choice(mas[l:r + 1])
        i = l
        j = r
        while i <= j:
            while mas[i] < pivot:
                i += 1
            while mas[j] > pivot:
                j -= 1
            if i <= j:
                mas[i], mas[j] = mas[j], mas[i]
                i += 1
                j -= 1
        quicksort(mas, l, j)
        quicksort(mas, i, r)

# ------------------------------------------------------------------------------
# Сортировка выбором максимума | Average O(n^2) | Best O(n^2) --> O(n^2) Worst |
# ------------------------------------------------------------------------------

def SelectionSort(mas):
    for i in range(n):
        min1 = mas[i]
        i1 = i
        for j in range(i, n):
            if mas[j] <= min1:
                min1 = mas[j]
                i1 = j
        mas[i], mas[i1] = mas[i1], mas[i]

# --------------------------------------------------------------------
# Сортировка вставками | Average O(n^2) | Best O(n) --> O(n^2) Worst |
# --------------------------------------------------------------------

def InsertionSort(mas):
    for i in range(1, n):
        elem = mas[i]
        while i - 1 >= 0 and mas[i - 1] > elem:
            mas[i] = mas[i - 1]
            i -= 1
        mas[i] = elem
        
# --------------------------------------------------------------------
# Сортировка пузырьком | Average O(n^2) | Best O(n) --> O(n^2) Worst |
# --------------------------------------------------------------------

def BubbleSort(mas):
    for i in range(n - 1, 0, -1):
        sens = 0
        for j in range(i):
            if mas[j] > mas[j + 1]:
                mas[j], mas[j + 1] = mas[j + 1], mas[j]
                sens = 1
        if sens == 0:
            break

# ----------------------------------------------------------------------------------------------------
# Пирамидальная сортировка (Heapsort) | Average O(n*log(n)) | Best O(n*log(n)) --> O(n*log(n)) Worst |
# ----------------------------------------------------------------------------------------------------

class heap:
    def __init__(self):
        self.data = mas_input
        self.length = n

    def sift_up(self, i):
        while i > 0:
            if self.data[i] > self.data[(i - 1) // 2]:
                self.data[i], self.data[(i - 1) // 2] = self.data[(i - 1) // 2], self.data[i]
            else:
                break
            i = (i - 1) // 2
        return i + 1
    
    def sift_down(self, i):
        while i * 2 + 1 < self.length:            
            if i * 2 + 2 > self.length - 1 or self.data[i * 2 + 1] >= self.data[i * 2 + 2]:
                j = i * 2 + 1
            else:
                j = i * 2 + 2                  
            if self.data[i] < self.data[j]:
                self.data[i], self.data[j] = self.data[j], self.data[i]
            else:
                break            
            i = j
        return i + 1
    
    def heapify(self):
        for i in range(self.length - 1, -1, -1):
            self.sift_down(i)
        
    def change(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        self.data.pop()
        self.length -= 1
        
    def get(self):
        return self.data
        
        
n = int(input())
mas_input = list(map(int, input().split()))
heap = heap()
str_answer = ""
mas_answer = []
for i in range(n):
    heap.heapify()
    str_answer += (" ".join(map(str, heap.get()))) + "\n"
    mas_answer.append(heap.get()[0])
    heap.change()
mas_answer.reverse()
str_answer += (" ".join(map(str, mas_answer))) + "\n"
with open("output.txt", "w") as fout:
    fout.write(str_answer)
