''' String compression'''

def strcomp(string):
    str_list = list(string)
    comp_string = ""
    char_count = 1
    non_dupchar = [str_list[0]]
    ''' Create a non-duplicate character list from the set of characters in original string'''
    for i in range(1, len(str_list)):
        if str_list[i] == str_list[i-1]:
            char_count += 1
            continue
        ''' Add the count value obtained to the character'''
        comp_string = comp_string + str_list[i-1] + str(char_count)
        char_count = 1

    comp_string = comp_string + str_list[i] + str(char_count)

    if len(comp_string) > len(string):
        return string

    return comp_string

''' Test Cases - aabcccccaaa, dddddeeeeZZZQUUii, abcd'''

test = input()
result = strcomp(test)
print (result)
