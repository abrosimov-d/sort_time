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
    Класс для создания диалогового окна сортировки с использованием tkinter.

    Атрибуты:
    ----------
    on_sort_listener : function
        Функция-обработчик, вызываемая при выполнении сортировки.
    methods : list
        Список методов сортировки.
    orders : list
        Список порядков сортировки.

    Методы:
    -------
    __init__(self, on_sort_listener, methods, orders):
        Инициализация класса SortDialog с заданной функцией-обработчиком и списками методов и порядков сортировки.
        
    run(self):
        Запускает основное диалоговое окно сортировки.
        
    __event_listener(self, event, id, event_data):
        Обрабатывает события интерфейса (нажатия кнопок, ввод данных и т.д.).
    """
    
    def __init__(self, on_sort_listener, methods, orders):
        """
        Инициализирует класс SortDialog, создавая шаблон диалогового окна с указанными параметрами.

        Параметры:
        ----------
        on_sort_listener : function
            Функция-обработчик, вызываемая при выполнении сортировки.
        methods : list
            Список методов сортировки.
        orders : list
            Список порядков сортировки.
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
        label, date: XX.11.2024, 0, 0
        urlbutton, https://github.com/abrosimov-d/sort_time, 0, 0
        '''
        super().template(template)
        super().set_event_listener(self.__event_listener)

    def run(self):
        """
        Запускает основное диалоговое окно сортировки.
        """
        super().run()
    
    def __event_listener(self, event, id, event_data):
        """
        Обрабатывает события интерфейса (нажатия кнопок, ввод данных и т.д.).

        Параметры:
        ----------
        event : str
            Тип события (например, 'click', 'key', 'close').
        id : int
            Идентификатор элемента интерфейса, вызвавшего событие.
        event_data : dict
            Дополнительные данные события.

        Возвращает:
        ----------
        bool
            True, если событие 'close' успешно обработано.
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
