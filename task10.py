class Point:
    '''
    A class representing a point on the plane.
    '''
    def __init__(self, tup=(0,0)):
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
        return ((self.get_x() - other.get_x())**2 + (self.get_y() - other.get_y())**2)**0.5

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

class Segment:
    '''
    Class of segments
    '''
    def __init__(self, point1, point2, one_intersection):
        '''
        method for initialization
        :param point1:first point
        :param point2: second point
        :param one_intersection: nothing
        '''
        self.point1 = point1
        self.point2 = point2
        self.one_intersection = one_intersection


class CoordinateSystem:
    '''
    Class of coordinate systems
    '''
    def __init__(self):
        '''
        method for initialization
        '''
        self.segments = []

    def add_segment(self, segment):
        '''
        method for adding segment
        :param segment: segment
        :return: nothing
        '''
        self.segments.append(segment)

    def axis_intersection(self):
        '''
        method for getting amount of segments with only one intersection
        :return: count
        '''
        count = 0
        for segment in self.segments:
            if segment.one_intersection:
                count += 1
        return count

    def __str__(self):
        '''
        method for string representation
        :return: string with coordinate system's info
        '''
        return f'Плоскость, имеющая отрезки: {self.segments}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with coordinate system's info
        '''
        return self.__str__()

point1 = Point((1, 2))
point2 = Point((2, 3))
s1 = Segment(point1,point2, False)
point3 = Point((0, 3))
point4 = Point((-1, 2))
s2 = Segment(point3,point4,True)
c = CoordinateSystem()
c.add_segment(s1)
c.add_segment(s2)
print(c.axis_intersection())

