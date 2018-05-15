def check_elements_type(L, expected_class):
    try:
        it = iter(L)
        del it
        for e in L:
            if not isinstance(e, expected_class):
                return False
        return True
    except TypeError:
        return False