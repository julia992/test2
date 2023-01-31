class Restaurant():
    """Simple restaurant"""
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def get_descriptive_name(self):
        """Return description"""
        long_name = str(self.year) + ' ' + self.name
        return long_name.title()

my_restaurant = Restaurant('tokio', 2018)
print(my_restaurant.get_descriptive_name())

