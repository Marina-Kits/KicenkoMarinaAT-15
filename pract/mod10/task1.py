import doctest
import re
def password_verification(passw):
    """
    Функция, которая проверяет может ли являться входная строка корректным паролем
    Args:
        passw (str): введённый пароль

    Returns:
        bool: корректность данных
    >>> password_verification('пароль')
    False
    >>> password_verification('password')
    False
    >>> password_verification('3482')
    False
    >>> password_verification('qwerty')
    False
    >>> password_verification('.sh&w?h139HFJS')
    False
    >>> password_verification('lOngPa$$W0Rd')
    False
    >>> password_verification('rtG&3FG#Tr^e')
    True
    >>> password_verification('a^A1@*@1Aa')
    True
    >>> password_verification('ddd222@@@DDD')
    True
    >>> password_verification('oF^a1D@y5%e6')
    True
    >>> password_verification('ld@38kF#WK*d40')
    True
    >>> password_verification('enroi#$*rkdeR#$*092uwedchf34tguv394h')
    True
    """
    symbols=re.compile(r'^(?=.*[a-z].*[a-z])(?=.*\d)(?=.*[$^%@#&*])(?=(.*[$^%@#&*]){3,})(?!.*[,.!?]).{8,}$')
    return bool(symbols.match(passw))
doctest.testmod(verbose=True)