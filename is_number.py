def is_number(s):
    return is_positive_number(s) or is_negative_number(s) or is_scientific_number(s)

def is_scientific_number(s):
    if s.count('e') != 1:
        return False
    
    before_e, after_e = s.split('e')

    return ((is_positive_number(before_e) or is_negative_number(before_e))
    and (is_positive_number(after_e) or is_negative_number(after_e)))

def is_positive_number(s):
    return is_positive_integer(s) or is_positive_real(s)

def is_negative_number(s):
    return is_negative_integer(s) or is_negative_real(s)


def is_negative_real(s):
    return s.startswith('-') and is_positive_real(s[1:])

def is_positive_real(s):
    if s.count('.') != 1:
        return False

    integer_part, decimal_part = s.split('.')
    return is_positive_integer(integer_part) and is_positive_integer(decimal_part)

def is_negative_integer(s):
    return s.startswith('-') and is_positive_integer(s[1:])

def is_positive_integer(s):
    return s.isdigit()