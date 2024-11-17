from methods.bubble import Bubble
from helper import Helper

class Sort():
    def __init__(self):
        self.__orders = ('min -> max', 'max -> min')
        self.__methods = []

        for method in [Bubble, Bubble]:
            self.__methods.append(method())

    def get_methods(self):
        return (m.get_name() for m in self.__methods)

    def get_orders(self):
        return self.__orders

    def check(self, data):
        array = []
        try:
            elements = data['array'].split(',')
            for element in elements:
                array.append(int(element.strip()))
            data['array'] = array
        except Exception as e:
            data['error'] = f'error: {e}'
        return data

    def generate_random_array(self, data, size):
        data['array'] = self.array_to_string([Helper.random_999() for _ in range(size)])
        return data

    def string_to_array(self, string):
        pass

    def array_to_string(self, array):
        return ','.join(str(element) for element in array)

    def run(self, data):
        data['array'] = self.__methods[data['method']].sort(data['array'])
        if (data['order']):
            data['array'].reverse()
        data['array'] = self.array_to_string(data['array'])
        return data