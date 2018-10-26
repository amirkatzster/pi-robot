import time
from functools import wraps


PROF_DATA = {}

def profile(fn):

    def with_profiling(*args, **kwargs):
        start_time = time.perf_counter()
        ret = fn(*args, **kwargs)
        elapsed_time = time.perf_counter() - start_time

        if fn.__name__ not in PROF_DATA:
            PROF_DATA[fn.__name__] = [0, []]
        PROF_DATA[fn.__name__][0] += 1
        PROF_DATA[fn.__name__][1].append(elapsed_time)

        return ret

    return with_profiling

def print_prof_data():
    for fname, data in PROF_DATA.items():
        max_time = max(data[1])
        avg_time = sum(data[1]) / len(data[1])
        print('Function {} called {} times. '.format(fname, data[0]))
        print('Execution time max: %.3f, average: %.3f'.format(max_time, avg_time))

def clear_prof_data():
    global PROF_DATA
    PROF_DATA = {}