"""
An iterator is an object that allows sequential access to elements in a collection without exposing its underlying structure.

Understanding Iterators
------------------------
An iterator must implement two methods:

__iter__() → Returns the iterator object itself.

__next__() → Returns the next item in the sequence.
"""

# Creating a custom iterator
class MyNumbers:
    def __init__(self, start, end):
        self.current = start
        self.end = end
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        value = self.current
        self.current+=1
        return value

# Using the iterator
def test_custom_iterator():
    nums = MyNumbers(1, 5)
    for num in nums:
        print(num)


# Using iter() and next() on Built-in Iterables
def using_inbuilt_iterator():
    mylist = [1,2,3]
    nums = iter(mylist)
    print(next(nums))
    print(next(nums))
    print(next(nums))


"""
Generators in Python
A generator is a simpler way to create an iterator using the yield keyword instead of maintaining state manually.

"""
def count_up(start,end):
    while start <= end:
        yield start
        start +=1

def testing_count_up():
    dta = count_up(1,10)
    for each in dta:
        print(each)


def using_shorthand_generators():
    dta = (x*x for x in range(1,4))
    print(next(dta))
    print(next(dta))
    print(next(dta))

using_shorthand_generators()

