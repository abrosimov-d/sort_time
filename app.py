from sortdialog import SortDialog
from sort import Sort
from duration import Duration

class App():
    def __init__(self):
        self.sort = Sort()
        self.sort_dialog = SortDialog(self.on_sort_listener, self.sort.get_methods(), self.sort.get_orders())

    def run(self):
        self.sort_dialog.run()

    def on_sort_listener(self, data):
        try:
            if 'array' not in data:
                data = self.sort.generate_random_array(data, 1000)
            elif 'method' in data:
                data = self.sort.check(data)
                duration = Duration()
                duration.start()
                data = self.sort.run(data)
                data['duration'] = duration.stop()
                data = self.sort.finish(data)
            else:
                data = self.sort.check(data)
        except Exception as err:
            data['error'] = f'{err}'
        return data