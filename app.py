from sortdialog import SortDialog
from sort import Sort
from duration import Duration

class App():
    """
    Application class

    attributes:
    ----------
    sort : Sort
        instance Sort class
    sort_dialog : SortDialog
        instance SortDialog class

    methods:
    -------
    __init__(self):
        init class App, init instance Sort, SortDialog
        
    run(self):
        Run SortDialog
        
    on_sort_listener(self, data):
        process messages for SortDialog
    """
    
    def __init__(self):
        """
        init class App, init instance Sort, SortDialog

        methods:
        -------
        on_sort_listener(data):
            process messages for SortDialog
        """
        self.sort = Sort()
        self.sort_dialog = SortDialog(self.on_sort_listener, self.sort.get_methods(), self.sort.get_orders())

    def run(self):
        """
        run SortDialog
        """
        self.sort_dialog.run()

    def on_sort_listener(self, data):
        """
        process messages for SortDialog

        params:
        ----------
        data : dict
            data for sort

        return:
        ----------
        dict
            sorted data, error message
        """
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
