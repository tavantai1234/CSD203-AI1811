class Employee:
    def __init__(self, id, name, level):
        self.id = id
        self.name = name
        self.level = level

    def __repr__(self):
        return f"{self.id} {self.name} {self.level}"


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j].id > key.id:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j].id < arr[min_idx].id:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j].id > arr[j + 1].id:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


employees = [
    Employee("A05", "Tran Quang", 7),
    Employee("A03", "Nguyen An", 7),
    Employee("A01", "Truong Phung", 5),
    Employee("A04", "Pham Thi Lam", 2),
    Employee("A02", "Do Truong Ton", 5),
]

insertion_sort(employees)
print("Ascending order by ID (Insertion Sort):", employees)

selection_sort(employees)
employees.reverse()
print("Descending order by ID (Selection Sort):", employees)

bubble_sort(employees)
print("Ascending order by ID (Bubble Sort):", employees)
