from dialog import Dialog
from helper import Helper

ID_INPUT_UNSORTED = Helper.random_id()
ID_BUTTON_FILL_RANDOMS = Helper.random_id()
ID_INPUT_SORTED = Helper.random_id()
ID_LABEL_ERROR = Helper.random_id()
ID_BUTTON_START = Helper.random_id()

class SortDialog(Dialog):
    def __init__(self, on_sort_listener):
        super().__init__()
        template = f'''
        size, XXL, 0, 0
        header, 🚀SORT&TIME, 1
        label, unsorted array:, 2
        input, not_sorted, {ID_INPUT_UNSORTED}
        slabel, , {ID_LABEL_ERROR}
        button, fill randoms, {ID_BUTTON_FILL_RANDOMS}
        separator, 0, 0
        combo, 1, 5, sort: min -> max, sort: max -> min
        button, start, {ID_BUTTON_START}
        separator, 0, 0
        label, sorted array:, 7
        input, sorted, {ID_INPUT_SORTED}
        xlabel, 00:00:00.0, 9
        '''
        super().template(template)
        super().set_event_listner(self.__event_listener)
        self.on_sort_listener = on_sort_listener 

    def run(self):
        super().run()
    
    def __event_listener(self, event, id, data):
        if event == 'key' and data.key == '\r' or event =='click' and id==ID_BUTTON_START:
            data = {}
            result = self.on_sort_listener(data)
            if 'error' in result:
                self.set_text_by_id(ID_LABEL_ERROR, result['error'])