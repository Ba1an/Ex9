import random
import time


class NotSleeping:
    '''
    Class for person that is not sleeping
    '''

    def __init__(self, name):
        '''
        method for initialization
        :param name: name of person
        '''
        self.name = name
        self.sheep = 0

    def add_sheep(self):
        '''
        Method for counting sheep.
        :return: nothing
        '''
        self.sheep += 1

    def lost(self):
        '''
        method for losing number of sheep
        :return: nothing
        '''
        self.sheep_count = 0

    def get_count_sheeps(self):
        '''
        method for getting count of sheep
        :return: count of sheep
        '''
        return self.sheep_count

    def __str__(self):
        '''
        method for string representation
        :return: string with person's name
        '''
        return f'Человек, пытающийся заснуть: {self.name}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with person's name
        '''
        return self.__str__()


sleeper = NotSleeping('Оля')
stop = random.randint(1, 10)
print(stop)
for i in range(1, 20):
    if i < stop:
        sleeper.lost()
        sleeper.add_sheep()
        time.sleep(1)
        print(sleeper.sheep, '...')
    else:
        sleeper.lost()
        print('сбился')
        break
