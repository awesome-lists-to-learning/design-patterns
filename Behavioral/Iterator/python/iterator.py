'''
Python prescribes a syntax for iterators as part of the language itself,
so that language keywords such as for work with what Python calls sequences.
A sequence has an __iter__() method that returns an iterator object. The
"iterator protocol" requires next() return the next element or raise a
StopIteration exception upon reaching the end of the sequence.
Iterators also provide an __iter__() method returning themselves so that they
 can also be iterated over e.g., using a for loop.
'''

class Item:

    def __init__(self, name, val):
        self.name = name
        self.val = val

    def __str__(self):
        return "{} {}".format(self.name, self.val)

class ItemsIterator:
    def __init__(self, items):
        self.index = 0
        self.items = items

    def has_next(self):
        if self.index >= len(self.items):
            return False
        return True

    def next(self):
        item = self.items[self.index]
        self.index += 1
        return item

if __name__ == '__main__':
    item1 = Item('car', 30000)
    item2 = Item('house', 100000)
    item3 = Item('bike', 500)
    item4 = Item('tv', 800)
    items = []
    items.append(item1)
    items.append(item2)
    items.append(item3)
    items.append(item4)

    iterator = ItemsIterator(items)

    while iterator.has_next():
        item = iterator.next()
        print item