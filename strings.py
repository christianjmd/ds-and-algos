"""
decode function:
 - takes an encoded message as a string and returns the decoded message.
 - input: a string "string" and positive int n.
 - output: decoded string. string decoded by discarding the first n characters
            from input string, keeping next n characters, discarding next n
            characters and so on, until input string is exhausted.
 - example: decode(`#P#y#t#h#o#n#', 1) returns `Python'.
"""
def decode(string, n):
    output = ""
    i = 0

    while i <= len(string):

        if (i == n) or (i != 0 and i % n == 0):
            output += string[i: i + n]
            i = i + (n + 1)

        else:
            i = i + 1

    return output

"""
decode function:
 - counts how many times a pattern occurs within a text.
 - examples: pattern_count('aaaa', 'aa') returns 2
             pattern_count(`If you must blink, do it now.', `code') returns 0.
"""

def pattern_count(string, pat):

    counter = 0

    for i in range(len(string)):

        if string[i] is pat[0]:
            if string[i:i + len(pat)] == pat:
                counter += 1
                i + len(pat)                        # skip the following elements after checking.

    return counter

"""
palindrome function checks whether a word, phrase, or sequence reads the same
backwards and forwards.
"""

def palindrome(string):

    new_string = ""

    for i in range(len(string)):

        if string[i].isalpha() or string[i].isnumeric():
            new_string += string[i].lower()

    if list(new_string) == list(reversed(new_string)):
        return True
    else:
        return False
