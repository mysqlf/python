#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
# import types
# def my_love(self,girl):
#     print('%s love %s'%(self.name,girl))
# class Me(object):
#     def __init__(self,name):
#         self.name=name
# Me.my_love=my_love
# zl=Me('zl')
# zl.my_love('who')
# 
# class Me(object):
#     @property
#     def love(self):
#         print(self._love)
#     @love.setter
#     def love(self,name):
#         self._love=name
# m=Me()
# m.love='zc'
# m.love
    
class Student(object):
    def __init__(self,name):
        self._name=name
    def __str__(self):
        return 'Student object (name :%s)'%self._name
    __repr__=__str__
# print(Student('ZL'))
# s=Student('ZL')
# print(s)

class Fib(object):
    def __init__(self):
        self.a,self.b=0,1
    def __iter__(self):
        return self
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration();
        return self.a
# for n in Fib():
#     print(n)
#     
#     定制一个产生斐波那契数列的类
# class Fibs(object):
#     def __getitem__(self,n):
#         a,b=1,1
#         for x in range(n):
#             a,b=b,a+b
#         return a
# # f=Fibs()
# # print(f[100])
# 定制一个产生斐波那契数列的类支持切片
# class Fib3(object):
#     def __getitem__(self,n):
#         if isinstance(n,int):
#             a,b=1,1
#             for x in range(n):
#                 a,b=b,a+b
#             return a
#         if isinstance(n,slice):
#             start=n.start
#             stop=n.stop
#             if start is None:
#                 start=0
#             a,b=1,1
#             L=[]
#             for x in range(stop):
#                 if x>start:
#                     L.append(a)
#                 a,b=b,a+b
#             return L
# f=Fib3()
# print(f[98:100])
# 
# __getattr__
class Student(object):
    def __init__(self,path=''):#初始化类的属性
        self._path=path
    def __getattr__(self,path):#调用不存在的类方法时返回
        return Student('%s/%s' % (self._path, path))
    def __str__(self):#这用来返回字符串
        return self._path
    __repr__=__str__
    def __call__(self,path):#调用自己的方法或属性
        return Student('%s/%s' % (self._path, path))

#print(Student().user('zl').up)
#流程Student()实例化一个类
#Student().user('')

from enum import Enum,unique

Month=Enum('Month',('Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'))
#for name, member in Month.__members__.items():
#    print(name,'=>',member,',',member.value)#value属性则是自动赋给成员的int常量，默认从1开始计数。
    
    
@unique # @unique装饰器可以帮助我们检查保证没有重复值。
class Week(Enum):
    Sun=0
    Mon=1
    Tue=2
    Wed=3
    Thu=4
    Fri=5
    Sat=6

# day1=Week.Mon
# print(day1)
# day1=Week.Mon.value
# print(day1)
#for name,member in Week.__members__.items():
#    print(name,'=>',member,',',member.value)
#    既可以用成员名称引用枚举常量，又可以直接根据value的值获得枚举常量。
#print(Week(1))

# for x in range(1,30):
#     print(Week(x%7))


# from hello import Hello
# h=Hello()
# h.hello()
# print(type(h))

# def fn(self,name='world'):
#     print('Hello,%s'%name)
# #type()函数既可以返回一个对象的类型，又可以创建出新的类型，
# #比如，我们可以通过type()函数创建出Hello类，
# #而无需通过class Hello(object)...的定义：
# Hello=type('Hello',(object,),dict(hello=fn))
# h=Hello()
# h.hello()
# print(type(Hello))
# #<class 'type'>
# print(type(h))
# #<class '__main__.Hello'>
# #
# 
# class ListMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         attrs['add']=lambda self,value:self.append(value)
#         attrs['d']=lambda self,value:self.pop(value)
#         return type.__new__(cls,name,bases,attrs)
# class MyList(list,metaclass=ListMetaclass):
#     pass
# l=MyList()
# l.add(1)
# print(l)
# l1=list()#list 没有add 方法但是
# #l1.add(1)
# l1.append(1)
# print(l1)
# l.add(2)
# print(l)
# l.d(0)
# print(l)
# 
# class Field(object):
#     def __init__(self,name,column_type):
#         self.name=name
#         self.column_type=column_type
#     def __str__(self):
#         return '<%s:%s>'%(self.__class__.__name__,self.name)
# class StringField(Field):
#     def __init__(self,name):
#         super(StringField,self).__init__(name,'varchar(100)')

# class IntegerField(Field):
#     def __init__(self,name):
#         super(IntegerField,self).__init__(name,'bigint')

# class ModelMetaclass(type):
#     def __new__(cls,name,bases,attrs):
#         if name=='Model':
#             return type.__new__(cls,name,bases,attrs)
#         print('Found model :%s'%name)
#         mappings=dict()
#         for k,v in attrs.items():
#             if isinstance(v,Field):
#                 print('Found mappings :%s==>%s'%(k,v))
#                 mappings[k]=v
#         for k in mappings.keys():
#             attrs.pop(k)
#         attrs['__mappings__']=mappings
#         attrs['__table__']=name
#         return type.__new__(cls,name,bases,attrs)
# class Model(dict,metaclass=ModelMetaclass):
#     def __init__(self,**kw):
#         super(Model,self).__init__(**kw)
#     def __getattr__(Self,key):
#         try:
#             return self[key]
#         except KeyError:
#             raise AttributeError(r"'Modle' object has no attribuys '%s'"%key)
#     def __setattr__(self,key,value):
#         self[key]=value
#     def save(self):
#         fields=[]
#         params=[]
#         args=[]
#         for k,v in self.__mappings__.items():
#             fields.append(v.name)
#             params.append('?')
#         sql='insert into %s (%s) values(%s)'%(self.__table__,','.join(fields),','.join(params))
#         print('SQL:%s'%sql)
#         print('APGS:%s'%str(args))
# class User(Model):
#     id=IntegerField('id')
#     name=StringField('username')
#     email=StringField('email')
#     password=StringField('password')



# u=User(id=12345,name='zl',email='zl@zl.com',password='123456')
# u.save()