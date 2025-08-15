import pytest
from ..services.math_service import compute_pow


@pytest.mark.parametrize(
    "base,exp,expected",
    [
        (2, 3, 8),
        (5, 0, 1),
        (10, -1, 0.1),
        (2, 10, 1024),
    ],
)
def test_pow_op(base, exp, expected):
    assert compute_pow(base, exp) == pytest.approx(expected)


@pytest.mark.benchmark(group="pow")
def test_pow_benchmark(benchmark):
    # benchmark pow on a typical large exponent
    benchmark(compute_pow, 2, 1000000)
