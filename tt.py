
#==============================================================================
# # -*- coding: utf-8 -*-
# import pickle
# class t(object):
#     def __init__(self,x):
#         self.tt = x
#         print(x)
# f = open('y.pkl','wb');
# a = [1,2];
# b = a;
# a.append(3);
# pickle.dump(a,f)
# pickle.dump(b,f)
# f.close()
# f = open('y.pkl','rb');
# x = pickle.load(f)
# y = pickle.load(f)
# f.close()
# print(x is y)
#==============================================================================

#==============================================================================
# # -*- coding: utf-8 -*-
# import pickle
# class t(object):
#     def __init__(self,x):
#         self.tt = x
#         print(x)
# f = open('y.pkl','wb');
# a = [1,2];
# b = a;
# a.append(3);
# pickle.dump((a,b),f)
# #pickle.dump(b,f)
# f.close()
# f = open('y.pkl','rb');
# x,y = pickle.load(f)
# #y = pickle.load(f)
# f.close()
# print(x is y)
#==============================================================================

#==============================================================================
# # -*- coding: utf-8 -*-
# import pickle
# class t(object):
#     def __init__(self,x):
#         self.tt = x
#         print(x)
# f = open('y.pkl','wb');
# pickler = pickle.Pickler(f)
# a = [1,2];
# b = a;
# a.append(3);
# pickler.dump(a)
# pickler.dump(b)
# f.close()
# f = open('y.pkl','rb');
# unpickler = pickle.Unpickler(f)
# x = unpickler.load()
# y = unpickler.load()
# f.close()
# print( x is y)
#==============================================================================

#==============================================================================
# import pickle
# class Foo(object):  
#     def __init__(self, value):  
#         self.value = value  
# f = open('111.pkl', 'rb') 
# #foo = Foo('What is a Foo?')  
# ftt = pickle.load(f)  
# print(ftt.value)
# f.close()
#==============================================================================
class A:
    def __init__( self, num = 0, a = None, b = None ):
        self.l = a
        self.r = b
        self.num = num
        
    def addl(self,num):
        self.l = A(num)
    
    def addr(self,num):
        self.r = A(num)
