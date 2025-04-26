import multiprocessing
import math
import sys
import time

sys.set_int_max_str_digits(100000)

def computer_factorial(number):
    print(f"computing factorial of {number}")
    result = math.factorial(number)
    print(f"factorial of {number} is {result}")
    return result

if __name__ == "__main__":
    number = [500,600,700,800]
    start_time = time.time()

    with multiprocessing.Pool() as pool:
        results = pool.map(computer_factorial,number)

        end_time = time.time()
        total_time = end_time - start_time
        print(f"the total time is : {total_time}")