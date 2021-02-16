# from datetime import datetime
# import logging
#
#
# logging.basicConfig(level='INFO', filename='logs2.txt')
# logger = logging.getLogger()
#
#
# def logger_decor(function):
#
#     def func_logger(*args, **kwargs):
#
#         date = datetime.now()
#         name = function.__name__
#         f_return = function(*args, **kwargs)
#
#         logger.info(f' {date} {name} {args} {kwargs} {f_return}')
#
#     return func_logger
#
#
# @logger_decor
# def some_func(*args, **kwargs):
#     return 'done'
#
#
# some_func('1', '2', name='ARGSKWARGS')

from datetime import datetime
from inspect import signature
import os


def parameterized_logger(path):
    logs_file_name = os.path.join(path, 'out.txt')

    def logger(some_function):
        def log_function(*args, **kwargs):

            now = datetime.now()
            function_name = some_function.__name__

            sig = signature(some_function)
            ba = sig.bind(*args, **kwargs)
            args = ba.args
            kwargs = ba.kwargs

            function_return = some_function(*args, **kwargs)

            f = open(logs_file_name, 'w')
            f.write(str(now) + '\t' + str(function_name) + '\t' +
                    str(args) + str(kwargs) + '\t' +
                    str(function_return) + '\t' + '\n')
            f.close()
            return
        return log_function

    return logger


@parameterized_logger('1')  # put path to logs as an argument
def say_something(*args, **kwargs):
    return 'func_result'


say_something('Hello!', 'Bay', name='John')