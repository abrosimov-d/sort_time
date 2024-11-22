from methods.bubble import Bubble
from methods.counting import Counting
from methods.heap import Heap
from methods.merge import Merge
from methods.quick import Quick
from methods.radix import Radix

from helper import Helper

class Sort():
    """
    class for sort execution

    attributes:
    ----------
    __orders : tuple
        tuple for order array methods
    __methods : list
        list of instance sort methods

    methods:
    -------
    __init__(self):
        init Sort class
        
    get_methods(self):
        return sort methods names
        
    get_orders(self):
        return order array methods
        
    check(self, data):
        validate array string
        
    generate_random_array(self, data, size):
        genarate random array string with size
        
    string_to_array(self, string):
        convert array to string
        
    array_to_string(self, array):
        convert string to array
        
    run(self, data):
        run sort only (without reverse and converting to string)
        
    finish(self, data):
        finish: revers array if need, converting to string
    """
    
    def __init__(self):
        """
        init Sort class

        methods:
        -------
        Bubble, Counting, Heap, Merge, Quick, Radix:
            methods for sort
        """
        self.__orders = ('min -> max', 'max -> min')
        self.__methods = []

        for method in [Bubble, Counting, Heap, Merge, Quick, Radix]:
            self.__methods.append(method())

    def get_methods(self):
        """
        Возвращает имена доступных методов сортировки.

        return:
        ----------
        list
            list names of sort methods
        """
        return (m.get_name() for m in self.__methods)

    def get_orders(self):
        """
        return array orders

        return:
        ----------
        tuple
            tuple array orders
        """
        return self.__orders

    def check(self, data):
        """
        validate array string

        params:
        ----------
        data : dict
            data for validate

        return:
        ----------
        dict
            validated data or error message
        """
        try:
            data['array'] = self.string_to_array(data['array'])
        except Exception as e:
            data['error'] = f'error: {e}'
        return data

    def generate_random_array(self, data, size):
        """
        genarate random array string with size

        params:
        ----------
        data : dict
            data for generated array
        size : int
            size ganerated array

        return:
        ----------
        dict
            generated array
        """
        data['array'] = self.array_to_string([Helper.random_999() for _ in range(size)])
        return data

    def string_to_array(self, string):
        """
        convert string to array

        params:
        ----------
        string : str
            string with array

        return:
        ----------
        list
            array of ints
        """
        result = []
        elements = string.split(',')
        for element in elements:
            result.append(int(element.strip()))
        return result
        
    def array_to_string(self, array):
        """
        convert array ints to string

        params:
        ----------
        array : list
            array ints.

        return:
        ----------
        str
            array string
        """
        return ','.join(str(element) for element in array)

    def run(self, data):
        """
        Выполняет сортировку массива определенным методом.

        Параметры:
        ----------
        data : dict
            Данные для сортировки.

        Возвращает:
        ----------
        dict
            Отсортированный массив.
        """
        data['array'] = self.__methods[data['method']].sort(data['array'])
        return data
    
    def finish(self, data):
        """
        Завершает сортировку, учитывая заданный порядок, и преобразует массив в строку.

        Параметры:
        ----------
        data : dict
            Данные для завершения сортировки, включая массив и порядок.

        Возвращает:
        ----------
        dict
            Отсортированный массив.
        """
        if data['order']:
            data['array'].reverse()
        data['array'] = self.array_to_string(data['array'])
        return data
