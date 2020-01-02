from functools import wraps  # this will help to keep __name__ track from funcion calls
import logging
import time
import wdata_config.loggers as loggers
import concurrent.futures

# This function will add a log report of args passed to a function decorated
def func_logger(original_func):
    logger = loggers.create_info_log(original_func.__name__)
    
    @wraps(original_func)
    def wrapper_func(*args, **kwargs):
        logger.info(f"Running with args {args} and kwargs {kwargs}")
        
        return original_func(*args, **kwargs)
    return wrapper_func


# This function will add time runing duration of a function decorated
def func_time_logger(original_func):
    logger = loggers.create_info_log(original_func.__name__)

    @wraps(original_func)
    def wrapper_func(*args, **kwargs):
        starting_time = time.time()
        
        variable = original_func(*args, **kwargs)
        
        ending_time = time.time()
        result = ending_time - starting_time
        
        logger.info(f"{original_func.__name__} ran in: {result} sec")
        return variable
        
    return wrapper_func





# This function will create threads
# use in the future some threads decorators