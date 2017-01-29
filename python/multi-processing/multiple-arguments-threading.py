from multiprocessing import Pool
from functools import partial

threads = 0


def f(fixed, iterable):
    global threads
    threads += 1
    print "Fixed: " + str(fixed) + ", Iterable: " + str(iterable)
    return fixed * iterable

if __name__ == '__main__':
    pool = Pool(4)
    num_sequence = [1, 2, 3]
    results = pool.map(partial(f, 2), num_sequence)
    pool.close()
    pool.join()

    print("Results: " + str(results))
    print("Threads: " + str(threads))
