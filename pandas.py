from collections import Counter
import numpy as np 
class Series:
    def __init__(self, data, _index=None):
        self.data = data
        self._index = _index

    def __numrical(self):
        numric_list = []
        for element in self.data:
            if type(element) in [int, float]:
                numric_list.append(element)
            else:
                raise TypeError("only numbers is available")
        return numric_list
    
    def sum(self):
        return sum(self.__numrical())

    def mean(self):
        return self.sum()/len(self.__numrical())
    
    def median(self):
        numrical_data = self.__numrical()
        numrical_data.sort()
        mid = []
        if len(numrical_data) % 2 ==0:
            mid.append(numrical_data[len(numrical_data)// 2 - 1])
            mid.append(numrical_data[len(numrical_data)//2])
            mid = sum(mid) / 2
            return(mid)
        else:
            return (numrical_data[len(numrical_data)// 2])
    
    def min(self):
        return min(self.__numrical())

    def max(self):
        return max(self.__numrical())
    
    def index(self):
        if self._index == None:
            raise TypeError("you should write list of index to print this function")
        else:
            return dict(zip(self._index, self.__numrical()))
    
    def count(self):
        counter = 0
        lenght = len(self.__numrical())
        while lenght > 0:
            counter += 1
            lenght -= 1
        return counter

    def shape(self):
        return (self.count(),)
    
    def name(self, name):
        return f"The name of series is {name} : {self.__numrical()}, {self._index}" if self._index else f"The name of series is {name} : {self.__numrical()}"
    
    def __frequensy(self):
        lst = self.__numrical()
        rsl = []
        for element in lst:
            rsl.append(type(element))
        rsl2 = Counter(rsl)
        return rsl2.most_common(1)[0][0]
    
    def values(self):
        return f"your values is {self.data}, {self.__frequensy()}"



series = Series([1, 2, 3, 4, 5, 0, 5], ["a", "b", "c", "d", "e", "f", "g"])
print("The submission for data", series.sum())
print("The mean of data",series.mean())
print("The med number is ",series.median())
print("The minmum value is ",series.min())
print("The maxmum value is ",series.max())
print("Your index for data that modifide ",series.index())
# print(series.index().values())
# print(series.index().keys())
print("how many number of values",series.count())
print("The shape of values is your dimention", series.shape())
print("Name of Series is ",series.name("a"))
print("Values in series is ",series.values())

print("#" * 20)

class Dataframe:
    __supported_type=np.ndarray|Series|list
    def __init__(self, columns, data):
        # very slow check 
        if  not (isinstance(data,self.__supported_type) and isinstance(columns,self.__supported_type)) :
            raise TabError("only thoese types are supported",self.__supported_type)
        else:
            self.data = data
            self.columns = data[0] if columns == None else columns 

    def head(self, h=5):
        return (f"\n{self.columns[:h]} \n{self.data[:h]}")

    def tail(self, t=5):
        return(f"\n{self.columns[-t:]} \n{self.data[-t:]}")
    
    def mean(self):
        rsl = []
        for element in self.data:
            for _ in element:
                 rsl.append(_)
        return sum(rsl) / len(rsl)
    
    def max(self):
        # rsl = []
        # for _ in self.data:
        #     rsl.append(max(_))
        # return max(rsl)
        return max(sum(self.data, []))
    
    def min(self):
        # counter = 0
        # rsl = []
        # while counter < len(self.data):
        #     rsl.append(min(self.data[counter]))
        #     counter += 1   
        # return min(rsl)  
        return min(sum(self.data, []))
    
    def median(self):
        rsl = []
        mid = []
        for elemnt in self.data:
            for _ in elemnt:
                rsl.append(_)
        rsl.sort()
        if len(rsl) % 2 ==0:
            mid.append(rsl[len(rsl)// 2 - 1])
            mid.append(rsl[len(rsl)//2])
            mid = sum(mid) / 2
            return(mid)
        else:
            return rsl[len(rsl)//2]
        
    def count(self):
        counter = 0
        for elemnt in self.data:
            for _ in elemnt:
                    # print(elemnt)
                    # print(counter)
                    counter += 1
        return counter
    
    def shape(self):
        columns = len(self.columns)
        rows = len(self.data)
        return(rows, columns)
    
    def index(self):
        return list(range(len(self.data)))
    
    def __length(self):
        for i in range(len(self.data)):
            if len(self.columns) >= len(self.data[i]):
                while len(self.data[i]) < len(self.columns):
                    self.data[i].append(None)
            else:
                raise TypeError("the length of data is bigger than length of columns")
        return self.columns, self.data
    
    def display(self):
        self.columns, self.data = self.__length()
        rsl = {}
        for i, col in enumerate(self.columns):
            values = []
            for element in self.data:
                values.append(element[i])
            rsl[col] = values
            
        print("     ".join(rsl.keys()))

        for i in range(len(next(iter(rsl.values())))):
            rows = []
            for _ in rsl:
                rows.append(str(rsl[_][i]))
            print("     ".join(rows))

    
df = Dataframe(["a", "B", "c"],[[1, 2, 10], [4, 5, 6], [7, 8, 120]])
print("The Head for data with name of columns",df.head(2))
print("The Tail for data with name of columns",df.tail(2))
print("The mean of data",df.mean())
print("The maxmum number of data",df.max())
print("The minmum number of data",df.min())
print("The median number of data",df.median())
print("The length of data", df.count())
print("The Shape of Data Frame", df.shape()) 
print("index", df.index()) 
print("Your DataFram ")
df.display() 


# def length(columns, data):
#     for i in range(len(data)):
#         # print("element in data",data[i])
#         if len(columns) >= len(data[i]):
#             while len(data[i]) < len(columns):
#                 # print("data",data)
#                 data[i].append("Nan")
#         else:
#             raise TypeError("the length of data is biger than length of columns")
#     return(columns, data)
    

# def display(columns, data):
#     columns, data = length(columns, data)
#     rsl = {}
#     for i,col in enumerate(columns):
#         values = []
#         for elemnet in data:
#             values.append(elemnet[i])
#         rsl[col] = values
    
#     print("     ".join(rsl.keys()))

#     for i in range(len(next(iter(rsl.values())))):
#         rows = []
#         for col in rsl:
#             # print("col", col)
#             rows.append(str(rsl[col][i]))
#             # print("form in",str(rsl[col][i]))
#         print("     ".join(rows))




