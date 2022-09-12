def is_anagram(test, original):
    while True:
        for x in test:
            if x == x in original and len(test) == len(original):
                return True
            else:
                return False




