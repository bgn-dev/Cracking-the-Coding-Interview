def check_permutation_sort(string_one: str, string_two: str) -> bool:
    # Case: Permutations have the same length, only the order can be different of the characters are different
    if len(string_one) != len(string_two):
        return False
    # Case: Two permutations of each other are the same when sorted 
    string_one = sorted(string_one)
    string_two = sorted(string_two)
    if string_one != string_two:
        return False
    
    return True

def check_permutation_unicode_count(string_one: str, string_two: str) -> bool:
    # Case: Permutations have the same length, only the order can be different of the characters are different
    if len(string_one) != len(string_two):
        return False
    
    unicode_count_one = 0
    unicode_count_two = 0

    for c in string_one:
        unicode_count_one += ord(c)
    
    for c in string_two:
        unicode_count_two += ord(c)

    if unicode_count_one != unicode_count_two:
        return False
    return True