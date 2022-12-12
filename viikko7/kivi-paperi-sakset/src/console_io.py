class ConsoleIo:
    def write(self, message):
        print(message)

    def read(self, message):
        return input(message)


default_console_io = ConsoleIo()
