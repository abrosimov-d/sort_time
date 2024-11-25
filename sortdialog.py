from dialog import Dialog
from helper import Helper

ID_INPUT_UNSORTED = Helper.random_id()
ID_BUTTON_FILL_RANDOMS = Helper.random_id()
ID_INPUT_SORTED = Helper.random_id()
ID_LABEL_INPUTERROR = Helper.random_id()
ID_LABEL_SORTERROR = Helper.random_id()
ID_BUTTON_START = Helper.random_id()
ID_COMBO_METHOD = Helper.random_id()
ID_COMBO_ORDER = Helper.random_id()
ID_LABEL_DURATION = Helper.random_id()

class SortDialog(Dialog):
    """
    Class for create tkinter dialog 

    attributes:
    ----------
    on_sort_listener : function
        Sort listener
    methods : list
        Methods list
    orders : list
        Order array lists

    methods:
    -------
    __init__(self, on_sort_listener, methods, orders):
        init SortDialog
        
    run(self):
        run SortDialog
        
    __event_listener(self, event, id, event_data):
        process dialog events (click, key)
    """
    
    def __init__(self, on_sort_listener, methods, orders):
        """
        init SortDialog

        params:
        ----------
        on_sort_listener : function
            Sort Listener
        methods : list
            Methods list
        orders : list
            Order array lists
        """
        super().__init__()
        self.on_sort_listener = on_sort_listener 
        template = f'''
        size, XXL, 0, 0
        header, 🚀SORT_TIME, 1
        tab, ST, 0, 0
        label, unsorted array:, 2
        input, not_sorted, {ID_INPUT_UNSORTED}
        slabel, , {ID_LABEL_INPUTERROR}
        button, fill with 1000 randoms, {ID_BUTTON_FILL_RANDOMS}
        separator, 0, 0
        combo, 1, {ID_COMBO_METHOD},{','.join(['method: ' + str(x) for x in methods])}
        combo, 1, {ID_COMBO_ORDER},{','.join(['order: ' + str(x) for x in orders])}
        button, start, {ID_BUTTON_START}
        slabel, , {ID_LABEL_SORTERROR}
        separator, 0, 0
        label, sorted array:, 7
        input, sorted, {ID_INPUT_SORTED}
        xlabel, , {ID_LABEL_DURATION},

        tab, AB, 0, 1
        xlabel, SORT_TIME, 0, 0
        label, assignment for python course, 0, 0
        label, used: tkinter, 0, 0 
        label, date: 25.11.2024, 0, 0
        urlbutton, https://github.com/abrosimov-d/sort_time, 0, 0
        '''
        super().template(template)
        super().set_event_listener(self.__event_listener)

    def run(self):
        """
        run SortDialog
        """
        super().run()
    
    def __event_listener(self, event, id, event_data):
        """
        process dialog events (click, key)

        params:
        ----------
        event : str
            event (click, key, close)
        id : int
            id element
        event_data : dict
            data for event

        return:
        ----------
        bool
            True if close was processed
        """
        
        if event =='click' and id == ID_BUTTON_START:
            self.set_text_by_id(ID_INPUT_SORTED, '')
            self.set_text_by_id(ID_LABEL_DURATION, '')
            data = {}
            data['method'] = self.get_selected_index_by_id(ID_COMBO_METHOD)
            data['order'] = self.get_selected_index_by_id(ID_COMBO_ORDER)
            data['array'] = self.get_text_by_id(ID_INPUT_UNSORTED)
            result = self.on_sort_listener(data)
            if 'error' in result:
                self.set_text_by_id(ID_LABEL_SORTERROR, result['error'])
            else:
                self.set_text_by_id(ID_INPUT_SORTED, result['array'])
                self.set_text_by_id(ID_LABEL_DURATION, f"{result['duration']} µs")

        if event == 'key' and id == ID_INPUT_UNSORTED:
            self.set_text_by_id(ID_LABEL_INPUTERROR, '')
            self.set_text_by_id(ID_LABEL_SORTERROR, '')
            data = {}
            data['array'] = self.get_text_by_id(ID_INPUT_UNSORTED)
            result = self.on_sort_listener(data)
            if 'error' in result:
                self.set_text_by_id(ID_LABEL_INPUTERROR, 'invalid array')
            else:
                self.set_text_by_id(ID_LABEL_INPUTERROR, '')
            self.set_text_by_id(ID_INPUT_SORTED, '')
            self.set_text_by_id(ID_LABEL_DURATION, '')
            self.set_enable_by_id(ID_BUTTON_START, 'error' not in result)
        
        if event == 'click' and id == ID_BUTTON_FILL_RANDOMS:
            data = {}
            result = self.on_sort_listener(data)
            self.set_text_by_id(ID_INPUT_UNSORTED, result['array'])
            self.set_text_by_id(ID_LABEL_INPUTERROR, '')
            self.set_text_by_id(ID_LABEL_SORTERROR, '')
            self.set_text_by_id(ID_LABEL_DURATION, '')
            self.set_text_by_id(ID_INPUT_SORTED, '')
            self.set_enable_by_id(ID_BUTTON_START, 'error' not in result)

        if event == 'close':
            return True
