class Node:
    def __init__(self, value, next =None):
        self.value = value
        self.next = next

class Animal:
    def __init__(self, value):
        self.value = value
        self.priority = 0

    def setPriority(self, priority):
        self.priority = priority

    def getPriority(self):
        return self.priority

    def __str__(self):
        return self.value

    def isOlderThan(self, other):
        return self.getPriority() >= other.getPriority()


class Dog(Animal):
    pass

class Cat(Animal):
    pass

class AnimalShelter:
    def __init__(self):
        self.dog = self.cat = None
        self.dogHead = self.catHead = None
        self.priority = 0

    def enqueue(self, item):
        item.setPriority(self.priority)
        self.priority += 1

        if isinstance(item, Dog):
            if self.dog is None:
                self.dog = self.dogHead= Node(item)
            else:
                self.dog.next = Node(item)
                self.dog = self.dog.next
        else:
            if self.cat is None:
                self.cat = self.catHead = Node(item)
            else:
                self.cat.next = Node(item)
                self.cat = self.cat.next

    def dequeueCat(self):
        cat = self.catHead
        self.catHead = self.catHead.next
        return cat

    def dequeueDog(self):
        dog = self.dogHead
        self.dogHead = self.dogHead.next
        return dog

    def dequeueAny(self):
        if not self.dogHead:
            return self.dequeueCat()
        elif not self.catHead:
            return self.dequeueDog()
        else:
            if self.dogHead.value.isOlderThan(self.catHead.value):
                return self.dequeueCat()
            else:
                return self.dequeueDog()


a = AnimalShelter()
a.enqueue(Cat('c1'))
a.enqueue(Cat('c2'))
a.enqueue(Cat('c3'))
a.enqueue(Dog('d1'))
print(a.dequeueCat().value)
print(a.dequeueDog().value)
print(a.dequeueAny().value)
print(a.dequeueAny().value)





