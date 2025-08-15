import asyncio
from concurrent.futures import ProcessPoolExecutor

from app.services.math_service import (
    compute_pow,
    compute_factorial as _sync_factorial,
    compute_fibonacci as _sync_fibonacci,
)


async def pow_op(
    base: int, exponent: int, executor: ProcessPoolExecutor
) -> int:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, compute_pow, base, exponent)


async def factorial_op(n: int, executor: ProcessPoolExecutor) -> int:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, _sync_factorial, n)


async def fibonacci_op(n: int, executor: ProcessPoolExecutor) -> int:
    loop = asyncio.get_event_loop()
    return await loop.run_in_executor(executor, _sync_fibonacci, n)
