def is_unique_brute_force(characters: str) -> bool:
    for i in range(len(characters)):
        for j in range(i+1,len(characters)):
            if characters[i] == characters[j]:
                print(characters[i],characters[j])
                return False
    return True

def hash_function(character: str, table_size: int) -> int:
    return ord(character) % table_size

def is_unique_hash_table(string: str) -> bool:
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
    bit_vector = 0 # 000...0
    for character in string:
        position = ord(character) # unicode of character
        mask = 1 << position # shifting the one bit to the position of the character: 000...1 --> 000...100 if position = 2
        if (bit_vector & mask) != 0: # With &-Operator check if the masked position is already set to one in the bit_vector
            return False
        bit_vector |= mask # Set the masked position inside the bit_vector to one
    return True