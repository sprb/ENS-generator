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



#make a statement for any number below 100 so it is 001 ex: $001

#does not work because the length is always less then or equal to 1000 or what ever the length is




#have leading zeros for all numbers below 100

#def length_choice():
#    choice = int(input("How many values would you like to generate? "))
#    if choice == 10:
#        return 10
#    if choice == 100:
#        return 100
#    if choice == 10000:
#        return 10000
#    else:
#        return 1000                  