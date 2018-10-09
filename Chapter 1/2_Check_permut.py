# ------------------------------------------------------------------------------
# Approach 1 - Sort both the given strings and then compare if they are the same
# ------------------------------------------------------------------------------
def chk_permu(s1,s2):
    # Assuming both strings contain only ASCII
    # There can't be more than 128 unique ASCII char in a string, hence the below check
    if len(str1) > 128 or len(str2) > 128:
        return False
    if len(str1) == len(str2):
        if list(sorted(str1)) != list(sorted(str2)):
            return False
    return True

# Test Case1 - str1 = "abcd", str2 = "dbca"
# Test Case2 - str1 = "abc d", str2 = "cdba"
str1 = input()
str2 = input()
result = chk_permu(str1,str2)

# ------------------------------------------------------------------------------
# Approach 2 - Check if length of counter dictionary varies after processing
#              the first occurence or a char in the second string when length of  
#              dictinary increases 
# ------------------------------------------------------------------------------

from collections import Counter
def chk_permu(s1,s2):
    if len(s1) > 128 or len(s2) > 128:
        return False

    if len(s1) != len(s2):
        return False

    char_count = Counter()
    for char in s1:
        char_count[char] += 1
    init_len = len(char_count)
    for char in s2:
        char_count[char] += 1
        fin_len = len(char_count)
        if fin_len - init_len != 0:
            return False

    return True

str1 = input()
str2 = input()
result = chk_permu(str1,str2)
