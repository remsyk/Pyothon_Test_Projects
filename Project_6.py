# DEFINITIONS


def get_name():
    print("Please enter a name (if it contains a '#', an error message will appear: ")
    name_input = input()
    if name_input.find('#') > -1:
        #<your code here>
        raise ValueError('Error: Cannot Have #')


# EXECUTION

try:
    get_name()
except Exception as error:
    print('We Have An Error: ' + repr(error))