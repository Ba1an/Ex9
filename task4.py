class User:
    '''
    Class of users.
    '''
    def __init__(self, id, nick_name, first_name, last_name=None, middle_name=None, gender=None):
        '''
        method for initialization
        :param id: person's id
        :param nick_name: person's nickname
        :param first_name: person's first name
        :param last_name: person's last name
        :param middle_name: person's middle name
        :param gender: person's gender
        '''
        self.id = id
        self.nick_name = nick_name
        self.first_name = first_name
        self.last_name = last_name
        self.middle_name = middle_name
        self.gender = gender

    def update(self):
        '''
        method for updating data
        :return: nothing
        '''
        flag = 0
        while flag == 0:
            try:
                par = input('Какой параметр вы хотите изменить?: ')
                new = input('Введите новое значение: ')

                if par == 'id':
                    self.id = new
                elif par == 'nick_name':
                    self.nick_name = new
                elif par == 'first_name':
                    self.first_name = new
                elif par == 'last_name':
                    self.last_name = new
                elif par == 'middle_name':
                    self.middle_name = new
                else:
                    self.gender = new
                flag = 1
            except:
                print('Ошибка! Попробуйте ещё раз')

    def __str__(self):
        """
        method for string representation
        :return: string with person's info
        """
        return (f"User(id={self.id}, nick_name='{self.nick_name}', first_name='{self.first_name}', "
                f"last_name='{self.last_name}', middle_name='{self.middle_name}', gender='{self.gender}')")

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with person's info
        '''
        return self.__str__()


No1 = User(9999, 'Sti', 'Stiven', gender='male')
No1.update(id, '2222')
