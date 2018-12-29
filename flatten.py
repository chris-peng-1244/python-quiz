def flatten(d, separator='.'):
    new_dict = {}
    for key, val in d.items():
        if isinstance(val, dict):
            flattened_subdict = flatten(val)
            for flatkey, flatval in flattened_subdict.items():
                new_dict[key + separator + flatkey] = flatval
        else:
            new_dict[key] = val

    return new_dict