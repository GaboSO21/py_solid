import logging
import threading


class SingletonMeta(type):

    _instances = {}
    _lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                cls._instances[cls] = super(
                    SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class Logger(metaclass=SingletonMeta):

    _logger = None

    def __init__(self):
        # Initialize the logger during object creation
        self._initialize_logger()

    # Method to initialize logger
    def _initialize_logger(self):
        print("<Logger init> initializing logger...")
        # Create a logger object with the specified name
        self._logger = logging.getLogger('my_logger')
        # Set the logging level to DEBUG
        self._logger.setLevel(logging.DEBUG)

        # Create a file handler to log messages to a file
        file_handler = logging.FileHandler('logs/my_log_file.log')
        # Set the file handler logging level to DEBUG
        file_handler.setLevel(logging.DEBUG)

        # Create a console handler to log messages to the console
        console_handler = logging.StreamHandler()
        # Set the console handler to logging level to INFO
        console_handler.setLevel(logging.INFO)

        # Define the log message format
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        # Set the formatter for both the file and console handlers
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add the file and console handlers to the logger
        self._logger.addHandler(file_handler)
        self._logger.addHandler(console_handler)

    def getLogger(self):
        return self._logger


# Usage
logger = Logger().getLogger()
logger2 = Logger().getLogger()
logger.debug("This is a debug message")
logger.info("This is an info message")
logger.warning("This is a warning message")
logger.error("This is an error message")
logger.critical("This is a critical message")
print(logger == logger2)
