#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Dog(object):

    def __init__(self):
        self.name = "Dog"

    def brak(self):
        return "woof"


class Cat(object):

    def __init__(self):
        self.name = "Cat"

    def meow(self):
        return "meow"


class Human(object):

    def __init__(self):
        self.name = "Human"

    def speak(self):
        return "hrllo"


class Car(object):

    def __init__(self):
        self.name = "Car"

    def make_noise(self, octane_level):
        return "Vroom{0}".format("!"*octane_level)


class Adapter(object):

    """
   Adapts an object by replacing methods.
   Usage:
   dog = Dog
   dog = Adapter(dog, dict(make_noise=dog.bark))
   >>> objects = []
   >>> dog = Dog()
   >>> print(dog.__dict__)
   {'name': 'Dog'}
   >>> objects.append(Adapter(dog, make_noise=dog.bark))
   >>> print(objects[0].original_dict())
   {'name': 'Dog'}
   >>> cat = Cat()
   >>> objects.append(Adapter(cat, make_noise=cat.meow))
   >>> human = Human()
   >>> objects.append(Adapter(human, make_noise=human.speak))
   >>> car = Car()
   >>> car_noise = lambda: car.make_noise(3)
   >>> objects.append(Adapter(car, make_noise=car_noise))
   >>> for obj in objects:
   ...     print('A {} goes {}'.format(obj.name, obj.make_noise()))
   A Dog goes woof!
   A Cat goes meow!
   A Human goes 'hello'
   A Car goes vroom!!!
   """

    def __init__(self, obj, **adapted_methods):
        self.obj = obj
        self.__dict__.update(adapted_methods)

    def __getattr__(self, attr):
        return getattr(self.obj, attr)

    def original_dict(self):
        return self.obj.__dict__


def main():
    objects = []
    dog = Dog()
    print(dog.__dict__)
    objects.append(Adapter(dog, make_noise=dog.brak))
    print(objects[0].__dict__)
    print(objects[0].original_dict())
    cat = Cat()
    objects.append(Adapter(cat, make_noise=cat.meow))
    human = Human()
    objects.append(Adapter(human, make_noise=human.speak))
    car = Car()
    objects.append(Adapter(car, make_noise=lambda: car.make_noise(3)))
    for obj in objects:
        print("A {0} goes {1}".format(obj.name, obj.make_noise()))
if __name__ == "__main__":
    main()
# 适配器模式
# 在不能修改数据来源类又不能将接收接口修改额时候
# 就可以写一个中间类，将两个类对接
# 比如产生的日志既要写日志文件又要存数据库的时候，
# 日志产生不可能写两个方法
# 这样就可以选择写一个适配器，将日志转为文件给文件系统
# 然后又将日志数据化传给数据库
# 即使以后添加新的存储方式也只需要在适配器中添加一个方法即可
#
# Adapter 设计模式主要目的组合两个不相干类，
# 常用有两种方法，第一种解决方案是修改各自类的接口。
# 但是如果没有源码，
# 或者不愿意为了一个应用而修改各自的接口，
# 则需要使用 Adapter 适配器，
# 在两种接口之间创建一个混合接口。
