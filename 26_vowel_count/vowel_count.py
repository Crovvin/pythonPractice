def vowel_count(phrase):
    """Return frequency map of vowels, case-insensitive.

        >>> vowel_count('rithm school')
        {'i': 1, 'o': 2}
        
        >>> vowel_count('HOW ARE YOU? i am great!') 
        {'o': 2, 'a': 3, 'e': 2, 'u': 1, 'i': 1}
    """

    vowelCount = {}
    VOWELS = set("aeiou")
    phrase = phrase.lower()
    for letter in phrase:
        if letter in VOWELS:
            vowelCount[letter] = vowelCount.get(letter, 0) + 1
    return vowelCount