import sys
import os
import time
import asyncio
from concurrent.futures import ProcessPoolExecutor

from app.services.math_service_async import fibonacci_op, factorial_op, pow_op
from app.services.math_service import (
    compute_pow,
    compute_factorial,
    compute_fibonacci,
)

# Add project root to import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

# Create the executor once
executor = ProcessPoolExecutor()


def synch_test():
    print("SYNCHRONOUS TEST:")
    start = time.perf_counter()
    compute_fibonacci(42)
    compute_factorial(10000)
    compute_pow(2, 200000)
    end = time.perf_counter()
    print(
        f"Time taken for synchronous operations: {end - start:.4f} seconds)\n"
    )


async def async_test():
    print("ASYNCHRONOUS TEST:")
    start = time.perf_counter()
    await asyncio.gather(
        fibonacci_op(42, executor),
        factorial_op(10000, executor),
        pow_op(2, 200000, executor),
    )
    end = time.perf_counter()
    print(
        f"Time taken for asynchronous operations: {end - start:.4f} seconds)\n"
    )


def secondary_synch_test():
    print("\n\nSYNCHRONOUS TEST2:")
    start = time.perf_counter()
    compute_fibonacci(42)
    compute_fibonacci(42)
    compute_fibonacci(42)
    compute_fibonacci(42)
    compute_fibonacci(42)
    compute_factorial(6000)
    compute_factorial(6000)
    compute_pow(2, 150000)
    compute_pow(2, 150000)
    compute_pow(2, 150000)
    end = time.perf_counter()
    print(f"Total synchronous time: {end - start:.4f} seconds\n")


async def secondary_async_test():
    print("ASYNCHRONOUS TEST2:")
    start = time.perf_counter()
    tasks = [
        fibonacci_op(42, executor),
        fibonacci_op(42, executor),
        fibonacci_op(42, executor),
        fibonacci_op(42, executor),
        fibonacci_op(42, executor),
        factorial_op(6000, executor),
        factorial_op(6000, executor),
        pow_op(2, 150000, executor),
        pow_op(2, 150000, executor),
        pow_op(2, 150000, executor),
    ]
    await asyncio.gather(*tasks)
    end = time.perf_counter()
    print(f"Total asynchronous time: {end - start:.4f} seconds\n")


if __name__ == "__main__":
    secondary_synch_test()
    asyncio.run(secondary_async_test())
