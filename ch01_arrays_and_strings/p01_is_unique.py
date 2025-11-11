def is_unique_brute_force(string: str) -> bool:
    """
    Checks whether or not a string is unique using a brute force method.
    Returns True or False, accordingly.
    """
    for i in range(len(string)):
        for j in range(i+1,len(string)):
            if string[i] == string[j]:
                return False
    return True

def hash_function(character: str, table_size: int) -> int:
    """
    Compute the hash number which is used for the index within the hash table.
    """
    return ord(character) % table_size

def is_unique_hash_table(string: str) -> bool:
    """
    Checks whether or not a string is unique using a hash table.
    Disclaimer: Not (significantly) faster than the brute force method.
    Returns True or False, accordingly.
    """
    table_size = 100
    tables = [[] for _ in range(table_size)]
    for character in string:
        key = hash_function(character, table_size)
        for elem in tables[key]:
            if elem == character:
                return False
        tables[key].append(character)
    return True

def is_unique_bit_vector(string: str) -> bool:
    """
    Checks whether or not a string is unique using a bit vector.
    Unicode of character used for position shift of the mask which is compared to the bit_vector.
    Returns True or False, accordingly.
    """
    bit_vector = 0 # 000...0
    for character in string:
        position = ord(character) # unicode of character
        mask = 1 << position # shifting the one bit to the position of the character: 000...1 --> 000...100 if position = 2
        if (bit_vector & mask) != 0: # With &-Operator check if the masked position is already set to one in the bit_vector
            return False
        bit_vector |= mask # Set the masked position inside the bit_vector to one
    return True

def is_unique_sort_and_compare(string: str) -> bool:
    """
    Checks whether or not a string is unique sorting a string and comparing each neighboring character.
    """
    string = sorted(string)
    for i in range(len(string)-1):
        if string[i] == string [i+1]:
            return False
    return True