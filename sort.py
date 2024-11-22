from methods.bubble import Bubble
from methods.counting import Counting
from methods.heap import Heap
from methods.merge import Merge
from methods.quick import Quick
from methods.radix import Radix

from helper import Helper

class Sort():
    """
    Класс для выполнения различных методов сортировки.

    Атрибуты:
    ----------
    __orders : tuple
        Кортеж, содержащий возможные порядки сортировки ('min -> max', 'max -> min').
    __methods : list
        Список экземпляров классов сортировки.

    Методы:
    -------
    __init__(self):
        Инициализация класса Sort с созданием списка методов сортировки.
        
    get_methods(self):
        Возвращает имена доступных методов сортировки.
        
    get_orders(self):
        Возвращает возможные порядки сортировки.
        
    check(self, data):
        Проверяет и преобразует строку массива в список чисел.
        
    generate_random_array(self, data, size):
        Генерирует случайный массив заданного размера и сохраняет его в строку.
        
    string_to_array(self, string):
        Преобразует строку массива в список чисел.
        
    array_to_string(self, array):
        Преобразует список чисел в строку.
        
    run(self, data):
        Выполняет сортировку массива выбранным методом.
        
    finish(self, data):
        Завершает сортировку, задает порядок и преобразует массив в строку.
    """
    
    def __init__(self):
        """
        Инициализирует класс Sort.

        Методы:
        -------
        Bubble, Counting, Heap, Merge, Quick, Radix:
            Классы методов сортировки, которые будут использоваться.
        """
        self.__orders = ('min -> max', 'max -> min')
        self.__methods = []

        for method in [Bubble, Counting, Heap, Merge, Quick, Radix]:
            self.__methods.append(method())

    def get_methods(self):
        """
        Возвращает имена доступных методов сортировки.

        Возвращает:
        ----------
        generator
            Генератор, возвращающий имена методов сортировки.
        """
        return (m.get_name() for m in self.__methods)

    def get_orders(self):
        """
        Возвращает возможные порядки сортировки.

        Возвращает:
        ----------
        tuple
            Кортеж с порядками сортировки ('min -> max', 'max -> min').
        """
        return self.__orders

    def check(self, data):
        """
        Проверяет и преобразует строку массива в список чисел.

        Параметры:
        ----------
        data : dict
            Данные для проверки, содержащие строку массива.

        Возвращает:
        ----------
        dict
            Обработанные данные с преобразованным массивом или сообщением об ошибке.
        """
        try:
            data['array'] = self.string_to_array(data['array'])
        except Exception as e:
            data['error'] = f'error: {e}'
        return data

    def generate_random_array(self, data, size):
        """
        Генерирует случайный массив заданного размера и сохраняет его в строку.

        Параметры:
        ----------
        data : dict
            Данные для обновления с новым массивом.
        size : int
            Размер генерируемого массива.

        Возвращает:
        ----------
        dict
            Обновленные данные с новым случайным массивом.
        """
        data['array'] = self.array_to_string([Helper.random_999() for _ in range(size)])
        return data

    def string_to_array(self, string):
        """
        Преобразует строку массива в список чисел.

        Параметры:
        ----------
        string : str
            Строка, представляющая массив.

        Возвращает:
        ----------
        list
            Список чисел, полученных из строки.
        """
        result = []
        elements = string.split(',')
        for element in elements:
            result.append(int(element.strip()))
        return result
        
    def array_to_string(self, array):
        """
        Преобразует список чисел в строку.

        Параметры:
        ----------
        array : list
            Список чисел.

        Возвращает:
        ----------
        str
            Строка, представляющая массив чисел.
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
