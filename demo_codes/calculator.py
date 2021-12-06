class Add:
    def sum(self, a,b):
        return a+b;
    
class Sub:
    def sub(self, a,b):
        return a-b;
class Div(Add,Sub):
    def div(self, a,b):
        return a/b;
 
a = int(input("enter a : "))

b = int(input("enter b : ") )  
q = Div()
print(q.sum(a,b));
print(q.sub(a,b));
print(q.div(a,b));