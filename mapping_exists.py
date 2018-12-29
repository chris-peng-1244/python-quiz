def mapping_exists(s1, s2):
    if len(s1) != len(s2):
        return False

    mapping = {}
    for char1, char2 in zip(s1, s2):
        if char1 not in mapping:
            mapping[char1] = char2
        elif mapping[char1] != char2:
            return False
        
    return True