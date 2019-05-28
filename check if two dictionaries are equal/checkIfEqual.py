def equal_dicts(d1, d2, ignore_keys):
    """
    Checks if the two passed dictionaries/objects are same with some keys ignored
    :param d1: Dictionary 1
    :param d2: Dictionary 2
    :param ignore_keys: List of keys which need to be ignored
    :return: Boolean according to result
    """
    return {k: v for k, v in d1.items() if k not in ignore_keys} == {k: v for k, v in d2.items() if
                                                                     k not in ignore_keys}
