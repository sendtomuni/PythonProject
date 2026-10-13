class Parent:
    def __init__(self):
        self.parent_variable = "Parent variable"

    def show(self):
        print("Parent Show")
        print(self.parent_variable)

class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_variable = "Child variable"

    def show(self):
        print("Child Show")
        print(self.child_variable)

child = Child()
child.show()

## If we want child to call the parent show it has to be defined only in child's show method