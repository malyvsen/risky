from ..base import Indicator



class Column(Indicator):
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def calculate(self, data):
        return data[self.name]


Open = lambda: Column('open')
High = lambda: Column('high')
Low = lambda: Column('low')
Close = lambda: Column('close')
Volume = lambda: Column('volume')