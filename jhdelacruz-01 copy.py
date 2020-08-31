import string
import re

# Get all 95 ascii characters
def get_ascii():
    ascii_characters  = string.printable.strip()
    ascii_characters_list = list(ascii_characters)
    ascii_characters_list.append(' ')
    len(ascii_characters)
    len(ascii_characters_list)
    return ascii_characters_list

# Clean and split the input
def clean_me(user_input):
    user_input = user_input.replace('\t',' ')
    user_input = user_input.strip()
    user_input = re.sub('\s+'," ",user_input)
    user_input = user_input.split(" ")
    return user_input


if __name__ == '__main__':
    # All Valid Keyword List
    keyword_list = ['CREATE', 'GIVEYOU!', 'GIVEYOU!!', 'PLUS', 'MINUS', 'TIMES', 'DIVBY', 'MODU', 'RUPTURE']
    # Operator Symbols
    operator_symbols = {'PLUS': '+', 'MINUS': '-', 'TIMES': '*', 'DIVBY': '/', 'MODU': '%'}
    # Error Messages
    error_messages = {'SYNTAX_ERROR': "The syntax is incorrect", 'BEGIN_ERROR':'Input the BEGIN keyword to start.', 'INVALID_KW': 'is not a valid keyword.', 'INVALID_ASCII': ' is not a valid ASCII character.','INVALID_ASCIIS': ' are not valid ASCII characters.', 'INVALID_STRING': ' is not a valid string.',  'INVALID_INTEGER': ' is not a valid integer.'}
    # Successful Messages
    success_messages = {'WELCOME':'Welcome to INTERPOL syntax checker!', 'BEGIN_WARNING': 'Input CREATE to begin.','END_WARNING': 'Input RUPTURE to end.','BEGIN':'Beginning syntax checker', 'END':'Thank you for using syntax checker', 'SYNTAX_CORRECT': 'The syntax is correct.'}
    ascii_list = get_ascii()
    not_ascii = ""

    # Display welcome message
    print ("{0}\n{1} {2}".format(success_messages['WELCOME'], success_messages['BEGIN_WARNING'], success_messages['END_WARNING']))
    user_input = clean_me(input())

    # Check if CREATE keyword has been inputted
    while user_input[0] != "CREATE":
        print ("{0}".format(success_messages['BEGIN_WARNING']))
        user_input = clean_me(input())

    # Display begin message
    print ("{0} {1}".format(success_messages['SYNTAX_CORRECT'],success_messages['BEGIN']))

    # Check for invalid characters
    for word in user_input:
        word_list = list(word)
        for c in word_list:
            if not c in ascii_list:
                not_ascii += "{0} ".format(c)

    # Display syntax error message
    if not_ascii != "":
        print (error_messages['SYNTAX_ERROR'])
        if len(not_ascii) < 3:
            print ("{0} {1}".format(not_ascii, error_messages['INVALID_ASCII']))
        else:
            print ("{0} {1}".format(not_ascii, error_messages['INVALID_ASCIIS']))

    # Check if the expression is a comment
    if user_input[0][:1] == "#":
        # Proceed to exit program and check if syntax is correct
        print (success_messages['SYNTAX_CORRECT'])
