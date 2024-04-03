class Point:
    '''
    A class representing a point on the plane.
    '''

    def __init__(self, tup=(0, 0)):
        '''
        Initializes an instance of the Point class.
        :param tup: Tuple with point coordinates (x, y). By default (0, 0).
        '''
        self.tup = tup

    def get_x(self):
        '''
        Gets the y coordinate of the point.
        :return: X coordinate.
        '''
        return self.tup[0]

    def get_y(self):
        '''
        Gets the y coordinate of the point.
        :return: Y coordinate.
        '''
        return self.tup[1]

    def distance(self, other):
        '''
        Calculates the distance between the current point and another point.
        :param other: Another point.
        :return: The distance between the points.
        '''
        return ((self.get_x() - other.get_x()) ** 2 + (self.get_y() - other.get_y()) ** 2) ** 0.5

    def sum(self, other):
        '''
        Calculates the sum of the coordinates of the current point with the coordinates of another point.
        :param other: Another point.
        :return: A new point containing the sum of coordinates.
        '''
        return Point((self.get_x() + other.get_x(), self.get_y() + other.get_y()))

    def __str__(self):
        '''
        Returns a string representation of a point.
        :return: String representation of the point.
        '''
        return f'Координаты объекта:{self.tup}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with teams' info
        '''
        return self.__str__()


first = Point((2, 4))
second = Point()
print(first.distance(second))
third = first.sum(second)
print(first.sum(second))
