class Dataframe:
    def __init__(self, columns, data):
        if not (type(data) == list and all(type(element) == list for element in data)):
            raise TabError("only listes")
        if not (type(columns) in [list, str] and all(type(element) in [list, str] for element in columns)):
            raise TabError("only list or string")
        else:
            self.data = data
            self.columns = columns

    def head(self, h=5):
        return (f"\n{self.columns[:h]} \n{self.data[:h]}")

    def tail(self, t=5):
        return(f"\n{self.columns[-t:]} \n{self.data[-t:]}")
    
    def mean(self):
        rsl = []
        for element in self.data:
            # print("main loop ", element)
            for _ in element:
                #  print("inner loop ", _)
                 rsl.append(_)
        # print("list of resault ", rsl)
        return sum(rsl) / len(rsl)
    
    def max(self):
        rsl = []
        for _ in self.data:
            rsl.append(max(_))
        return max(rsl)
    
    def min(self):
        counter = 0
        rsl = []
        while counter < len(self.data):
            rsl.append(min(self.data[counter]))
            # print("rsl", rsl)
            counter += 1   
        return min(rsl)   
      
    def median(self):
        rsl = []
        mid = []
        for elemnt in self.data:
            for _ in elemnt:
                rsl.append(_)
        rsl.sort()
        # print(rsl)
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
    
df = Dataframe(["a", "B", "c"],[[1, 2, 3], [4, 5, 6], [7, 8, 9, 3]])
print("The Head for data with name of columns",df.head(2))
print("The Tail for data with name of columns",df.tail(2))
print("The mean of data",df.mean())
print("The maxmum number of data",df.max())
print("The minmum number of data",df.min())
print("The median number of data",df.median())
print("The length of data", df.count())
print("The Shape of Data Frame", df.shape()) 
print("index", df.index())   


