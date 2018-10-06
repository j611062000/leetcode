def findAndReplacePattern(words, pattern):
    """
    :type words: List[str]
    :type pattern: str
    :rtype: List[str]
    """
    
    def trans(word):
        temp1 = {}
        for char in word:
            temp1[char] = temp1.get(char, len(temp1) + 1)
        
        return "".join([chr(temp1[char]+97) for char in word])

    pattern = trans(pattern)
    temp = []

    for word in words:
        if trans(word) == pattern:
            temp.append(word)
    return temp

print(findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"],"abb"))
