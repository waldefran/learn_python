'''
Exercise 1: Write a program to read through a file and print the contents of the file (line by line) all in 
upper case. Executing the program will look as follows:
'''

arq = open('mbox-short.txt')

for L in arq:
    L.rstrip()
    print(L.upper())
