def reverse_vowels(s):
    """Reverse vowels in a string.

    Characters which re not vowels do not change position in string, but all
    vowels (y is not a vowel), should reverse their order.

    >>> reverse_vowels("Hello!")
    'Holle!'

    >>> reverse_vowels("Tomatoes")
    'Temotaos'

    >>> reverse_vowels("Reverse Vowels In A String")
    'RivArsI Vewols en e Streng'

    reverse_vowels("aeiou")
    'uoiea'

    reverse_vowels("why try, shy fly?")
    'why try, shy fly?''
    """
    vowels = 'aeiou'
    lst = []
    for char in s:
        if char.lower() in vowels:
            lst.append(char)
            s = s.replace(char, '/')
    lst.reverse()  

    index = 0 
    for char in s:
        if char == '/':
            s = s.replace(char, lst[index], 1)
            index += 1 
    return s

