class Bubble():
    def __init__(self):
        self.__name = 'bubble'
        pass

    def get_name(self):
        return self.__name

    def sort(self, arr):
        return self.bubble_sort(arr)

    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr
