class StrandsDNA:
    '''
    Class for dna chains
    '''
    def __init__(self, all_strands=[]):
        '''
        method for initialization
        :param all_strands: list of dna chains
        '''
        self.all_strands = all_strands

    def add_strands(self, strands):
        '''
        method for adding DNA
        :param strands: DNAs to add
        :return: nothing
        '''
        strands = strands.split()
        self.all_strands.extend(strands)

    def get_max_strands(self):
        '''
        Method for getting pater of chains with maximum length
        :return: final
        '''
        final = ''
        len_str = []
        for i in self.all_strands:
            len_str.append(len(i))
        max_len = max(len_str)
        for i in sorted(self.all_strands):
            if len(i) == max_len:
                count = 0
                for el in i:
                    if i.count(el) == 1:
                        count += 1
                    if count == max_len:
                        final += i + ' '
        return final

    def __str__(self):
        '''
        method for string representation
        :return: string with DNA chains
        '''
        return f'Цепочка ДНК: {self.all_strands}'

    def __repr__(self):
        '''
        method for interactive presentation
        :return: string with DNA chains
        '''
        return self.__str__()


a1 = StrandsDNA(['ABCD', 'ADC', 'AD', 'ADDC', 'RTH', 'ABCD', 'ABHE'])
print(a1.get_max_strands())


