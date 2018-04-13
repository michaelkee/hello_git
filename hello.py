import sys

def my_decorator(f):
    def func(*args, **kwargs):
        return print(f(*args, **kwargs) + ' ' + sys.argv[-1])
    return func

@my_decorator
def greeting():
    return 'hello'

if __name__ == '__main__':
    greeting()
