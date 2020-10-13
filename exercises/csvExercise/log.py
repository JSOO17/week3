from colorama import init, Fore


def singleton(cls):

    instances = dict()

    def wrap():
        if cls not in instances:
            instances[cls] = cls()

        return instances[cls]

    return wrap


@singleton
class Log(object):
    @staticmethod
    def info(msg: str):
        print(Fore.RESET + Fore.YELLOW + "Info: ", end="")
        print(Fore.RESET + msg)

    @staticmethod
    def error(msg: str):
        print(Fore.RESET + Fore.RED + "error: ", end="")
        print(Fore.RESET + msg)

    @staticmethod
    def debug(msg: str):
        print(Fore.RESET + Fore.GREEN + "Debug: ", end="")
        print(Fore.RESET + msg)


if __name__ == '__main__':
    log = Log()
