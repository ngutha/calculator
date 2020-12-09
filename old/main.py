from Calculator_Project.calculator import addition
from Calculator_Project.calculator import subtraction
from Calculator_Project.calculator import multiplication
from Calculator_Project.calculator import division

# Making Calls to ADDITION Methods
print("\n### : Making Calls to ADDITION Methods : ###")
print("Calling add Numbers :", addition.add())
print("Adding 2 Numbers (10, 20) :", addition.add_2_numbers(10, 20))

# LAMBDA Function: To ADD given 2 Numbers
fn_add = lambda first_no, second_no: first_no + second_no
print("Adding 2 Numbers using Lambda: 123, 234, fn_add :", addition.adding_2_numbers_using_lambda(123, 234, fn_add))

print("Adding 3 Numbers (11, 22, 33) :", addition.add_3_numbers(11, 22, 33))
print("Adding 'n' Numbers (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) :", addition.adding_n_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print("Adding Required No Of Numbers :", addition.adding_required_numbers())


# Making Calls to SUBTRACTION Methods
print("\n### : Making Calls to SUBTRACTION Methods : ###")
print("Subtract() : No Arguments passed as Input : ", subtraction.subtract())
print("Subtracter(15, 6) : ", subtraction.subtracter(15, 6))

# LAMBDA Function: To SUBTRACT given 2 Numbers
func_sub = lambda first_no, second_no: first_no - second_no
print("Subtracting_2_numbers_using_lambda(25, 22) : ", subtraction.subtracting_2_numbers_using_lambda(25, 22, func_sub))
print("Subtracting_n_numbers(10, 15, 20, 25, 33) : ", subtraction.subtracting_n_numbers(10, 15, 20, 25, 33))

# Making Calls to MULTIPLICATION Methods
print("\n### : Making Calls to MULTIPLICATION Methods : ###")
print("Multiply() : ", multiplication.multiply())
print("Multiplying_2_numbers(10, 25) : ", multiplication.multiplying_2_numbers(10, 25))

# LAMBDA Function: To MULTIPLY given 2 Numbers
func_multiply = lambda first_no, second_no: first_no * second_no
print("Multiplying_2_numbers_using_lambda(10, 5, fn_lambda) :",
      multiplication.multiplying_2_numbers_using_lambda(10, 5, func_multiply))

print("Multiplying_3_numbers(30, 40, 5) : ", multiplication.multiplying_3_numbers(30, 40, 5))
print("Multiplying_n_numbers(2, 5, 10, 20) : ", multiplication.multiplying_n_numbers(2, 5, 10, 20))
print("Multiply_required_numbers() : ", multiplication.multiply_required_numbers())

# Making Calls to DIVISION Methods
print("\n### : Making Calls to DIVISION Methods : ###")
print(" divide() :", division.divide())
print(" divide_2_numbers(243, 13) : ", division.divide_2_numbers(243, 13))

# LAMBDA Function: To MULTIPLY given 2 Numbers
fn_divide = lambda first_no, second_no: first_no / second_no if second_no != 0 else None
# print("divide_2_numbers_using_lambda(first_num: float, second_num: float, fn_divide: object) -> float:")

print("divide_2_numbers_using_lambda(243, 13, fn_divide): ", division.divide_2_numbers_using_lambda(243, 13, fn_divide))
