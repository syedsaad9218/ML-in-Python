from concurrent.futures import ProcessPoolExecutor
import time

def square_number(number):
    time.sleep(1)
    return f"square : {number * number}"

if __name__ == "__main__":
    start_time = time.time()

    number = [1,2,3,4,5,6,7,8,9]

    with ProcessPoolExecutor(max_workers=3) as executor:
        results = executor.map(square_number, number)
        for result in results:
            print(result)

    end_time = time.time()

    print(f"total time: {end_time - start_time:.2f} seconds")
