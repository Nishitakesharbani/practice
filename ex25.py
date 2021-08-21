def break_word(stuff):
    """This function will break your word"""
    words=stuff.split(' ')
    return words

def sort_words(words):
    """sort the word"""
    return sorted(words)

def print_first_word(words):
    """Prints the first word after popping it off"""
    word=words.pop(0)
    print(word)

def print_last_word(words):
    """Prints the last word after popping it off"""
    word=words.pop(-1)
    print(word)

def sort_sentence(sentence):
    """Takes the full sentence and return the sorted part"""
    words=break_word(sentence)
    return sort_words(words)