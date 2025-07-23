from pydantic import BaseModel, Field

class PowRequest(BaseModel):
    base: int = Field(..., ge= 0, description="The base number to be raised to a power (>=0)")
    exponent: int = Field(...,ge = 0, description="The exponent to which the base number is raised (>=0)") #maybe make it possible for negative numbers as well