from datetime import datetime
import logging


logging.basicConfig(level='INFO', filename='logs2.txt')
logger = logging.getLogger()


def logger_decor(function):

    def func_logger(*args, **kwargs):
        date = datetime.now()
        name = function.__name__
        f_return = function(*args, **kwargs)
        logger.info(f' {date} {name} {args} {kwargs} {f_return}')
        return f_return
    return func_logger


@logger_decor
def some_func(*args, **kwargs):
    return 'done'


some_func('1', '2', name='ARGSKWARGS')
