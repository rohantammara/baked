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
def dict_flatten(input_dict):
    flat = {}
    continue_flag = False
    for key in input_dict:
        if isinstance(input_dict[key], dict):
            for k in input_dict[key]:
                if isinstance(input_dict[key][k], dict) or isinstance(input_dict[key][k], list):
                    continue_flag = True
                flat[str(key)+'.'+str(k)] = input_dict[key][k]
        elif isinstance(input_dict[key], list):
            for i in range(len(input_dict[key])):
                flat[str(key)+'[{}]'.format(i)] = input_dict[key][i]
        else:
            flat[key] = input_dict[key]
    
    if continue_flag:
        flat = dict_flatten(flat)
    
    return flat

#===============================================================#

# Implementation to get an Ordered Set (list object)
# The first occurring index of an element is considered its index in the ordered set.
def OrderedSet(input_list):
    ordered = []
    for i in range(len(input_list)):
        item = input_list[i]
        if not item in ordered:
            ordered.append(item)
    return ordered

#===============================================================#
