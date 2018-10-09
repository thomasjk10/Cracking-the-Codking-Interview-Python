def unq_char(string):
    # Assuming the entire string contains only ASCII
    # There can't be more than 128 unique ASCII char in a string, hence the below check
    if len(string) > 128:
        return False

    str_list = [ord(c) for c in string]
    # Filter out unique characters in the list
    unq_list = set(str_list)
    if len(str_list) != len(unq_list):
        return False
# Test Cases - Test = "abcd123 e", Test = "abc@$a% 1de)"
Test = "abcde"

Chk = unq_char(Test)
print (Chk)

