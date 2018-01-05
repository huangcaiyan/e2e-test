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
        elif running_system == 'Windows':
            current_system_name = 'Windows'
        else:
            current_system_name = 'others'
            print('自动化测试程序在 非Mac 或 windows 机器上运行！')
        return current_system_name
