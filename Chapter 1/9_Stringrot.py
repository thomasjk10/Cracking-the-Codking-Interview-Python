''' String compression'''

def is_substring(longstr, substr):
    return longstr.find(substr)

def strrotation(s1, s2):
    if len(s1) == len(s2) != 0:
        return is_substring(s1 + s1, s2) != -1
    return False

string1 = input()
string2 = input()
result = strrotation(string1,string2)
print (result)
