class Restaurant():
    def __init__(self, restaurant_name, cuisine_type):
        """initializes restaurant attribures."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Restaurant description."""
        print(self.restaurant_name.title() + " is super !")
        print(self.cuisine_type.title() + " is better.")
        
    def open_restaurant(self):
        """Restaurant is open."""
        print(self.restaurant_name.title() + " is open !")

restaurant_1 = Restaurant('tokio', 'japan')
"""Ask to attribuite"""
print(restaurant_1.restaurant_name)

"""Ask to method"""
restaurant_1.describe_restaurant()
restaurant_1.open_restaurant()
