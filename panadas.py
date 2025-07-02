class Series:
    def __init__(self, data):
        if type(data) == dict:
            self.data = list(data.values())
        elif type(data) == list:
            self.data = data
        else:
            raise TypeError("Series accepts list or dict")
        
    def mean(self):
        return sum(self.data) / len(self.data)


class Dataframe:
    def __init__(self, data):
        if not (type(data) == list and all(type(row) == dict for row in data)):
            raise TypeError("DataFram accepts only list of dictionaries")
        else:
            self.data = data
            self.column = data[0].keys()

    def mean(self):
        rsl = {}
        for c in self.column:
            valus = [row[c] for row in self.data]
            rsl[c] = sum(valus) / len(valus)
        return rsl
        