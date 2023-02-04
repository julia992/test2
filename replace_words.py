filename = 'learning_python.txt'
"""replace words in text file"""
with open(filename) as file_object:
    msg = file_object.read()
    
with open(filename) as file_object:   
    msg = msg.replace('Python', 'C')

print(msg)
