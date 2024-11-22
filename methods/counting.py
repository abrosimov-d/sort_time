class Counting():
    def __init__(self):
        self.__name = 'counting'
        pass

    def get_name(self):
        return self.__name

    def sort(self, arr):
        return counting_sort(arr)

def counting_sort(arr):
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (arr[i]) % 10
        count[index] += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    i = n - 1
    while i >= 0:
        index = (arr[i]) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1
        i -= 1

    for i in range(n):
        arr[i] = output[i]
    
    return arr
