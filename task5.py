class Game:
    '''
    The class representing the game.
    '''
    def __init__(self, score):
        '''
        Initializes an instance of the Game class.
        :param score: A dictionary containing the initial number of points for each team.
        '''
        self.score = score
        return

    def ball_thrown(self, command, points):
        '''
        Processing the ball throw.
        :param command: The team that scored the ball.
        :param points:The number of points.
        :return: nothing
        '''
        self.score[command] += points
        return

    def get_score(self):
        '''
        Getting the current account of the game.
        :return: A tuple with the number of points of each team.
        '''
        return tuple([self.score['command1'], self.score['command2']])

    def get_winner(self):
        '''
        Determining the winner of the game.
        :return: Game summary
        '''
        if self.score['command1'] > self.score['command2']:
            return 'command1'
        elif self.score['command1'] < self.score['command2']:
            return 'command2'
        else:
            return 'Ничья'

    def __str__(self):
        '''
        Returns a string representation of a point.
        :return: String representation of the point.
        '''
        return f'Координаты объекта:{self.t}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with teams' info
        '''
        return self.__str__()

game1 = Game({'command1': 0,  'command2': 0})
game1.ball_thrown('command1', 1)
game1.get_score()
game1.ball_thrown('command2', 1)
print(game1.get_winner())

