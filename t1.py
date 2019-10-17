marksheet = []
# for _ in range(0,int(input())):
#     marksheet.append([input(), float(input())])

# second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
# print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
x = simpleGeneratorFun()
print(dir(x))
print(next(x))
print(next(x))
print(next(x))
try:
    print(next(x))
except Exception as e:
    print("???????????")
    print(e.value)

class Parent(object):
    def get_context_data(self, **kwargs):
        print('Parent')

class ListSortedMixin(object):
    def get_context_data(self, **kwargs):
        print('ListSortedMixin')
        return super(ListSortedMixin,self).get_context_data(**kwargs)

class ListPaginatedMixin(object):
    def get_context_data(self, **kwargs):
        print('ListPaginatedMixin')
        return super(ListPaginatedMixin,self).get_context_data(**kwargs)

class MyListView(ListSortedMixin, ListPaginatedMixin, Parent):
    def get_context_data(self, **kwargs):
        return super(MyListView,self).get_context_data(**kwargs)


m = MyListView()
print(MyListView.__mro__)
m.get_context_data(l='l')

class A:
    def speak(self):
        print("class A speaking")


class B:
    def speak(self):
        print("class B speaking")


class C(B, A):
    pass

m = C()
m.speak()
print(C.__mro__)

# defining a decorator 
def hello_decorator(func): 
  
    # inner1 is a Wrapper function in  
    # which the argument is called 
      
    # inner function can access the outer local 
    # functions like in this case "func" 
    def inner1(): 
        print("Hello, this is before function execution") 
  
        # calling the actual function now 
        # inside the wrapper function. 
        func() 
  
        print("This is after function execution") 
          
    return inner1 
  
  
# defining a function, to be called inside wrapper 
@hello_decorator
def function_to_be_used(): 
    print("This is inside the function !!") 

function_to_be_used()