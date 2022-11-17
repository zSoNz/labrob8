from factorial import *
from mul import *
from Sum import *
from div import *

first_num = int(input('Enter first number:'))
sec_num = int(input('Enter second number:'))
oper = input('Enter operation:')

match oper:
    case "!":
        result = fact(first_num)
    case "+":
        result = sum(first_num, sec_num)
    case "*":
        result = mul(first_num, sec_num)
    case "/":
        result = div(first_num, sec_num)
    case _:
        result = "такого нема"
        
print(result)