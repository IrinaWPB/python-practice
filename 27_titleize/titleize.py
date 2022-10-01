def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """
    new_str = ''
    my_lst = phrase.lower().split(' ')
    for el in my_lst:
        new_str += f"{el.capitalize()} "
    return new_str.strip()


