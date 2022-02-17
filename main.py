import random
import math
def randodo():
    A=int(input("Введите колличество строк:"))
    B=int(input("Введите колличество столбцов:"))
    min=int(input("Введите нижнюю границу рандома:"))
    max=int(input("Введите верхнюю границу:"))
    return A,B,min,max
def gen(A,B,min,max):
    mas = [[random.randint(min, max)  for j in range(B)]for i in range(A)]
    return mas


def sortobm(mas,A,B):
    array=Unification(mas)
    print(array)
    swapped = False
    for i in range(len(array) - 1, 0, -1):
        for j in range(i):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swapped = True
        if swapped:
            swapped = False
        else:
            break
    return Divider(array, A, B)

def sortvib(mas,A,B):
    mas = Unification(mas)
    for i in range(len(mas) - 1):
        min_idx = i
        for idx in range(i + 1, len(mas) - 1):
            if mas[idx] < mas[min_idx]:
                min_idx = idx
        mas[i], mas[min_idx] = mas[min_idx], mas[i]
    return Divider(mas, A, B)
    print(*mas, sep="\n")
def sortvstav(mas,A,B):
    mas = Unification(mas)
    for i in range(1, len(mas)):
        key = mas[i]
        j = i - 1
        while mas[j] > key and j >= 0:
            mas[j + 1] = mas[j]
            j -= 1
        mas[j + 1] = key
    return Divider(mas, A, B)

def sorthel(mas,A,B):
    mas = Unification(mas)
    n = len(mas)
    k = int(math.log2(n))
    interval = 2 ** k - 1
    while interval > 0:
        for i in range(interval, n):
            temp = mas[i]
            j = i
            while j >= interval and mas[j - interval] > temp:
                mas[j] = mas[j - interval]
                j -= interval
            mas[j] = temp
        k -= 1
        interval = 2 ** k - 1
    return Divider(mas, A, B)
def heapify(array, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and array[i] < array[l]:
        largest = l
    if r < n and array[largest] < array[r]:
        largest = r

    if largest != i:
        array[i], array[largest] = array[largest], array[i]
        heapify(array, n, largest)


def sortpiro(mas,A,B):
    array=Unification(mas)
    n = len(array)
    for i in range(n // 2, -1, -1):
        heapify(array, n, i)
    for i in range(n - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heapify(array, i, 0)
    return Divider(array,A,B)

def sortfast(mas,A,B):
    print("Quick sort:")
    nums = Unification(mas)
    nums = for_quick_sort(nums)
    return Divider(nums,A,B)


def for_quick_sort(nums):
        less = []
        equal = []
        greater = []
        if len(nums) > 1:
            pivot = nums[0]
            for x in nums:
                if x < pivot:
                    less.append(x)
                elif x == pivot:
                    equal.append(x)
                elif x > pivot:
                    greater.append(x)
            return for_quick_sort(less) + equal + for_quick_sort(greater)
        else:
            return nums
def sorttur(mas,A,B):
    arr = mas.copy()
    for i in range(len(arr)):
        tournamentSort(arr[i])
    return arr
def tournamentSort(arr):
    tree = [None] * 2 * (len(arr) + len(arr) % 2)
    index = len(tree) - len(arr) - len(arr) % 2

    for i, v in enumerate(arr):
        tree[index + i] = (i, v)

    for j in range(len(arr)):
        n = len(arr)
        index = len(tree) - len(arr) - len(arr) % 2
        while index > -1:
            n = (n + 1) // 2
            for i in range(n):
                i = max(index + i * 2, 1)
                if tree[i] != None and tree[i + 1] != None:
                    if tree[i][1] < tree[i + 1][1]:
                        tree[i // 2] = tree[i]
                    else:
                        tree[i // 2] = tree[i + 1]
                else:
                    tree[i // 2] = tree[i] if tree[i] != None else tree[i + 1]
            index -= n

        index, x = tree[0]
        arr[j] = x
        tree[len(tree) - len(arr) - len(arr) % 2 + index] = None
def Unification(matrix):
    massive=[]

    for i in matrix:
        for j in i:
            massive.append(j)

    return massive
def Divider(massive,M,N):
    matrix=[]
    k=0

    for i in range(M):
        matrix.append([0] * N)
        for j in range(N):
            matrix[i][j] = massive[k]
            k+=1
    return matrix

A=int(input("Введите колличество строк:"))
B=int(input("Введите колличество столбцов:"))
min=int(input("Введите нижнюю границу рандома:"))
max=int(input("Введите верхнюю границу:"))
mas=gen(A,B,min,max)
mas = sortobm(mas,A,B)
print(*mas,sep="\n")
print()
mas=gen(A,B,min,max)
mas = sortvib(mas,A,B)
print(*mas,sep="\n")
print()
mas=gen(A,B,min,max)
mas = sortvstav(mas,A,B)
print(*mas,sep="\n")
print()
mas=gen(A,B,min,max)
mas = sorthel(mas,A,B)
print(*mas,sep="\n")
print()
mas=gen(A,B,min,max)
mas = sortpiro(mas,A,B)
print(*mas,sep="\n")
print()
mas=gen(A,B,min,max)
mas = sortfast(mas,A,B)
print(*mas,sep="\n")
print()
#mas=gen(A,B,min,max)
#mas = sorttur(mas,A,B)
#Sprint(*mas,sep="\n")