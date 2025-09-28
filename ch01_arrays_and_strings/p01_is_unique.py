def is_unique_brute_force(characters: str) -> bool:
    for i in range(len(characters)):
        for j in range(i+1,len(characters)):
            if characters[i] == characters[j]:
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