class Dog:
    """
    A class representing a dog.
    """
    def __init__(self, name=None):
        """
        Initializes an instance of the Dog class.
        :param name: The name of the dog.
        """
        self.name = name

    def say(self):
        """
        Displays the sound made by the dog on the screen.
        """
        print('Гав!')

    def __str__(self):
        """
        method for string representation
        :return: string with dog's name
        """
        return f'Собака: {self.name}'

    def __repr__(self):
        """
        method for interactive presentation
        :return: string with dog's name
        """
        return self.__str__()


dog = Dog('Шарик')
dog.say()
