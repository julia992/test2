filename = 'learning_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()

    python_string = ''
    for line in lines:
        python_string += line.rstrip()

        print(python_string)
        print(len(python_string))
        
