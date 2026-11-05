import pytest
import akamai


def test_sum_as_string():
    assert akamai.sum_as_string(1, 1) == "2"
