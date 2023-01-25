def make_shirt(size, text='dog'):
    print("\nI want  " + size + ".")
    print("I love " + text + "!")

make_shirt(size='L')
make_shirt('S')
make_shirt(size='M', text='cat')
    
def city_country(city, country):
    full_name = city + ' ' + country
    return full_name.title()
location = city_country('poznan' , 'ploand')
print(location)

location = city_country('ny', 'usa')
print(location)

def make_album(name , album, age=''):
   full_name = {'first': name, 'second': album}
   if age:
       full_name['age'] = age
   return full_name

music = make_album('sting', 'rose', age=48)
print(music)

music =make_album('sia', 'sea', age=54)
print(music)

