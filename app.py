from sortdialog import SortDialog

class App():
    def __init__(self):
        self.sort_dialog = SortDialog(self.on_sort_listener)
        pass

    def run(self):
        self.sort_dialog.run()
        pass

    def on_sort_listener(self, data):
        data['error'] = 'error message'
        return data