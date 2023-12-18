#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides two lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.

    Returns:
        A new list of length list_length containing all the divisions.
    """
    new = []
    for integer in range(0, list_length):
        try:
            divider = my_list_1[integer] / my_list_2[integer]
        except TypeError:
            print("wrong type")
            divider = 0
        except ZeroDivisionError:
            print("division by 0")
            divider = 0
        except IndexError:
            print("out of range")
            divider = 0
        finally:
            new.append(divider)
    return (new)
