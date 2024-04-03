class MorseMsg:
    '''

    '''
    morse_dict = {'.-': ('A', 'А'), '-...': ('B', 'Б'), '-.-.': ('C', 'Ц'), '-..': ('D', 'Д'), '.': ('E', 'Е'),
                  '..-.': ('F', 'Ф'), '--.': ('G', 'Г'), '....': ('H', 'Х'), '..': ('I', 'И'), '.---': ('J', 'Й'),
                  '-.-': ('K', 'К'), '.-..': ('L', 'Л'), '--': ('M', 'М'), '-.': ('N', 'Н'), '---': ('O', 'О'),
                  '.--.': ('P', 'П'), '--.-': ('Q', 'Щ'), '.-.': ('R', 'Р'), '...': ('S', 'С'), '-': ('T', 'Т'),
                  '..-': ('U', 'У'), '...-': ('V', 'Ж'), '.--': ('W', 'В'), '-..-': ('X', 'Ь'), '-.--': ('Y', 'Ы'),
                  '--..': ('Z', 'З'), '.-.-': ('', 'я')}
    glas = 'АЕЁИОУЫЭЮAEIOUY'

    def __init__(self, str):
        '''
        method for initialization
        :param str: pater in morse
        '''
        self.str = str

    def eng_decode(self):
        '''
        method for decoding to english
        :return: pater in english
        ='''
        lst = self.str.split()
        s = ''
        for i in lst:
            for key, value in self.morse_dict.items():
                if key == i:
                    s += value[0] + ' '
        return s

    def ru_decode(self):
        '''
        method for decoding to russian
        :return: pater in russian
        '''
        lst = self.str.split()
        s = ''
        for i in lst:
            for key, value in self.morse_dict.items():
                if key == i:
                    s += value[1] + ' '
        return s

    def get_vowels(self, lang):
        '''
        method for getting vowels
        :param lang:language
        :return: only vowels
        '''
        if lang == 'ru':
            x = 1
        else:
            x = 0
        lst = self.str.split()
        s = ''
        for i in lst:
            for key, valeu in self.morse_dict.items():
                if key == i:
                    if valeu[x] in self.glas:
                        s += valeu[x] + ' '
        return s

    def get_consonants(self, lang):
        '''
        method for getting consonants
        :param lang: language
        :return: consonants
        '''
        if lang == 'ru':
            x = 1
        else:
            x = 0
        lst = self.str.split()
        s = ''
        for i in lst:
            for key, value in self.morse_dict.items():
                if key == i:
                    if value[x] not in self.glas:
                        s += value[x] + ' '
        return s

    def __str__(self):
        '''
        method for string representation
        :return: string with a message
        '''
        return f'Закодированное сообщение: {self.str}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with a message
        '''
        return self.__str__()


first = MorseMsg('-.-- --- ..- ... .... --- ..- .-.. -.. --- .. - ')
second = MorseMsg('- -.-- ... ----. --..--- ..---...-.')
print(first.eng_decode())
print(second.ru_decode())
print(second.get_vowels('ru'))
print(second.get_consonants('ru'))
