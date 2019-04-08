class Parent:
    greeting = "Hi, I'm a parent object"


class ChildA(Parent):
    greeting = "Hi, I'm a child object"


class ChildB(Parent):
    pass

Parent = Parent()
ChildA = ChildA()
ChildB = ChildB()

print(Parent.greeting,"\n", ChildA.greeting,"\n",ChildB)