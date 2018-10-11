def oneaway(string1,string2):
    tmp_s1list = list(string1)
    tmp_s2list = list(string2)
    '''Check to see if there is any new inserted character in string2 with respect to string1'''
    if len(string1) < len(string2):
        if [char for char in tmp_s2list if char not in tmp_s1list]:
            return True
    '''Check to see if there is any deleted character in string2 with respect to string1'''
    if len(string1) > len(string2):
        if [char for char in tmp_s1list if char not in tmp_s2list]:
            return True
    '''Check to see if any character in string2 has been replaced from original comparison to string1'''
    if len(string1) == len(string2):
        if [char for char in tmp_s2list if char not in tmp_s1list]:
            return True

    '''If none of the above conditions are satisfied, its implied that more than one edit was done'''

    return False

''' Test inputs:
pale,  ple
pales, pale
pale,  bale
pale,  bake'''

st1 = input()
st2 = input()
result = oneaway(st1,st2)
