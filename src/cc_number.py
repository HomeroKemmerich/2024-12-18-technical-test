# Create a function that receives a credit card number as parameter
# and returns the last four numbers, with the other characters being represented 
# with '*'.
# Example: 
# input                 output
# 5867 1425 2356 8751   **** **** **** 8751

EXAMPLE_INPUT = '5867 1425 2356 8751'

CC_NUMBER_LENGTH = 16
CC_NUMBER_SPACES = 3

def secure_cc_number(cc_number: str):
    '''
    Unique numbers like credit card numbers should always be strings
    '''

    clear_cc_number = cc_number.replace(' ', '')

    if not clear_cc_number.isdigit():
        return 'Error: not a numeric value'

    if(len(clear_cc_number) < CC_NUMBER_LENGTH):
        return 'Erro: not a valid credit card number'
    
    secure_number = '**** ' * CC_NUMBER_SPACES + clear_cc_number[-4:]

    return secure_number

secure_number = secure_cc_number(EXAMPLE_INPUT)
print(secure_number)