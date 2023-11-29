def spellingAlphabetConverter(word):
    words = {
        "a": "Alpha",
        "b": "Bravo",
        "c": "Charlie",
        "d": "Delta",
        "e": "Echo",
        "f": "Foxtrot",
        "g": "Golf",
        "h": "Hotel",
        "i": "India",
        "j": "Juliet",
        "k": "Kilo",
        "l": "Lima",
        "m": "Mike",
        "n": "November",
        "o": "Oscar",
        "p": "Papa",
        "q": "Quebec",
        "r": "Romeo",
        "s": "Sierra",
        "t": "Tango",
        "u": "Uniform",
        "v": "Victor",
        "w": "Whiskey",
        "x": "Xray",
        "y": "Yankee",
        "z": "Zulu",
        "1": "One",
        "2": "Two",
        "3": "Three",
        "4": "Four",
        "5": "Five",
        "6": "Six",
        "7": "Seven",
        "8": "Eight",
        "9": "Nine",
        "0": "Zero",
        "@": "<At>",
        " ": "<Space>",
        ".": "<Dot>",
        ",": "<Comma>",
        "?": "<Question Mark>",
        "!": "<Exclamation Point>",
        "+": "<Plus>",
        "-": "<Minus>",
        "/": "<Slash>",
        "*": "<Asterisk>",
        ";": "<Semicolon>",
        ":": "<Colon>",
        "<": "<Less Than>",
        ">": "<More Than>"
    }
    for letter in word:
        try:
            print(words[letter.lower()], end = ' ')
        except:
            print("<! Unknown character !>")
    print('')
    print('')
print('--------------------')
print('| WordSpeller v2.0 |')
print('--------------------')
print('')

while True:
    spellingAlphabetConverter(input('Input the word to spell out:'))