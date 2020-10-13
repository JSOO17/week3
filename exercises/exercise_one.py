class Memory:
    def __init__(self, function):
        self.function = function
        self.store = {}

    def __call__(self, *args):
        try:
            return self.store[args]
        except KeyError:
            self.store[args] = self.function(*args)
            return self.store[args]


@Memory
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


if __name__ == '__main__':
    result = [fibonacci(x) for x in range(0, 10)]
    print(result)
