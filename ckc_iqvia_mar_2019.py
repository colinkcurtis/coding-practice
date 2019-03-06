li = [11,1,2,3]
num = 21
import re


# Problem 1
# A solution to the first problem... in "most" cases it will operate in less than O(N^2)
def check_sum(list_of_ints, proposed_sum):
    # the line below will reduce the value of N
    test_list = set(x for x in list_of_ints if x < proposed_sum)
    sum_found = False
    while test_list:
            first_num = test_list.pop()
            for integer in test_list:
                test_sum = first_num + integer
                # This will end the process early unless the sum is found using the final 2 values in the (shortened) list
                if test_sum == proposed_sum:
                    sum_found = True
    print(sum_found)

#check_sum(li,num)

# Problem 2
# first interval is defined as [x1,x2]; second interval is defined as [y1, y2] where x1 is chosen as the min value from both pairs
# three cases:
# 1) where the first interval ([x1,x2]) is "before" the second interval on a number line: x1<y2 & x2<y1
# 2) where the intervals overlap (not just touch at the boundaries): x1<y2 & x2>y1
# 3) where the first interval is "after" the second interval: x1>y2 & x2>y1
li_1 = [[1,5], [8,9], [3,6]]
li_2 = [[1,5], [5,6]]

def check_overlap(list_of_tuples):
    overlap = False
    while len(list_of_tuples) > 1:
        first_interval = list_of_tuples.pop()
        # print(first_interval)
        x1 = min(first_interval)
        x2 = max(first_interval)
        # print(x1)
        # print(x2)
        for second_interval in list_of_tuples:
            y1 = min(second_interval)
            y2 = max(second_interval)
            # print(y1)
            # print(y2)
            if x1<y2:
                if x2>y1:
                    overlap = True
    print(overlap)

# check_overlap(li_1)

# Problem 3
# replace 'latest_slice::sale order' with '(SELECT * FROM sale order WHERE ds = 'LATEST')' 
query = """SELECT * FROM
latest_slice::sale_order so INNER JOIN latest_slice::res_partner rp ON
so.id = rp.id"""

def replace_latest_slice(query_text):
    table_name_1 = query_text.split("::", 2)
    del table_name_1[0]
    table_names_2 = []
    for x in table_name_1:
        table_names_2.append(x.split(' '))
    the_table_names = [x[0] for x in table_names_2]
    new_query_text = query_text.replace('latest_slice::'+str(the_table_names[0]),"(SELECT * FROM "+str(the_table_names[0])+" WHERE ds ='LATEST')" ) \
                    .replace('latest_slice::'+the_table_names[1], "(SELECT * FROM "+the_table_names[1]+" WHERE ds ='LATEST')")
    print(new_query_text)

#replace_latest_slice(query)


# Problem 4

# skipping for now... LEAST experience is with SQL... I CAN do this but it will be slower.

# Given two tables:
# ● deliveries(id INT, day DATE, driver_id INT)
# ● drivers(id INT, name VARCHAR, city VARCHAR)
# Write an SQL query that
# A. counts for each driver, 2017 September deliveries that happened in Dubai (stats).
# B. counts how many drivers made more than 1,000 overall deliveries in Dubai (top drivers).
# C. counts how many days driver John Smith made deliveries in 2017 September (active
# days).
# D. counts deliveries on 2017-09-01 that were assigned to a non-existent driver (errors).




# Problem 5
test_word = 'is'
test_text = 'Hi my name is Colin I like Python. Python is nice and friendly it is for friends.'

# My assumptions are that the text is well-formed, no slang, all words seperated by a space(' ') and no extra spaces.

def percent(word, text):
    # below, we subtract 1 because when we cut an object, there are always 1 more pieces than cuts
    is_counter = text.split('is')
    number_of_is = len(is_counter) - 1
    #print('number of "is":', number_of_is)
    word_counter = text.split(' ')
    number_of_words = len(word_counter)
    #print('number of words:', number_of_words)
    percentage = number_of_is / number_of_words * 100
    print("the percentage of words which are 'is' is: %s %", round(percentage,1))

#percent(test_word, test_text)


# Problem A

test_string_1 = 'abcdef'
test_string_2 = 'abcdefg'
test_string_3 = 'ababcabc'
test_string_4 = 'ccccacccc'

def split_string(a_string):
    # each of these "bites" would be better off as a function which can be passed the desired "bite" size, e.g. 2 or 3 or 4...
    two_size = 2
    two_string = [a_string[x:x+two_size] for x in range(0, len(a_string), two_size)]
    # two_string_odds = {a_string[x:x+two_size] for x in range(0, len(a_string), two_size)}
    # all_two_strings = two_string + two_string_odds
    # adjacent and identical strings are forbidden, so we remove...

    #print(two_string)

    three_size = 3
    three_string = [a_string[x:x+three_size] for x in range(0, len(a_string), three_size)]
    #print(three_string)

    total_strings = two_string + three_string

    print(total_strings)


#split_string(test_string_1)