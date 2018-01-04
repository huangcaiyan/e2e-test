import platform


class BaseClass:
    def __init__(self):
        pass

    @staticmethod
    def get_system_name():
        running_system = platform.system()
        print("system=>", running_system)
        if running_system == 'Darwin':
            current_system_name = 'Mac'
            return current_system_name
        elif running_system == 'Windows':
            current_system_name = 'Windows'
            return current_system_name
        else:
            current_system_name = 'others'
            return current_system_name

    def get_accounting_book_property(self):

