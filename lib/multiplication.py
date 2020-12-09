###################################################################
# AUTHORS NAME  : R.K.Rao Chigurupati
# CREATION DATE : 25-NOV-2020
# File Name     : multiplication.py
# DESCRIPTION   : To create multiplication() Methods for CALC
###################################################################

def multiply():
    """
    This function multiplies the User Input Numbers
    :return: Returns the product of numbers
    """
    first_no = int(input("Enter the First Number : "))
    second_no = int(input("Enter the Second Number : "))
    result = first_no * second_no
    print(f"Result of MULTIPLICATION : {first_no} * {second_no} = {result}")
    return result


def multiply_2_numbers(first_num, second_num):
    """
    This function multiplies the given two numbers
    :param first_num:
    :param second_num:
    :return: Returns the product of 2 numbers as result
    """
    result_2_nums = first_num * second_num
    return result_2_nums


# LAMBDA Function: To MULTIPLY given 2 Numbers
# func_multiply = lambda first_no, second_no: first_no * second_no
# NOTE: Passing Lambda Function as 3rd Argument to below function..


def multiplying_2_numbers_using_lambda(first_num, second_num, func_multiply):
    """
    This function subtracts the given two numbers using Lambda or Anonymous Function
    :param first_num:
    :param second_num:
    :param func_multiply:
    :return: Returns the SUBTRACTION Value of Second from the First Number
    """
    return func_multiply(first_num, second_num)


def multiplying_3_numbers(first_num, second_num, third_num):
    """
    This function multiplies the given three numbers
    :param first_num:
    :param second_num:
    :param third_num:
    :return: Returns the product of 3 numbers as result
    """
    result_3_nums = first_num * second_num * third_num
    return result_3_nums


def multiplying_n_numbers(*numbers):
    """
    This functions multiplies the given n number of numbers
    :param numbers:
    :return: Returns the product of n numbers as result
    """
    result = 1
    # print("First Number:", numbers[0])
    # print("Last Number :", numbers[len(numbers)-1])
    if len(numbers) > 1:
        if len(numbers) == 2:
            result = numbers[0] * numbers[len(numbers)-1]
            return result
        else:
            for number in numbers:
                result *= number
            return result
    else:
        if len(numbers) == 1:
            result = numbers
            print(
                f"Single Number {result} supplied.. Hence returning the Same NO.!")
            return result
        else:
            return f"Nothing has Provided.. None!"


def multiply_required_numbers():
    """
    This function is to Multiply the Required Numbers based on User Choice
    :return: Returns the Product of Multiplying ALL the Numbers given by User
    """
    result_prod = 1
    how_many_numbers = int(
        input("How many Numbers Do you want to Multiply.? "))
    for number in range(how_many_numbers):
        result_prod *= int(input("Enter the Number-" +
                                 str(number + 1) + " : "))
    return result_prod
