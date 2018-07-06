class Node:
    def __init__(self, obj, next=None):
        self.value = obj
        self.next = next


class Animal:
    def __init__(self, value):
        self.value = value
        self.priority = 0

    def set_priority(self, priority):
        self.priority = priority

    def get_priority(self):
        return self.priority

    def __str__(self):
        return self.value

    def is_older_than(self, other):
        return self.get_priority() >= other.get_priority()


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
        item.set_priority(self.priority)
        self.priority += 1

        if isinstance(item, Dog):
            if self.dog is None:
                self.dog = self.dogHead = Node(item)
            else:
                self.dog.next = Node(item)
                self.dog = self.dog.next
        else:
            if self.cat is None:
                self.cat = self.catHead = Node(item)
            else:
                self.cat.next = Node(item)
                self.cat = self.cat.next

    def dequeue_cat(self):
        cat = self.catHead
        self.catHead = self.catHead.next
        return cat

    def dequeue_dog(self):
        dog = self.dogHead
        self.dogHead = self.dogHead.next
        return dog

    def dequeue_any(self):
        if not self.dogHead:
            return self.dequeue_cat()
        elif not self.catHead:
            return self.dequeue_dog()
        else:
            if self.dogHead.value.is_older_than(self.catHead.value):
                return self.dequeue_cat()
            else:
                return self.dequeue_dog()


a = AnimalShelter()
a.enqueue(Cat('c1'))
a.enqueue(Cat('c2'))
a.enqueue(Cat('c3'))
a.enqueue(Dog('d1'))
print(a.dequeue_cat().value)
print(a.dequeue_dog().value)
print(a.dequeue_any().value)
print(a.dequeue_any().value)





