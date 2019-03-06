# Usage: "$python3 iqvia_problemA_ckc.py <test_string>" where you replace <teststring> with any contiguous string you like.

import itertools
import sys

test_string = sys.argv[1]
two_string_set = set()

def split_string(a_string):
    len_2_substrings =  [a_string[x:x+2] for x in range(0, len(a_string), 1) if len(a_string[x:x+2]) == 2]
    len_3_substrings = [a_string[x:x+3] for x in range(0, len(a_string), 1) if len(a_string[x:x+3]) == 3]
    all_substrings = len_2_substrings + len_3_substrings
    set_of_substrings = set()
    forbidden_adjacent_identical_strings = False
    for y in range(1,4):
        all_combinations_gen = itertools.permutations(all_substrings, y)
        for combination in all_combinations_gen:
            for index, value in enumerate(combination[:-1]):
                if value == combination[index+1]:
                    forbidden_adjacent_identical_strings = False
                    break
                else:
                    forbidden_adjacent_identical_strings = True
            if forbidden_adjacent_identical_strings == True:
                new_string = ''.join(combination)
                if new_string == a_string:
                    for index, value in enumerate(combination):
                        set_of_substrings.add(value)
    print(set_of_substrings)

if __name__ == '__main__':
    split_string(test_string)