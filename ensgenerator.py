#ENS list generator

import numbers

with open('enslist.txt', 'w') as ens_list:
    ens_list.write('')

def ens_generator():

    prefix = str(input("What is the desired prefix? "))
    suffix = str(input("What is the desired suffix? "))
    num = int(input("What number would you like to begin the list? "))
    length = int(input("How many values would you like to generate? "))
    true_length = length + 1

    for i in range(length):
        value = prefix + str(num)
        print(value)
        with open('enslist.txt', 'a') as ens_list:
            ens_list.write("""
""" + value)
        num += 1

       
ens_generator()
