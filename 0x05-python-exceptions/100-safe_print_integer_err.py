#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    """Prints an integer with "{:d}".format().

    If a ValueError message is caught, a corresponding
    message is printed to standard error.

    Args:
        value (int): The integer to print.

    Returns:
        If a TypeError or ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except Exception as dr:
        print("Exception type: {type:(dr).__name__}, Message: {str(dr)}", file=sys.stderr)
        return (False)
