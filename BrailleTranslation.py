"""Braille is a writing system used to read by touch instead of sight. Each 
character is composed of six dots in a 2x3 grid, where each dot can either 
be a bump or be flat (no bump). Write a function answer(plaintext) that 
takes a string parameter and returns a string of 1's and 0's representing
the bumps and the absence of bumps in the input string. The function should
be able to encode the 26 lowercase letters, handle capitalization by adding
a Braille capitalization mark before that character, and use a blank character 
(000000) for spaces. String should be less than fifty characters long and 
contain only letters and spaces."""
# Written by Immanuel Kolapo Friday, 17th Feb 2017

# Needed letters and corresponding code
character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
             'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
charCode = ['100000', '110000', '100100', '100110', '100010', '110100',
            '110110', '110010', '010100', '010110', '101000', '111000',
            '101100', '101110', '101010', '111100', '111110', '111010',
            '011100', '011110', '101001', '111001', '010111', '101101',
            '101111', '101011', '000000']
capitalMark = "000001"

# The function
def answer(plaintext):
    if len(plaintext) < 49:
        for each_letter in plaintext:
            if each_letter == each_letter.upper():
                for each_character in character:
                    characterCap = each_character.upper()
                    if each_letter == characterCap:
                        for each_charCode in charCode:
                            if character.index(each_character) == charCode.index(each_charCode):
                                if each_letter == ' ':
                                    plaintext = plaintext.replace(each_letter, each_charCode)
                                else:
                                    each_charCode = capitalMark + each_charCode
                                    plaintext = plaintext.replace(each_letter, each_charCode)
            else:
                for each_character in character:
                    if each_letter == each_character:
                        for each_charCode in charCode:
                            if character.index(each_character) == charCode.index(each_charCode):
                                plaintext = plaintext.replace(each_letter, each_charCode)
        return plaintext
    else:
        plaintext = "String should be less than fifty characters long"
        return plaintext
# Supplied string
text = "The quick brown fox jumped over the lazy dog"
# Call to answer() function
print(answer(text))

# The test before writing the answer() function
# character = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
#              'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
# charCode = ['100000', '110000', '100100', '100110', '100010', '110100',
#             '110110', '110010', '010100', '010110', '101000', '111000',
#             '101100', '101110', '101010', '111100', '111110', '111010',
#             '011100', '011110', '101001', '111001', '010111', '101101',
#             '101111', '101011', '000000']
# capitalMark = "000001"
# text = "Written by C"
# if len(text) < 49:
#     for each_letter in text:
#         if each_letter == each_letter.upper():
#             for each_character in character:
#                 characterCap = each_character.upper()
#                 if each_letter == characterCap:
#                     for each_charCode in charCode:
#                         if character.index(each_character) == charCode.index(each_charCode):
#                             if each_letter == ' ':
#                                 text = text.replace(each_letter, each_charCode)
#                             else:
#                                 each_charCode = capitalMark + each_charCode
#                                 text = text.replace(each_letter, each_charCode)
#         else:
#             for each_character in character:
#                 if each_letter == each_character:
#                     for each_charCode in charCode:
#                         if character.index(each_character) == charCode.index(each_charCode):
#                             text = text.replace(each_letter, each_charCode)
#     print(text)
# else:
#     print("Strings should be less than fifty characters long")
