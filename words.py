def print_upper_words(list,):
    # this should print "HELLO", "HEY", "YO", and "YES"

    for word in list:
        print(word.upper())


print_upper_words(["hello", "hey", "yo", "yes"])


def must_start_with(word):
    for letter in word:
        if letter.startswith("e") or letter.startswith("E"):
            print(letter.upper())


def print_upper_with(list, must_start_with):
    for word in list:
        for letter in must_start_with:
            if word.startswith(letter):
                print(word.upper())
                break
