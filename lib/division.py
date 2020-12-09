###################################################################
# AUTHORS NAME  : R.K.Rao Chigurupati
# CREATION DATE : 25-NOV-2020
# File Name     : division.py
# DESCRIPTION   : To create division() Methods for CALC
###################################################################

def divide():
    """
    This function divides the First Number by Second Number
    :return: Returns the resulting value after Division operation
    i.e. The Result Value is Rounded up to 5 Decimal Places
    """
    first_num = float(input("Enter the First Value : "))
    second_num = float(input("Enter the Second Value : "))
    while True:
        if second_num == 0:
            print(f"Division with Zero is NOT possible..!")
            second_num = float(input("Enter another value for Second NO: "))
        else:
            break
    result_div = first_num / second_num
    print(
        f"DIVISION of {first_num}/{second_num} is : {first_num/second_num:0.5f}")
    return round(result_div, 5)


def divide_2_numbers(first_num: float, second_num: float) -> float:
    """
    This function divides the First Number by Second Number
    :param:
    :param:
    :return: Returns the result of division
    i.e. First Number over Second Number and Rounded till 3 Decimal Places
    """
    result_div = first_num / second_num
    print(
        f"Result of Division : {first_num}/{second_num} = {result_div:0.3f} ")
    return round(result_div, 3)


# LAMBDA Function: To MULTIPLY given 2 Numbers
# func_divide = lambda first_no, second_no: first_no / second_no if second_no != 0 else None
# NOTE: Passing Lambda Function as 3rd Argument to below function..

def dividing_2_numbers_using_lambda(first_num: float, second_num: float, fn_divide: object) -> float:
    """
    This is to divide 2 numbers by using the Lambda Function
    :param first_num:
    :param second_num:
    :param fn_divide:
    :return: Returns the result of division by passing numbers to lambda function
    """
    return fn_divide(first_num, second_num)
