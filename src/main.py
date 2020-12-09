
import addition as a
import multiplication as m
import subtraction as s
import division as d

# Making Calls to ADDITION Methods
print("\n### : Making Calls to ADDITION Methods : ###")
print("Calling add Numbers :", a.add())
a.add()

print("Adding 2 Numbers (10, 20) :", a.add_2_numbers(10, 20))

# LAMBDA Function: To ADD given 2 Numbers


def fn_add(first_no, second_no): return first_no + second_no


print("Adding 2 Numbers using Lambda: 123, 234, fn_add :",
      a.adding_2_numbers_using_lambda(123, 234, fn_add))

print("Adding 3 Numbers (11, 22, 33) :", a.adding_3_numbers(11, 22, 33))

print("Adding 'n' Numbers (1, 2, 3, 4, 5, 6, 7, 8, 9, 10) :",
      a.adding_n_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

print("Adding Required No Of Numbers :", a.adding_required_numbers())

"""
# Making Calls to SUBTRACTION Methods
print("\n### : Making Calls to SUBTRACTION Methods : ###")

print("Subtract() : No Arguments passed as Input : ", s.subtract())

print("Subtract_2_numbers(15, 6) : ", s.subtracter(15, 6))

# LAMBDA Function: To SUBTRACT given 2 Numbers


def func_sub(first_no, second_no): return first_no - second_no


print("Subtracting_2_numbers_using_lambda(25, 22) : ",
      s.subtracting_2_numbers_using_lambda(25, 22, func_sub))
print("Subtracting_n_numbers(10, 15, 20, 25, 33) : ",
      s.subtracting_n_numbers(10, 15, 20, 25, 33))

# Making Calls to MULTIPLICATION Methods
print("\n### : Making Calls to MULTIPLICATION Methods : ###")

print("Multiply() : ", m.multiply())

print("Multiply_2_numbers(10, 25) : ",
      m.multiply_2_numbers(10, 25))

# LAMBDA Function: To MULTIPLY given 2 Numbers


def func_multiply(first_no, second_no): return first_no * second_no


print("Multiplying_2_numbers_using_lambda(10, 5, fn_lambda) :",
      m.multiplying_2_numbers_using_lambda(10, 5, func_multiply))

print("Multiplying_3_numbers(30, 40, 5) : ",
      m.multiplying_3_numbers(30, 40, 5))

print("Multiplying_n_numbers(2, 5, 10, 20) : ",
      m.multiplying_n_numbers(2, 5, 10, 20))

print("Multiply_required_numbers() : ",
      m.multiply_required_numbers())

# Making Calls to DIVISION Methods
print("\n### : Making Calls to DIVISION Methods : ###")

print(" divide() :", d.divide())

print(" divide_2_numbers(243, 13) : ", d.divide_2_numbers(243, 13))

# LAMBDA Function: To MULTIPLY given 2 Numbers


def fn_divide(first_no, second_no):
    return first_no/second_no if second_no != 0 else None

# print("divide_2_numbers_using_lambda(first_num: float, second_num: float, fn_divide: object) -> float:")


print("dividing_2_numbers_using_lambda(243, 13, fn_divide): ",
      d.dividing_2_numbers_using_lambda(243, 13, fn_divide))

"""
