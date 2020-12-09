###################################################################
# AUTHORS NAME  : R.K.Rao Chigurupati
# CREATION DATE : 25-NOV-2020
# File Name     : subtraction.py
# DESCRIPTION   : To create subtraction() Methods for CALC
###################################################################

def subtract():
    """
    This function subtracts the Second Number from First One
    :return: Returns the Subtraction of Two Numbers supplied
    """
    first_num = int(input("Enter your First Number: "))
    second_num = int(input("Enter the Second Number: "))
    print(f"Result of SUBTRACTION : {first_num} - {second_num} = {first_num - second_num}")
    return first_num - second_num


def subtracter(first_num, second_num):
    """
    This function subtracts the Second No from the First Number
    :param first_num:
    :param second_num:
    :return: Returns the difference of First and Second Numbers
    """
    result = first_num - second_num
    print(f"SUBTRACT Result : {first_num} - {second_num} = {first_num - second_num}")
    return result


# LAMBDA Function: To SUBTRACT given 2 Numbers
# func_sub = lambda first_no, second_no: first_no - second_no
# NOTE: Passing Lambda Function as 3rd Argument to below function..

def subtracting_2_numbers_using_lambda(first_num, second_num, func_sub):
    """
    This function subtracts the given two numbers using Lambda or Anonymous Function
    :param first_num:
    :param second_num:
    :param func_sub:
    :return: Returns the SUBTRACTION Value of Second from the First Number
    """
    return func_sub(first_num, second_num)


def subtracting_n_numbers(*numbers):
    """
    This function accepts any 'n' number of arguments and
    subtracts the last item 'n' from all other n-1, n-2, n-3 ...
    :param numbers:
    :return: Returns by subtracting n' th item from all other items
    """
    index, result = 0, 0
    # print("First Number:", numbers[0])
    # print("Last Number :", numbers[len(numbers)-1])
    if len(numbers) > 1:
        if len(numbers) == 2:
            result = numbers[0] - numbers[1]
            return result
        else:
            index = 0
            for number in numbers:
                if index == (len(numbers) - 1):
                    result -= number
                else:
                    result += number
                index += 1
            return result
    else:
        if len(numbers) == 1:
            result = numbers[0]
            # result = numbers   # Simply we can write
            print(f"Single Number {result} supplied.. Hence returning the Same NO.!")
            return result
        else:
            return f"Nothing has Provided.. None!"
