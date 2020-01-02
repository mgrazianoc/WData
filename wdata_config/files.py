import os
from contextlib import contextmanager



@contextmanager
def act_on_dir(path):
    cwd = os.getcwd()
    os.chdir(f"{cwd}{path}")
    
    yield
    
    os.chrdir(cwd)
    
