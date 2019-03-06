from collections import deque
import itertools
import sys
from datetime import datetime
case = sys.argv[1]

test_string_1 = 'abcdef' #works
test_string_2 = 'abcdefg'
test_string_3 = 'ababcabc'
test_string_4 = 'ccccacccc'

two_string_set = set()

def split_string(a_string):
    starttime = datetime.now()
    print()
    print('a_string:', a_string)
    print()
    input_string_length = len(a_string)
    print('input_string_length:', input_string_length)
    print()
    input_string_list = [x for x in a_string]
    # print('the input as a list:', input_string_list)
    # print()
    input_string_deque = deque(input_string_list)

    len_2_substrings =  [a_string[x:x+2] for x in range(0, len(a_string), 1) if len(a_string[x:x+2]) == 2]
    print('len_2_substrings:', len_2_substrings)
    print()
    len_3_substrings = [a_string[x:x+3] for x in range(0, len(a_string), 1) if len(a_string[x:x+3]) == 3]
    print('len_3_substrings:', len_3_substrings)
    print()
    all_substrings = len_2_substrings + len_3_substrings
    print('all_substrings:', all_substrings)
    print()

    set_of_substrings = set()

    for y in range(1,10):
        all_combinations_gen = itertools.permutations(all_substrings, y)
        for x in all_combinations_gen:

            new_string = ''.join(x)
            #if len(new_string) < input_string_length+1:
            if new_string == a_string:
                # print(new_string)
                # print()
                # print(x)
                # print()
                for y in x:
                    set_of_substrings.add(y)
    length_of_set_of_substrings = len(set_of_substrings)
    print('set_of_substrings:', set_of_substrings)
    print('length_of_set_of_substrings', length_of_set_of_substrings)




    endtime = datetime.now()
    print('total time:', endtime-starttime)
 
if __name__ == '__main__':
    if case == '1':
        split_string(test_string_1)
    elif case == '2':
        split_string(test_string_2)
    elif case == '3':
        split_string(test_string_3)
    elif case == '4':
        split_string(test_string_4)