#!/usr/bin/python3

# in python we use camelCase name 
class Square():
    """Square class"""
    
    def __init__(self, width=0, height=0):
        # dont use Kwargs keep it simple like that 
        self.width = width
        self.height = height

    def area_of_my_square(self):
        """ Area of the square """
        return self.width * self.width

    # in python methods we use snake_case 
    def permiter_of_my_Square(self):
        # in math we use P =  2 * (width + height)
        return 2 * (self.width + self.height)

    def __str__(self):
        # str is a magic method give you information about your object.
        return f"Square - Width: {self.width}, Height: {self.height}"

if __name__ == "__main__":

    # i change name of your class
    s = Square(width=12, height=9)
    print(s)
    print(s.area_of_my_square())
    print(s.PermiterOfMySquare())
