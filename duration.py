from time import perf_counter_ns

class Duration():
    def __init__(self):
        pass

    def start(self):
        self.__start = perf_counter_ns()
        pass

    def stop(self):
        result = (perf_counter_ns() - self.__start) // 1000
        return result