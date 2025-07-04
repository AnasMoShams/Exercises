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
        


# decoration function that takes another method
def skip_if_empty(m):
    # inner function that checks if the object is empty or not
    def checker_is_empty(self, *args, **kwargs):
        # this condition gives you None if the object is empyt
        if self.empty:
            return None
        # if the object is not empty call the function and skip this function
        return m(self, *args, **kwargs)
    # return the inner function 
    return checker_is_empty


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
    
    @ skip_if_empty
    #  return the frist h number of rows
    def head(self, h=5):
        return self.data[:h]
    
    @ skip_if_empty
    # return the last t number of rows
    def tail(self, t=5):
        return self.data[-t:]

    @ skip_if_empty
    #  calculat mean or averge for data
    def mean(self):
        rsl = {} # stor the result for each column

        for c in self.colunms: # To through each column
            valus = []
            for element in self.data:
                if c in element and type(element[c]) in [int, float]:
                    valus.append(element[c])
            if valus: #  check if values is not empty
                rsl[c] = sum(valus) / len(valus) 
        return rsl
    
    @ skip_if_empty
    # calculat sum for data
    def sum(self):
        rsl = {}
        for c in self.colunms:  # To through each column
                total = 0
                for element in self.data:  # To through each row
                    val = element.get(c)
                    if type(val) in [int, float]: # to be sure this val is number or not
                        total += val
                rsl[c] = total # stor teh total sum for this column
        return rsl
    
    @ skip_if_empty
    # to give you the minmum value in columns
    def min(self):
        rsl = {}
        for c in self.colunms:
            # to get numeric values in column "c", skip row if "c" doesn't exist
            values = [element[c] for element in self.data if c in element and type(element[c]) in [int, float]]  
            if values: # check if values is not empty
                rsl[c] = min(values)
        return rsl
    
    @ skip_if_empty
    #  to give you the maxmum value in columns
    def max(self):
        rsl = {}
        for c in self.colunms:
            # to get numeric values in column "c", skip row if "c" doesn't exist
            values = [element[c] for element in self.data if c in element and type(element[c]) in [int, float]]
            if values: # check if values is not empty
                rsl[c] = max(values)
        return rsl
    
    @ skip_if_empty
    # to count how many values not equal None in each column
    def count(self):
        rsl = {}
        for c in self.colunms:
            count = 0
            for element in self.data:
                if c in element and element[c] is not None: # to check the key exist and the values is not None
                    count += 1

            rsl[c] = count
        return rsl

    # return the shape of data in (rows, columns)
    def shape(self):
        rows = len(self.data)
        columns = len(self.colunms)
        return (rows, columns)
    
    # return a list of index numbers of the rows
    def index(self):
        return list(range(len(self.data)))
    
    # return the coulmns names
    def columns_(self):
        return self.colunms

data = [
    {"a": 1},
    {},
    {}
    ]
df = Dataframe(data)
print(f"Head for data is: {df.head()}")
print(f"Tail for data is: {df.tail()}")
print(f"Mean for data is: {df.mean()}")
print(f"sum for data is: {df.sum()}")
print(f"The minmum number of data is: {df.min()}")
print(f"The maxmum number of data is: {df.max()}")
print(f"How many element in data is: {df.count()}")
print(f"Shape for data is: {df.shape()}")
print(f"Columns for data is: {df.columns_()}")