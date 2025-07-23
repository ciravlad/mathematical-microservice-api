from fastapi import APIRouter
from ..views.math_requests import PowRequest, FactorialRequest
from ..views.math_responses import ResultResponse
from ..services.math_service import compute_pow, compute_factorial

router = APIRouter()


@router.post("/pow", response_model= ResultResponse)
def pow_handler(request: PowRequest):
    """
    Calculate the power of a base raised to an exponent.
    """
    result = compute_pow(request.base, request.exponent)
    # dont forget to add a log_request as well ex log_request("pow", request.model_dump(), result)
    return ResultResponse(result=result)

@router.post("/factorial", response_model=ResultResponse)
def factorial_handler(request: FactorialRequest):
    """
    Calculate the factorial of a number.
    """
    result = compute_factorial(request.number)
    # dont forget to add a log_request as well ex log_request("factorial", request.model_dump(), result)
    return ResultResponse(result=result)
