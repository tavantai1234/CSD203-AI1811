class Employee:
    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level

    def __repr__(self):
        return f"{self.id} {self.name} {self.level}"


def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l].id > arr[largest].id:
        largest = l

    if r < n and arr[r].id > arr[largest].id:
        largest = r

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)


def partition(arr, low, high):
    pivot = arr[high].id
    i = low - 1

    for j in range(low, high):
        if arr[j].id < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m

    L = [arr[l + i] for i in range(n1)]
    R = [arr[m + 1 + i] for i in range(n2)]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i].id <= R[j].id:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)
        merge_sort(arr, m + 1, r)
        merge(arr, l, m, r)


employees = [
    Employee("A05", "Tran Quang", 7),
    Employee("A03", "Nguyen An", 7),
    Employee("A01", "Truong Phung", 5),
    Employee("A04", "Pham Thi Lam", 2),
    Employee("A02", "Do Truong Ton", 5),
]

heap_sort(employees)
print("Ascending order by ID (Heap Sort):", employees)

quick_sort(employees, 0, len(employees) - 1)
employees.reverse()
print("Descending order by ID (Quick Sort):", employees)

merge_sort(employees, 0, len(employees) - 1)
print("Ascending order by ID (Merge Sort):", employees)
