from art import logo
print(logo)

# calculating methods
def calculating(f_num, l_num, operation):
    """Return a result for a specific operation"""
    if operation == "+":
        result = f_num + l_num
    elif operation == "-":
        result = f_num - l_num
    elif operation == "*":
        result = f_num * l_num
    else:
        result = f_num / l_num
    return result

def Print_operations(operation_ls):
    for x in operation_ls:
        print(x)

# checking if operation out of the list of operations
def check_operation(operations):
    """print an error if user enter a wrong operation"""
    if operations not in ls_operation:
        error_operate = True
        while error_operate:
            print("Error, Please pick an operation from this list")
            Print_operations(ls_operation)
            global operation
            operations = input("Pick an operation: ")

            if operations not in ls_operation:
                continue
            else:
                operation = operations
                error_operate = False

def check_number():
    num_type = True
    while num_type:
        try:
            number = float(input("Enter a number: "))
            num_type = False
            return number
        except:
            print("please inter a number not strings")
            continue

ls_operation = ['+', '-', '*', '/']

f_num = check_number()

again = True
while again:
    # checking operations
    Print_operations(ls_operation)
    operation = input("Pick an operation: ").strip()
    check_operation(operations= operation)

    l_num = check_number()

    result = round(calculating(f_num, l_num, operation), 2)
    print(f"{f_num} {operation} {l_num} = {result}")

    continue_calculating = input(f"Type 'y' to continue calculating with {result}, type 'n' to start a new calculation or 'q' to quit: ").lower().strip()

    if continue_calculating == 'y':
        f_num = result
        continue
    elif continue_calculating == 'n':
        try:
            f_num = float(input("What's the first number?: "))
        except:
            print("Invalid input, Please Enter numbers.")
            quit()
        continue
    else:
        again = False
