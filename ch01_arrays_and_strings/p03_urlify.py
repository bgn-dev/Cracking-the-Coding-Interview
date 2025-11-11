def urlify_brute_force(string: str, length: int) -> str:
    """
    Create a URLify by manipulating the string directly.
    Account for the new index at each step.
    """
    indexer = 0
    for i in range(length):
        if string[i+indexer] == ' ':
            string = string[:i+indexer] + '%20' + string[i+1+indexer:]
            # Replace a space with %20, thus we add two new characters to the string
            indexer += 2
    
    return string

if __name__ == '__main__':
    string = ' Mr John Smith  '
    length = len(string)
    result = urlify_brute_force(string, length)
    print(result)