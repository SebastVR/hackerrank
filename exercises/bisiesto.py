""" Task
Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return 
False.
Note that the code stub provided reads from STDIN and passes arguments to the is_leap function. It is only necessary 
to complete the is_leap function.
 """

year = int(input("Add a leap year: "))

if year % 4 != 0:  # no divisible entre 4
    print(False)
elif year % 4 == 0 and year % 100 != 0:  # divisible entre 4 y no entre 100 o 400
    print(True)
elif (
    year % 4 == 0 and year % 100 == 0 and year % 400 != 0
):  # divisible entre 4 y 100 y no entre 400
    print(False)
elif (
    year % 4 == 0 and year % 100 == 0 and year % 400 == 0
):  # divisible entre 4, 100 y 400
    print(True)
