import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args,**kwargs):

        logger.info(f"function: {func.__name__}")

        if args:
            logger.info(f"positional parameters: {list(args)}")
        else:
            logger.info("positional parameters: none")
        if kwargs:
            logger.info(f"keyword parameters: {kwargs}")
        else:
            logger.info("keyword parameters: none")
        result = func(*args, **kwargs)

        logger.info(f"return: {result}")

        return result
    return wrapper

@logger_decorator
def hello():
    print("Hello, World!")

@logger_decorator
def position_function(*args):
    return True

@logger_decorator
def keyword_function(**kwargs):
    return logger_decorator

hello()

position_function(10, 20, 30, "Python")

keyword_function(name="Bhagyashri", course="Python", assignment=3)
