"""
Helpful bytes of code

Author: Rohan Tammara
"""

#===============================================================#
import time

# Pair of methods to time a block of code inspired by MATLAB
def tic(id="default_id"):
    print("<Timer {0} started>".format(id))
    return (id, time.time())

def toc(start):
    duration = time.time() - start[1]
    print("<Timer {0} Stopped> Duration : {1}".format(start[0], duration))
    return duration

#===============================================================#

# Faster alternative to morph.flatten for flattening dictionaries
def dict_flatten(input_dict, separator='.'):

    flat = {}
    continue_flag = False
    for key in input_dict:
        if isinstance(input_dict[key], dict):
            for k in input_dict[key]:
                if isinstance(input_dict[key][k], dict) or isinstance(input_dict[key][k], list):
                    continue_flag = True
                flat[str(key)+separator+str(k)] = input_dict[key][k]
        elif isinstance(input_dict[key], list):
            for i in range(len(input_dict[key])):
                flat[str(key)+'[{}]'.format(i)] = input_dict[key][i]
        else:
            flat[key] = input_dict[key]
    
    if continue_flag:
        flat = dict_flatten(flat)
    
    return flat

#===============================================================#

# Faster alternative to morph.unflatten
# List suppport not present to account for square braces in key names

def dict_unflatten(input_dict, separator='.', has_lists=False):
    """
    Unflatten a dictionary with nested keys.

    Args:
        input_dict (dict): The input dictionary to unflatten.
        separator (str): The separator character used to separate keys. Defaults to '.'.
        has_lists (bool): Whether the input dictionary contains lists. Defaults to False.

    Returns:
        dict: The unflattened dictionary.

    Raises:
        ValueError: If the input dictionary is empty.
        TypeError: If a non-string key is encountered.
    """
    if not input_dict:
        raise ValueError("Input dictionary cannot be empty")

    def nest_leaf(flat_dict, separator=separator):
        out_dict = {}
        keys = [*flat_dict.keys()]

        for key in keys:
            if not isinstance(key, str):
                raise TypeError("Keys must be strings")

            sub_keys = key.split(separator)
            value = flat_dict[key]

            if len(sub_keys) > 1:
                leaf_key = sub_keys[-1]
                trunk_key = separator.join(sub_keys[:-1])

                if trunk_key in out_dict.keys():
                    if not isinstance(out_dict[trunk_key], dict):
                        out_dict[trunk_key] = {}
                    out_dict[trunk_key].update({leaf_key: value})
                else:
                    out_dict[trunk_key] = {leaf_key: value}
            else:
                out_dict.update({key: value})

        return out_dict

    is_flat = lambda key: separator in key

    nested_dict = input_dict
    while any(list(map(is_flat, nested_dict.keys()))):
        nested_dict = nest_leaf(nested_dict)

    return nested_dict

#===============================================================#

# Implementation to get an Ordered Set (list object)
# The first occurring index of an element is considered its index in the ordered set.
def OrderedSet(input_list):
    seen = set()
    return [x for x in input_list if not (x in seen or seen.add(x))]
#===============================================================#

if __name__ == "__main__":
    # Test dictionary 1: Simple nested dictionary
    test_dict1 = {
        'a.b.c': 'value1',
        'a.b.d': 'value2',
        'e.f': 'value3'
    }

    # Expected output:
    # {
    #     'a': {
    #         'b': {
    #             'c': 'value1',
    #             'd': 'value2'
    #         }
    #     },
    #     'e': {
    #         'f': 'value3'
    #     }
    # }
    
    # Test dictionary 2: Dictionary with multiple levels of nesting
    test_dict2 = {
        'a.b.c.d.e': 'value1',
        'a.b.c.d.f': 'value2',
        'a.b.c.g': 'value3',
        'h.i.j': 'value4'
    }
    
    # Expected output:
    # {
    #     'a': {
    #         'b': {
    #             'c': {
    #                 'd': {
    #                     'e': 'value1',
    #                     'f': 'value2'
    #                 },
    #                 'g': 'value3'
    #             }
    #         }
    #     },
    #     'h': {
    #         'i': {
    #             'j': 'value4'
    #         }
    #     }
    # }
    
    # Test dictionary 3: Dictionary with empty values
    test_dict3 = {
        'a.b.c': '',
        'd.e': None,
        'f': 'value1'
    }
    
    # Expected output:
    # {
    #     'a': {
    #         'b': {
    #             'c': ''
    #         }
    #     },
    #     'd': {
    #         'e': None
    #     },
    #     'f': 'value1'
    # }
    
    # Test dictionary 4: Dictionary with non-string keys
    test_dict4 = {
        1: 'value1',
        'a.b': 'value2'
    }
    
    # Expected output: Should raise a TypeError
    
    # Test dictionary 5: Empty dictionary
    test_dict5 = {}
    
    # Expected output: Should raise a ValueError