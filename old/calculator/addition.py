###################################################################
# AUTHORS NAME  : R.K.Rao Chigurupati
# CREATION DATE : 25-NOV-2020
# File Name     : adder.py
# DESCRIPTION   : To create addition() Methods for CALC
###################################################################

def add():
    """
    This function is to add any given two numbers
    :return: Returns the ADDITION of Two Numbers supplied
    """
    first_num = int(input("Enter the First Number: "))
    second_num = int(input("Enter another Second Number: "))
    print(f"Result of ADDITION : {first_num} + {second_num} = {first_num + second_num}")
    return first_num + second_num


def add_2_numbers(first_no, second_no):
    """
    This function is to add given two numbers
    :param first_no:
    :param second_no:
    :return: Returns the SUM of Two Numbers
    """
    sum_of_2_numbers = first_no + second_no
    return sum_of_2_numbers


# LAMBDA Function: To ADD given 2 Numbers
# func_lambda = lambda first_no, second_no: first_no + second_no
# NOTE: Passing Lambda Function as 3rd Argument to below function..

def adding_2_numbers_using_lambda(first_num, second_num, fn_add):
    """
    This function adds the given two numbers using Lambda Function or Anonymous Function
    :param first_num:
    :param second_num:
    :param fn_add: Using fn_add Function to make the Addition Task by passing Numbers
    :return: Returns the SUM of the Two Numbers
    """
    return fn_add(first_num, second_num)


def add_3_numbers(first_no, second_no, third_no):
    """
    This function is to add given three numbers
    :param first_no:
    :param second_no:
    :param third_no:
    :return: Returns the SUM of Three Numbers
    """
    sum_of_3_numbers = first_no + second_no + third_no
    return sum_of_3_numbers


def adding_n_numbers(*numbers):
    """
    This function adds whatever the 'n' number of Numbers
    :param numbers: Numbers supplied as arguments
    :return: Returns the SUM of ALL the Number's supplied
    """
    sum_of_n_numbers = 0
    # print("First Number:", numbers[0])
    # print("Last Number :", numbers[len(numbers)-1])
    if len(numbers) > 1:
        if len(numbers) == 2:
            sum_of_n_numbers = numbers[0] + numbers[1]
            return sum_of_n_numbers
        else:
            for num in numbers:
                sum_of_n_numbers += num
            return sum_of_n_numbers
    else:
        if len(numbers) == 1:
            result = numbers[0]
            # result = numbers   # Simply we can write
            print(f"Single Number {sum_of_n_numbers} supplied.. Hence returning the Same NO.!")
            return sum_of_n_numbers
        else:
            return f"Nothing has Provided.. None!"


def adding_required_numbers():
    """
    This function can add required Number of Number's
    :return: Returns the SUM of required Number of Number's
    """
    how_many_numbers = int(input("How many Numbers do you want to ADD.? "))
    counter, result_sum = 0, 0
    while counter < how_many_numbers:
        result_sum += int(input("Enter the Number-" + str(counter + 1) + " : "))
        counter += 1
    return result_sum
