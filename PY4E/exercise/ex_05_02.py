'''
5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters anything 
other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. 
Enter 7, 2, bob, 10, and 4 and match the output below.
'''

largest = 0
print(f"Antes do Loop: {largest}")

for i in [10, 20 ,24, 123, 2, 1, 233, 143, 123, 457, 555, 873, 937, 347, 748, 837, 834, 747, 958, 857, 846]:
    if i > largest:
        largest = i
print(f"Depois do Loop: {largest}")

