""" Task
Given an integer, n, perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive 2 range 5 of  to , print Not Weird
If  is even and in the inclusive 6 range of 20  to , print Weird
If  is even and greater than 20, print Not Weird """


n = int(input("Write a number "))

if n % 2 == 0 and 2 <= n <= 5:
    print("Not Weird")
elif n % 2 == 0 and 6 <= n <= 20:
    print("Wierd")
elif n > 20:
    print("Not Wierd")
else:
    print("Not Wierd")
