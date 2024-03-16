def add(x,y):
    return x + y

def subtract(x,y):
    return x - y

def multiply(x,y):
    return x * y

def divide(x,y):
    return x / y


def check_if_user_is_finished():
    """
    Checks if the user wishes to end the program or not.
    Performs validation on the user input.
    """
    while True:
        user_input = input('Are you finished using the calculator? (y/n): ')
        if user_input.lower() == 'y':
            return True  # User wants to finish, so we stop.
        elif user_input.lower() == 'n':
            return False  # User wants to continue, so we don't stop.
        else:
            print('Response must be (y/n), please try again.')


def get_operation_choice():
    input_ok = False
    while not input_ok:
        print('Menu options are:')
        print('\t1. Add')
        print('\t2. Subtract')
        print('\t3. Multiply')
        print('\t4. Divide')
        print('------------------')
        user_selection = input('Please make a selection: ')
        if user_selection in ('1', '2', '3', '4'):
            input_ok = True
        else:
            print('Invalid Input (Musr be 1 - 4)')
    print('------------------')
    return user_selection


def get_numbers_from_user():
    num1 = get_integer_input('Input the first number: ')
    num2 = get_integer_input('Input the second number: ')
    return num1, num2


def get_integer_input(message):
    value_as_string = input(message)
    while not value_as_string.isnumeric():
        print('The input must be an integer')
        value_as_string = input(message)
    return int(value_as_string)


finished = False

while not finished:
    result = 0
    menu_choice = get_operation_choice()
    n1, n2 = get_numbers_from_user()
    if menu_choice == '1':
        result = add(n1, n2)
    elif menu_choice == '2':
        result = subtract(n1, n2)
    elif menu_choice == '3':
        result = multiply(n1, n2)
    elif menu_choice == '4':
        result = divide(n1, n2)
    print('Result:', result)
    print('====================')
    finished = check_if_user_is_finished()
    
print('Good-Bye for now.')
