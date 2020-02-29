def even_q(element):
    '''Вычисляет четность чисел
    >>> even_q(1)
    1
    >>> even_q(2)
    0
    '''
    return element % 2 

import doctest
# автоматически проверяет тесты в документации
doctest.testmod()
