from abc import ABC, abstractmethod
'/////////////////////////////////////////////////////////////////////   Наївна реалізація  ///////////////////////////////////////////////////////////////////////////////////////////////////'
class MyABC:
    def foo(self):
        raise NotImplementedError()

    def bar(self):
        raise NotImplementedError()

class ActualMy(MyABC):
    def foo(self):
        print('foo')

    def bar(self):
        print('bar')

a = ActualMy()
# a.foo()     # foo
# a.bar()     # raises NotImplementedError
'/////////////////////////////////////////////////////////////////////    ABC    ///////////////////////////////////////////////////////////////////////////////////////////////////'
class MyBaseClass(ABC):
    @abstractmethod
    def foo(self):
        pass

    @abstractmethod
    def baz(self):
        pass

class Child(MyBaseClass):
    def foo(self):
        return 'foo'
    
    def baz(self):
        return 'baz'

c = Child()
# print(c.foo())
# print(c.baz())
