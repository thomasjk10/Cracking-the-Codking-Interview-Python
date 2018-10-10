    '''Check if given string is a permuation of a palindrome'''
def palind(string):
    '''Check if length of string is even numbered or not, since even numbered string will not be a palindrome'''
    if len(string) %2 == 0:
        return False
    '''Put the string into a list, and create another list containing non-duplicate characters from the first
    list and then form another list containing the middle char that will be present in all permutations of the string'''
    char_list = list(string.lower())
    nondup_char = set(char_list)
    check_palin = [i for i in char_list if char_list.count(i)%2 != 0]

    '''If there is a middle character found-Palindrome feasibility is Yes'''
    if len(check_palin) == 1:
        return True

inp = input()
mod_inp = inp.replace(" ", "")
result = palind(mod_inp)
