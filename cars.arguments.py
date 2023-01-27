def make_car(name, year, producent, **car_info):
    """Build vocabluary with info about user."""
    profile = {}
    profile['name_car'] = name
    profile['producent_car'] = producent
    for key, value in car_info.items():
        profile[key] = value
    return profile

car = make_car('bmw', '2008', 'Germany',
               location='princeton',
               field='physics', hobby='books')
print(car)

car = make_car('honda', '2011', 'France',
               color='blue')
print(car)
