from fastapi import APIRouter
from ..views.math_requests import (
    PowRequest,
    FactorialRequest,
    FibonacciRequest,
)
from ..views.math_responses import ResultResponse
from ..services.math_service import (
    compute_pow,
    compute_factorial,
    compute_fibonacci,
)
from ..services.log_service import log_request

router = APIRouter()


@router.post("/pow", response_model=ResultResponse)
def pow_handler(request: PowRequest):
    """
    Calculate the power of a base raised to an exponent.
    """
    result = compute_pow(request.base, request.exponent)
    log_request("pow", request.model_dump(), result)
    return ResultResponse(result=result)


@router.post("/factorial", response_model=ResultResponse)
def factorial_handler(request: FactorialRequest):
    """
    Calculate the factorial of a number.
    """
    result = compute_factorial(request.number)
    log_request("factorial", request.model_dump(), result)
    return ResultResponse(result=result)


@router.post("/fibonacci", response_model=ResultResponse)
def fibonacci_handler(request: FibonacciRequest):
    """
    Calculate the nth Fibonacci number.
    """
    result = compute_fibonacci(request.n)
    log_request("fibonacci", request.model_dump(), result)
    return ResultResponse(result=result)
