def check_elements_type(L, expected_class):
    for e in L:
        if not isinstance(e, expected_class):
            return False
    return True