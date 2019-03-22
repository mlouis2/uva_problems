import sys
lower_bound = 1234
upper_bound = 98765

def check_if_unique_digits(num_a, num_b):
    str_num_a = str(num_a)
    str_num_b = str(num_b)
    while (len(str_num_a) < 5):
        str_num_a = '0' + str_num_a
    while (len(str_num_b) < 5):
        str_num_b = '0' + str_num_b
    str_to_check = str_num_a + str_num_b
    set_of_digits = set(str_to_check)
    if (len(set_of_digits) == len(str_to_check)):
        return True
    return False

first = True
for line in sys.stdin:
    answers = []
    value = int(line.strip())
    if (value == 0):
        break
    elif (first == False):
        print('')
    for i in range(lower_bound, upper_bound):
        if ((i * value) < upper_bound and check_if_unique_digits(i * value, i)):
            answers.append([i * value, i])
    for higher, lower in answers:
        str_higher = str(higher)
        str_lower = str(lower)
        if (len(str_lower) < 5):
            str_lower = '0' + str_lower
        if (len(str_higher) < 5):
            str_higher = '0' + str_higher
        print(str_higher + ' / ' + str_lower + ' = ' + str(value))
    if (len(answers) is 0):
        print('There are no solutions for ' + str(value) + '.')
    first = False
