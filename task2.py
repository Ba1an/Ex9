class NotSleeping:
    '''
    A class representing a person who cannot sleep.
    '''
    def __init__(self, name=None):
        '''
        method for initialization
        :param name: The name of the person
        '''
        self.name = name
        self.sheeps = 0

    def add_sheeps(self):
        '''
        Method for counting sheep.
        :return: nothing
        '''
        self.sheeps += 1

    def __str__(self):
        '''
        method for string representation
        :return: string with person's name
        '''
        return f'Человек: пытающий{self.name}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with person's name
        '''
        return self.__str__()


sleeper = NotSleeping('Оля')
for i in range(14):
    sleeper.add_sheeps()
    print(sleeper.sheeps, '...')
