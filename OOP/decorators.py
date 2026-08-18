import time

def execution_time(func):
    def wrapper(*args): # *args handles the number of inputs given to a function if we don't know 
        start = time.time()
        func(*args)
        print("TIme taken by ",func.__name__, time.time()-start, "secs")
    return wrapper

# @execution_time
# def hello():
#     print("Hello")
#     time.sleep(2)

# hello()

# @execution_time
# def square(num):
#     return num**2**9

# square(2)

def sanity_check(data_type):
    def outer_wrapper(func):
        def inner_wrapper(*args):
            if type(args[0]) == data_type:
                func(*args)
            else:
                raise TypeError("Input data type is wrong...",*args)
        return inner_wrapper
    return outer_wrapper

@sanity_check(int)
def square(num):
    print(num**2)

square(2)