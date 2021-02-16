from datetime import datetime
import logging
import os


def param_logs(path):
    logs_file_name = os.path.join(path, 'out.txt')
    logging.basicConfig(level='INFO', filename=logs_file_name)
    logger = logging.getLogger()

    def logger_decor(function):
        def func_logger(*args, **kwargs):
            date = datetime.now()
            name = function.__name__
            f_return = function(*args, **kwargs)
            logger.info(f' {date} {name} {args} {kwargs} {f_return}')
        return func_logger
    return logger_decor


@param_logs('')
def some_func(*args, **kwargs):
    return 'done'


some_func('1', '2', name='ARGSKWARGS')
