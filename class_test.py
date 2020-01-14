'''class A:
    def __init__(self):
        print('A')
'''
class B():
    def __init__(self):
        self.b_value = 'B'
        print('B')

class C():
    def __init__(self):
        self.c_value = 'C'
        print('C')

class D(C, B):
    def __init__(self):
        print('D')


d = D()
print(d.c_value)
print(D.__mro__)