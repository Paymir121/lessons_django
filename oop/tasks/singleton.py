class Logger:
    instance = None

    def __new__(cls):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.logs: list[str] = []

    def log(self, message: str):
        self.logs.append(message)

    def get_logs(self):
        return self.logs

if __name__ == '__main__':
    logger1 = Logger()
    logger2 = Logger()

    logger1.log("First message")
    logger2.log("Second message")

    assert logger1 is logger2, "Logger is not a singleton!"
    assert logger1.get_logs() == ["First message", "Second message"]