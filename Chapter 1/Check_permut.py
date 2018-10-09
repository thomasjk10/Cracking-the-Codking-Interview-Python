# Approach 1 - Sort both the given strings and then compare if they are the same
def chk_permu(s1,s2):
    # Assuming both strings contain only ASCII
    # There can't be more than 128 unique ASCII char in a string, hence the below check
    if len(str1) > 128 or len(str2) > 128:
        return False
    if len(str1) == len(str2):
        if list(sorted(str1)) != list(sorted(str2)):
            return False

# Test Case1 - str1 = "abcd", str2 = "dbca"
# Test Case2 - str1 = "abc d", str2 = "cdba"
str1 = input()
str2 = input()
result = chk_permu(str1,str2)
