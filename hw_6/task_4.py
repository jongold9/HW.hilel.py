from datetime import datetime
from time import sleep


def wait(function):
    def wrap(*args, **kwargs):
        for sec in range(3, 0, -1):
            print(sec)
            sleep(1)
        function(*args, **kwargs)
    return wrap


@wait
def actual_time():
    time = datetime.now().strftime("%H:%M")
    print(time)


actual_time()
