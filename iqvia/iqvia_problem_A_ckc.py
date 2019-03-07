# Usage: "$python3 iqvia_problemA_ckc.py <test_string>" where you replace <teststring> with any contiguous string you like.

from itertools import permutations
from sys import argv
from math import floor

test_string = argv[1]
two_string_set = set()
test_string_length = len(test_string)
loop_length = floor(test_string_length/2)+1

def split_string(a_string):
    len_2_substrings =  [a_string[x:x+2] for x in range(0, len(a_string), 1) if len(a_string[x:x+2]) == 2]
    len_3_substrings = [a_string[x:x+3] for x in range(0, len(a_string), 1) if len(a_string[x:x+3]) == 3]
    all_substrings = len_2_substrings + len_3_substrings
    set_of_substrings = set()
    forbidden_adjacent_identical_strings = False
    for y in range(1,loop_length):
        all_permutations_gen = permutations(all_substrings, y)
        for permutation in all_permutations_gen:
            for index, value in enumerate(permutation[:-1]):
                if value == permutation[index+1]:
                    forbidden_adjacent_identical_strings = False
                    break
                else:
                    forbidden_adjacent_identical_strings = True
            if forbidden_adjacent_identical_strings == True:
                new_string = ''.join(permutation)
                if new_string == a_string:
                    for index, value in enumerate(permutation):
                        set_of_substrings.add(value)
    list_of_substrings = list(set_of_substrings)
    list_of_substrings.sort(key=str.lower)
    print(list_of_substrings)

if __name__ == '__main__':
    split_string(test_string)