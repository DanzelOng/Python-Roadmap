# Method Resolution Order (MRO)
# The method with a higher priority will be chosen
# Determined by: 
# 1. Level of Class Hierarchy
# 2. The position of superclass in multiple inheritance

# 1. Level of Class Hierarchy
class A:
    def __init__(self):
        print('Called from A')
    
    def feat1(self):
        print("Feature 1")
    
    def x(self):
        return False

class B(A):
    def __init__(self):
        super().__init__()
        print('Called from B')
    
    def feat2(self):
        print("Feature 2")
    
    def x(self):
        return True

class C(B):
    def __init__(self):
        super().__init__()
    
    def feat3(self):
        print("Feature 3")
    
    def callfeat1(self):
        return super().feat1()

c = C()
# calling __mro__ on a class allows us to see the MRO of that class
# MRO: C -> B -> A
print(C.__mro__)

# Since only feat1 was defined in A and not B, c will search for feat1 by going up to A
c.callfeat1()

# Although method x is defined in A and B, B will be searched first as it is closer to C
print(c.x())

# Position of superclass in multiple inheritance
# In multiple inheritance, the superclass positioned on the left takes priority
class D:
    def __init__(self):
        print('Called from D')

class E(A, D):
    def __init__(self):
        super().__init__()

    def feat4(self):
        print("Feature 4")

# MRO: E > A > D
# instantiating E will only call the init method of A through super()
e1 = E()

# To directly call on the superclass init, we insert the name of the superclass beside __init__
class E(A, D):
    def __init__(self):
        A.__init__(self)
        D.__init__(self)

    def feat4(self):
        print("Feature 4")

# Priority of MRO remains unchanged as A is still on the left
e2 = E()