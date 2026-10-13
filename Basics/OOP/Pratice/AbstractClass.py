from abc import abstractmethod, ABC


class Parent(ABC):
    def meth1(self):
        print("Parent1 - Meth1")

    @abstractmethod
    def meth2(self):
        pass

class Child(Parent):
    def meth3(self):
        print("Child1 = meth3")

    def meth2(self):
        print("Child1 = meth2")

child = Child()
child.meth2()
