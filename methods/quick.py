class Quick():
    def __init__(self):
        self.__name = 'quick'
        pass

    def get_name(self):
        return self.__name

    def sort(self, arr):
        return quick_sort(arr)

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quick_sort(left) + middle + quick_sort(right)
