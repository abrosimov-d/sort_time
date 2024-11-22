import unittest
from sort import Sort

class TestSort(unittest.TestCase):
    
    def setUp(self):
        self.sort = Sort()
        self.unsorted_array = [6, 3, 9, -1, 4, 7, 0, 1, 4, 6, 7]
        self.sorted_array = [-1, 0, 1, 3, 4, 4, 6, 6, 7, 7, 9]
        self.sorted_array_reversed = [9, 7, 7, 6, 6, 4, 4, 3, 1, 0]

    def test_bubble(self):
        data = {}
        data['method'] = 0
        data['order'] = 0
        data['array'] = self.unsorted_array
        result = self.sort.run(data)
        self.assertEqual(result['array'], self.sorted_array)

    def test_counting(self):
        data = {}
        data['method'] = 1
        data['order'] = 0
        data['array'] = self.unsorted_array
        result = self.sort.run(data)
        self.assertEqual(result['array'], self.sorted_array)

    def test_heap(self):
        data = {}
        data['method'] = 2
        data['order'] = 0
        data['array'] = self.unsorted_array
        result = self.sort.run(data)
        self.assertEqual(result['array'], self.sorted_array)

    def test_merge(self):
        data = {}
        data['method'] = 3
        data['order'] = 0
        data['array'] = self.unsorted_array
        result = self.sort.run(data)
        self.assertEqual(result['array'], self.sorted_array)

    def test_quick(self):
        data = {}
        data['method'] = 4
        data['order'] = 0
        data['array'] = self.unsorted_array
        result = self.sort.run(data)
        self.assertEqual(result['array'], self.sorted_array)

    def test_radix(self):
        data = {}
        data['method'] = 5
        data['order'] = 0
        data['array'] = self.unsorted_array
        result = self.sort.run(data)
        #self.assertEqual(result['array'], self.sorted_array)


if __name__ == '__main__':
    unittest.main()
