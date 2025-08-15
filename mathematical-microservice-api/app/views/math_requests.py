from pydantic import BaseModel, Field


class PowRequest(BaseModel):
    base: int = Field(
        ..., ge=0, description="The base number to be raised to a power (>=0)"
    )
    exponent: int = Field(
        ...,
        ge=0,
        description="The exponent to which the base number is raised (>=0)",
    )  # maybe make it possible for negative numbers as well


class FactorialRequest(BaseModel):
    number: int = Field(
        ..., ge=0, description="The number to calculate the factorial of (>=0)"
    )


class FibonacciRequest(BaseModel):
    n: int = Field(
        ...,
        ge=0,
        description="The position in the Fibonacci sequence to calculate (>=0)",
    )
