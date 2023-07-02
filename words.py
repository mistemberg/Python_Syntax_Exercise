def print_upper_words(words):
    for word in words:
        print(word.upper())


def print_upper_words2(words):
    for word in words:
        if word.startswitch("e") or word.startswitch("E"):
            print(word.upper())


def print_upper_words3(words, must_start_with):
    for word in words:
        if word.startswitch(letter):
            print(word.upper())
            break