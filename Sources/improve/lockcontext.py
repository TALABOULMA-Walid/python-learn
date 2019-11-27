from threading import Lock
lock = Lock()

def do_something_dangerous():
    with lock:
        print ('lock is acquired here ? : %s'  %lock.locked())
        raise Exception('oops I forget an erro could happen here!!')

try:
    do_something_dangerous()
except:
    print('got an exception')

with lock:
    print('was able to get here')


### second part
from contextlib import contextmanager

# contextmanager decorator:
# before yield is __enter__ after is __exit__
@contextmanager
def tag(name):
    print("<%s>" %name)
    yield
    print("</%s>" %name)

with tag('h1'):
    print("header text")
#############################
@contextmanager
def openfile(path, mode):
    f = open(path, mode)
    yield f
    f.close()

files = []
for i in range(5000):
    with openfile("venv/main.py", "r") as f:
        files.append(f)

# double check
for f in files:
    if not f.closed:
        print("not closed")

# Third part context manager class

from contextlib import ContextDecorator

class mytagclass(ContextDecorator):
    def __init__(self,tagname='p'):
        self.tagname = tagname

    def __enter__(self):
        print('<%s>' %self.tagname)
        return self
    def __exit__(self, *exc):
        print('<%s>' %self.tagname)
        return False

@mytagclass('h1')
def emithtml():
    print ('hello world html')

# decorated
emithtml()
# or context
with mytagclass('img'):
    print("nice pic")











