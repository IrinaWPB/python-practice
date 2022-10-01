def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    non_true = [0, [], False, (), None, '']
    return [el for el in lst if el not in non_true]
    