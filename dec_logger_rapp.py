from datetime import datetime
import logging
import os
import hashlib


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
            return f_return
        return func_logger
    return logger_decor


@param_logs('')
def some_func(*args, **kwargs):
    return 'done'


some_func('1', '2', name='ARGSKWARGS')


@param_logs('')
def md5_hash(path):
    m = hashlib.md5()

    with open(path, encoding='utf-8') as f:
        while True:
            line = f.readline()
            if not line:
                break
            m.update(line.encode('utf-8'))
            yield m.hexdigest()


md5_hash('links_file.txt')
