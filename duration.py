from time import perf_counter_ns

class Duration():
    """
    class for measuring code execution time

    methods:
    -------
    __init__(self):
        Init instance class.
        
    start(self):
        Run timer.
        
    stop(self):
        Stop timer, return measuring result in microsecounds.
    """
    
    def __init__(self):
        """
        Init instance class.
        """
        pass

    def start(self):
        """
        Run timer.

        """
        self.__start = perf_counter_ns()
        pass

    def stop(self):
        """
        Stop timer, return measuring result in microsecounds.

        return:
        ----------
        int
            Duration code execution in microsecounds.
        """
        result = (perf_counter_ns() - self.__start) // 1000
        return result
