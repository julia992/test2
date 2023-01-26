def show_magicians(magic_names, great_names):
    while magic_names:
        current_magic = magic_names.pop()

        print("Great " + current_magic.title())
        great_names.append(current_magic)

def make_great(great_names):
    print("\nGreat: ")
    for great_name in great_names:
        print(great_names)

magic_names = ['ann', 'sam']
magic_names = ['add', 'nick']
great_names = []

show_magicians(magic_names, great_names)
make_great(great_names)

def show_magicians(magic_names[:], great_names):
    print("Great ")

    



