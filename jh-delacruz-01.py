import string
import re


def get_ascii():
    # Get all 95 ascii characters
    ascii_characters = string.printable.strip()
    ascii_characters_list = list(ascii_characters)
    ascii_characters_list.append(' ')
    len(ascii_characters)
    len(ascii_characters_list)
    return ascii_characters_list


def clean_me(user_inp):
    # Clean and return the input
    user_inp = user_inp.replace('\t', ' ')
    user_inp = user_inp.strip()
    user_inp = re.sub('\s+', " ", user_inp)
    return user_inp


def check_invalid_chars(user_inp):
    # Check for invalid characters
    # Get ascii list
    ascii_list = get_ascii()
    not_ascii = ""
    msg = ""

    for word in user_inp:
        word_list = list(word)
        for c in word_list:
            if not c in ascii_list:
                not_ascii += "{0} ".format(c)

    # Return syntax error message
    if not_ascii != "":
        msg = "{0}\n".format(error_messages['SYNTAX_ERROR'])
        if len(not_ascii) < 3:
            msg += "The {0}{1}".format(not_ascii, error_messages['INVALID_ASCII'])
        else:
            msg += "The {0}{1}".format(not_ascii, error_messages['INVALID_ASCIIS'])
    return msg


if __name__ == '__main__':
    # Main program
    # All valid keyword list
    keyword_list = ['GIVEYOU!', 'GIVEYOU!!', 'PLUS', 'MINUS', 'TIMES', 'DIVBY', 'MODU']
    # Print keywords
    print_keywords = ['GIVEYOU!', 'GIVEYOU!!']
    # Operator keywords
    operator_keywords = ['PLUS', 'MINUS', 'TIMES', 'DIVBY', 'MODU']
    # Error messages
    error_messages = {'SYNTAX_ERROR': "The syntax is incorrect.", 'BEGIN_ERROR': 'Input the BEGIN keyword to start.',
                      'INVALID_KW': 'is not a valid keyword.', 'INVALID_ASCII': 'is not a valid ASCII character.',
                      'INVALID_ASCIIS': 'are not valid ASCII characters.', 
                      'INVALID_STRING': 'The argument is not a valid string.',
                      'INVALID_INTEGER': 'The argument(s) is not a valid integer.', 'INT_ARG_ERROR':' needs 2 arguments.', 
                      'STR_ARG_ERROR':'The argument needs to be enclosed in quotation marks.',
                      'DQUOTE_ERROR':'The quote(s) needs to be escaped with a backslash.'}
    # Successful messages
    success_messages = {'WELCOME': 'Welcome to INTERPOL syntax checker!', 'BEGIN_WARNING': 'Input CREATE to begin.',
                        'END_WARNING': 'Input RUPTURE to end.', 'BEGIN': 'Beginning syntax checker...',
                        'BEGIN_INPUT': 'Input syntax to check.', 'END': 'Thank you for using syntax checker.',
                        'SYNTAX_CORRECT': 'The syntax is correct.'}
    try: 
        # Display welcome message
        print("{0}\n{1} {2}".format(success_messages['WELCOME'], success_messages['BEGIN_WARNING'],
                                    success_messages['END_WARNING']))
        user_input = clean_me(input('$ '))
    
        # Check if CREATE keyword has been inputted
        while user_input != "CREATE":
            print("{0}".format(success_messages['BEGIN_WARNING']))
            user_input = clean_me(input('$ '))
    
        # Display begin message if passed the above loop
        print("{0} {1}\n{2}".format(success_messages['SYNTAX_CORRECT'], success_messages['BEGIN'],
                                    success_messages['BEGIN_INPUT']))
        user_input = clean_me(input('$ '))
        user_input_list = user_input.split(" ")
    
        # Check if RUPTURE keyword has been inputted
        while user_input != "RUPTURE":
            
            # Check for invalid characters
            error_msg = check_invalid_chars(user_input_list)
            if error_msg != "":
                print(error_msg)
            else:
                # Check if the expression is a comment
                if user_input_list[0][:1] == "#" or user_input_list[0] == "CREATE":
                    print(success_messages['SYNTAX_CORRECT'])
                
                # Check if the expression has a valid keyword
                elif user_input_list[0] in keyword_list:
                    
                    # Check if the expression is an operation
                    if user_input_list[0] in operator_keywords:
                        if len(user_input_list) == 3:
                            try:
                                input_1 = int(user_input_list[1])
                                input_2 = int(user_input_list[2])
                                print(success_messages['SYNTAX_CORRECT'])
                            except ValueError:
                                print("{0}\n{1}".format(error_messages['SYNTAX_ERROR'],error_messages['INVALID_INTEGER']))
                        else:
                            print(error_messages['SYNTAX_ERROR'])
                            print("{0}{1}".format(user_input_list[0],(error_messages['INT_ARG_ERROR'])))
                
                    # Check if the expression is a print
                    elif user_input_list[0] in print_keywords and len(user_input_list) > 1: 
                        
                        # Split the KW and argument
                        kw_len = len(user_input_list[0]) + 1
                        arguments = user_input[kw_len:]
                        word = arguments[1:-1]
                        doubleq_err_count = 0
    
                        # Check if the argument has " in the beginning and end
                        if arguments[0:1] == '"' and arguments[-1] == '"':  
                            # Check if string has double quotes
                            if '"' not in word:
                                print(success_messages['SYNTAX_CORRECT'])
                            else:
                                # Check if it has unescaped double quotes inside
                                for match in re.finditer('"', word):
                                    s = int(match.start())
                                    e = int(match.end())
                                    escape_char = word[s-1:e-1]
                                    
                                    # Find if it has \ before the "
                                    if s == 0:
                                        doubleq_err_count += 1
                                    elif escape_char != "\\":
                                        doubleq_err_count += 1
                                    else:
                                        continue
                                # If argument is with or without unescaped double quotes
                                if doubleq_err_count == 0:
                                    print(success_messages['SYNTAX_CORRECT'])
                                else:
                                    print("{0}\n{1}".format(error_messages['SYNTAX_ERROR'],error_messages['DQUOTE_ERROR']))
                        else:
                            print("{0}\n{1}".format(error_messages['SYNTAX_ERROR'],error_messages['STR_ARG_ERROR']))
                    else:
                        print(error_messages['SYNTAX_ERROR'])
               
                # Catch all
                else:
                    print("{0}\n{1} {2}".format(error_messages['SYNTAX_ERROR'],user_input_list[0],error_messages['INVALID_KW']))
                
            user_input = clean_me(input('$ '))
            user_input_list = user_input.split(" ")
                    
        # Proceed to exit program
        print("{0}".format(success_messages['END']))
    except:
        # Proceed to exit program
        print("\n{0}".format(success_messages['END']))
