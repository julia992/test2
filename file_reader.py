file_path = 'Users\Lenovo\Dekstop\python\pi_digits.txt'
filename = 'pi_digits.txt'

with open('pi_digits.txt') as file_object:
    lines = file_object.readlines()

    pi_string = ''
    for line in lines:
        pi_string += line.rstrip()
        
    print(pi_string)
    print(len(pi_string))
