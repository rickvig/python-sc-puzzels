'''
Write a program that prints the numbers from 1 to 100.\
But for multiples of three print “Three” instead of the number and for the multiples of five print “Five”.\
For numbers which are multiples of both three and five print “ThreeFive”.
'''

def show_number(number_to_calculate):
    if number_to_calculate % 3 == 0 and number_to_calculate % 5 == 0:
        return 'TreeFive'
    elif number_to_calculate % 3 == 0:
        return 'Tree'
    elif number_to_calculate % 5 == 0:
        return 'Five'
    else:
        return str(number_to_calculate)

 
def list_numbers():
    return list(map(lambda number_to_calculate: show_number(number_to_calculate), range(1, 101)))