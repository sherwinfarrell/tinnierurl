import logging 

class CustomLogger():
    def __init__(self, name):
        self.logger = logging.getLogger(name)
        formatter = logging.Formatter(
            '%(asctime)s | %(name)s | [%(levelname)s] : %(name)s | %(lineno)d | %(module)s | %(filename)s | %(message)s')
        self.logger.setLevel(logging.DEBUG)

        stream_handler = logging.StreamHandler()
        stream_handler.setLevel(logging.INFO)
        stream_handler.setFormatter(formatter)

        logFilePath = "logs/my.log"
        file_handler = logging.FileHandler(logFilePath)
        file_handler.setFormatter(formatter)
        file_handler.setLevel(logging.DEBUG)

        self.logger.addHandler(file_handler)
        self.logger.addHandler(stream_handler)

    def get_logger(self):
        return self.logger