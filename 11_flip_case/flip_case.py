def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    new_str = ''
    for char in phrase:
        if char in [to_swap.lower(), to_swap.upper()]:
            char = char.swapcase()
        else: 
            char = char
        new_str += char
    return new_str