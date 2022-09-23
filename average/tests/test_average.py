"""Test suite to ensure that each function words correctly."""

from average import __version__

from average import main


def test_version():
    """Confirm that the version of the program is correct."""
    assert __version__ == "0.1.0"


def test_average_computation_five_numbers():
    """Confirm that it is possible to average together five non-zero numbers."""
    number_list = """-72
        29
        61
        -42
        44"""
    average_value = main.compute_average(number_list)
    assert average_value == ((-72 + 29 + 61 + -42 + 44) / 5)


def test_average_computation_five_numbers_all_zero():
    """Confirm that it is possible to average together five zero numbers."""
    number_list = """0
        0
        0
        0
        0"""
    average_value = main.compute_average(number_list)
    assert average_value == 0


def test_average_computation_five_numbers_all_negative():
    """Confirm that it is possible to average together five non-zero negative numbers."""
    number_list = """-72
        -29
        -61
        -42
        -44"""
    average_value = main.compute_average(number_list)
    assert average_value == ((-72 + -29 + -61 + -42 + -44) / 5)


def test_average_computation_no_provided_numbers():
    """Confirm that it is possible to average together no numbers."""
    number_list = ""
    average_value = main.compute_average(number_list)
    assert average_value == -1
