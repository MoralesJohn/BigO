import time

def simple_for(n):
    sum = 0
    start = time.clock()
    for _ in range(n):
        sum += 1
    end = time.clock()
    # convert runtime to seconds and return
    return 1000 * (end - start)

def nested_loop(n):
    sum = 0
    start = time.clock()
    for _ in range(n):
        for _ in range(n):
            sum += 1
    end = time.clock()
    return 1000 * (end - start)

def nested_square(n):
    sum = 0
    start = time.clock()
    for _ in range(n):
        for _ in range(n * n):
            sum += 1
    end = time.clock()
    return 1000 * (end - start)

def nested_truncated(n):
    sum = 0
    start = time.clock()
    for i in range(n):
        for _ in range(i):
            sum += 1
    end = time.clock()
    return 1000 * (end - start)

def nested_squared_trunc(n):
    sum = 0
    start = time.clock()
    for i in range(n):
        for j in range(i * i):
            for _ in range(j):
                sum += 1
    end = time.clock()
    return 1000 * (end - start)

def nested_squared_conditional(n):
    sum = 0
    start = time.clock()
    for i in range(1, n):
        for j in range(1, i * i):
            if (j % i == 0):
                for _ in range(j):
                    sum += 1
    end = time.clock()
    return 1000 * (end - start)

n_set = [10, 50, 100, 1000]
for n in n_set:
    print("n =", n, nested_squared_conditional(n))
