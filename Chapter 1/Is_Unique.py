#Implement an algorithm to determine if a string has all unique characters. What if you
#cannot use additional data structures?

def unq_char(string):
    # Assuming character set contains only ASCII
    # There can't be more than 128 unique ASCII char in a string, hence the below check
    if len(string) > 128:
        return False

    str_list = [ord(c) for c in string]
    unq_list = set(str_list)
    if len(str_list) != len(unq_list):
        return False

Test = "hb 627jh=j ()"

Chk = unq_char(Test)

