class TrafficLight:
    '''
    Class for traffic lights
    '''
    permissible_values = ['зеленый', 'желтый', 'красный', 'желтый']

    def __init__(self):
        '''
        Initializes an instance of the Traffic Light class.
        Sets the initial value of the current traffic light signal to green and the index to 0.
        '''
        self.current_signal = 'зеленый'
        self.ind = 0

    def next_signal(self):
        '''
        Switches the current traffic light signal to the next one.
        When the last signal in the list is reached, it switches to the first signal.
        :return: nothing
        '''
        self.ind += 1
        if self.ind >= 4:
            self.ind = self.ind - 4
        self.current_signal = self.permissible_values[self.ind]

    def __str__(self):
        '''
        Returns a string representation of a point.
        :return: string with current colour
        '''
        return f'Текущий цвет: {self.current_signal}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with teams' info
        '''
        return self.__str__()


traffic_light = TrafficLight()
print(traffic_light.current_signal)

for _ in range(10):
    traffic_light.next_signal()
    print(traffic_light.current_signal)
