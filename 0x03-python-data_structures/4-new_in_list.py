def new_in_list(my_list, idx, element):
    if (idx < 0 and idx >= len(my_list)):
        return mylist
    """
    creating a shallow copy
    of the list
    """
    new = my_list[:]
    new[idx] = element
    return new
