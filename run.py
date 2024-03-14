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
    Checks if the user wishes to end to program or not.
    Performs validation on the user input.
    """
    ok_to_finish = True
    user_input_accepted = False
    
    while not user_input_accepted:
        user_input = input('Are you finished using the calculator? (y/n): ')
        if user_input == 'y':
            user_input_accepted = True
        elif user_input == 'n':
            ok_to_finish = False
        else:
            print('Response must be (y/n), please try again.')
            
    return ok_to_finish


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


finished = False

while not finished:
    result = 0
    menu_choice = get_operation_choice()
    # get the numbers from user
    # select the operation
    print('Result', result)
    print('====================')
    finished = check_if_user_is_finished()
    
print('Bye')