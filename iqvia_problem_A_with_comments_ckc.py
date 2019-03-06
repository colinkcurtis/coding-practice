# Usage: "$python3 iqvia_problemA_ckc.py <test_string>" where you replace <teststring> with any contiguous string you like.

#from collections import deque
import itertools
import sys
#from datetime import datetime
test_string = sys.argv[1]

# test_string_1 = 'abcdef' #works
# test_string_2 = 'abcdefg'
# test_string_3 = 'ababcabc'
# test_string_4 = 'ccccacccc'
two_string_set = set()

def split_string(a_string):
    #starttime = datetime.now()
    # print()
    # print('a_string:', a_string)
    # print()
    len_2_substrings =  [a_string[x:x+2] for x in range(0, len(a_string), 1) if len(a_string[x:x+2]) == 2]
    len_3_substrings = [a_string[x:x+3] for x in range(0, len(a_string), 1) if len(a_string[x:x+3]) == 3]
    all_substrings = len_2_substrings + len_3_substrings
    # print('all_substrings:', all_substrings)
    # print()
    set_of_substrings = set()
    forbidden_adjacent_identical_strings = False
    #for y in range(1,int(sys.argv[2])):
    for y in range(1,4):
        all_combinations_gen = itertools.permutations(all_substrings, y)
        for combination in all_combinations_gen:
            for index, value in enumerate(combination[:-1]):
                # print(value)
                # print(combination[index+1])
                # print()
                if value == combination[index+1]:
                    forbidden_adjacent_identical_strings = False
                    break
                else:
                    forbidden_adjacent_identical_strings = True
            if forbidden_adjacent_identical_strings == True:
                new_string = ''.join(combination)
                if new_string == a_string:
                    # print(new_string)
                    # print()
                    # print(combination)
                    # print()
                    for index, value in enumerate(combination):
                        set_of_substrings.add(value)
    #length_of_set_of_substrings = len(set_of_substrings)
    print(set_of_substrings)
    # print('set_of_substrings:', set_of_substrings)
    # print()
    # print('length_of_set_of_substrings', length_of_set_of_substrings)
    # print()
    # endtime = datetime.now()
    # print('total time:', endtime-starttime)
    # print()
 
if __name__ == '__main__':
    # if case == '1':
    #     split_string(test_string_1)
    # elif case == '2':
    #     split_string(test_string_2)
    # elif case == '3':
    #     split_string(test_string_3)
    # elif case == '4':
    #     split_string(test_string_4)
    split_string(test_string)