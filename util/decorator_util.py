import sys
def exit_test(func):
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        if func(*args, **kw):
            print('true')
        else:
            print('false')
            sys.exit()
    return wrapper

        