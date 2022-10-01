def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    # lst = list(phrase.lower())
    # if ' ' in lst:
    #     lst.pop(lst.index(' '))
    # lst_copy = lst.copy()
    # lst_copy.reverse()
    # print(lst, lst_copy)
    # if lst == lst_copy:
    #     return True
    # else: 
    #     return False
    
    # no list
    
    edited_phrase = phrase.lower().replace(' ', '')
    return edited_phrase == edited_phrase[::-1]



