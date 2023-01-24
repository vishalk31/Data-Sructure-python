class Stack :
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return not self.items
    
    def push(self,item):
        self.items.append(item)
        return(self.items)
    
    def remove(self):
        return(self.items.pop())
    
    def peek (self):
        return(self.items[-1])
    
    def size(self):
        return(len(self.items))
    
    def __str__(self):
        return(str(self.items))


S = Stack()
string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
for values in string:
    S.push(values)

while not S.is_empty():
    reversed_string += S.remove()

print(reversed_string)