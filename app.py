from sortdialog import SortDialog
from sort import Sort

class App():
    def __init__(self):
        self.sort = Sort()
        self.sort_dialog = SortDialog(self.on_sort_listener, self.sort.get_methods(), self.sort.get_orders())

    def run(self):
        self.sort_dialog.run()
        pass

    def on_sort_listener(self, data):
        print(data)

        if 'array' not in data:
            data = self.sort.generate_random_array(data, 10)
            return data

        if 'method' in data:
            data = self.sort.check(data)
            data = self.sort.run(data)
        else:
            data = self.sort.check(data)
            print(data)
        return data