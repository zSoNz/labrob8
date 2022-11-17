def fact(first_number):
    if first_number==1:
        return 1
    else:
        return (first_number * fact(first_number-1))