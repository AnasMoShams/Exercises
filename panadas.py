class Series:
    def __init__(self, data):
        if type(data) == dict:
            self.data = list(data.values())
            self.key = list(data.keys()) 

        elif type(data) == list:
            self.data = data
            self.key = None

        else:
            raise TypeError("Series accepts list or dict")
        
    def mean(self):
        return sum(self.data) / len(self.data)
    
    def index(self):
        if self.key is not None:
            return self.key
        else:
            return list(range(len(self.data)))

class Dataframe:
    def __init__(self, data):
        # check if Data is a list of dictionaries or not
        if not (type(data) == list and all(type(element) == dict for element in data)):
            raise TypeError("DataFram accepts only list of dictionaries")
        else:
            self.data = data # stor the Data
            
            # get columns name from frist element
            cols =set() # get unique column names
            for row in data:
                cols.update(row.keys())

            self.colunms = list(cols)
            self.empty = len(self.colunms) == 0
    
    #  return the frist h number of rows
    def head(self, h=5):
        return self.data[:h]
    
    # return the last t number of rows
    def tail(self, t=5):
        return self.data[-t:]

    #  calculat mean or averge for data
    def mean(self):
        rsl = {} # stor the result for each column

        for c in self.columns: # To through each column
            valus = []
            for element in self.data:
                if c in element and type(element[c]) in [int, float]:
                    valus.append(element[c])
            if valus: #  check if values is not empty
                rsl[c] = sum(valus) / len(valus) 
        return rsl
    
     # calculat sum for data
    def sum(self):
        rsl = {}
        for c in self.columns:  # To through each column
                total = 0
                for element in self.data:  # To through each row
                    val = element.get(c)
                    if type(val) in [int, float]: # to be sure this val is number or not
                        total += val
                rsl[c] = total # stor teh total sum for this column
        return rsl
    
    # to give you the minmum value in columns
    def min(self):
        rsl = {}
        for c in self.columns:
            # to get numeric values in column "c", skip row if "c" doesn't exist
            values = [element[c] for element in self.data if c in element and type(element[c]) in [int, float]]  
            if values: # check if values is not empty
                rsl[c] = min(values)
        return rsl
    
    #  to give you the maxmum value in columns
    def max(self):
        rsl = {}
        for c in self.columns:
            # to get numeric values in column "c", skip row if "c" doesn't exist
            values = [element[c] for element in self.data if c in element and type(element[c]) in [int, float]]
            if values: # check if values is not empty
                rsl[c] = max(values)
        return rsl
    
    # to count how many values not equal None in each column
    def count(self):
        rsl = {}
        for c in self.columns:
            count = 0
            for element in self.data:
                if c in element and element[c] is not None: # to check the key exist and the values is not None
                    count += 1

            rsl[c] = count
        return rsl

    # return the shape of data in (rows, columns)
    def shape(self):
        rows = len(self.data)
        columns = len(self.columns)
        return (rows, columns)
    
    # return a list of index numbers of the rows
    def index(self):
        return list(range(len(self.data)))
    
    # return the coulmns names
    def columns_(self):
        return self.columns

data = [
    {},
    {},
    {}
    ]
df = Dataframe(data)
print(f"Head for data is: {df.head(2)}")
print(f"Tail for data is: {df.tail(2)}")
print(f"Mean for data is: {df.mean()}")
print(f"sum for data is: {df.sum()}")
print(f"The minmum number of data is: {df.min()}")
print(f"The maxmum number of data is: {df.max()}")
print(f"How many element in data is: {df.count()}")
print(f"Shape for data is: {df.shape()}")
print(f"Columns for data is: {df.columns_()}")