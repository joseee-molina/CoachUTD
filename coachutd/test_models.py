import pytest

from .models import Availability, bits_to_availability, availability_to_bits


@pytest.mark.parametrize("input", list(range(2**7)))
def test_symmetric(input):
    """
    Make sure that bits_to_availability and availability_to_bits is symmetric for every possible schedule
    """
    availability = bits_to_availability(input)
    assert availability_to_bits(availability) == input


def test_availability_0():
    """Test 0 availability"""
    assert bits_to_availability(0) == Availability(*[False] * 7)


def test_availability_full():
    """Test full availability"""
    assert bits_to_availability(0b1111111) == Availability(*[True] * 7)
