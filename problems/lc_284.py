# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """

class PeekingIterator:
    nextEl = None
    itr = None

    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.itr = iterator
        if self.itr.hasNext():
            self.nextEl = self.itr.next()

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        return self.nextEl

    def next(self):
        """
        :rtype: int
        """
        temp = self.nextEl
        if self.itr.hasNext():
            self.nextEl = self.itr.next()
        else:
            self.nextEl = None
        return temp

    def hasNext(self):
        """
        :rtype: bool
        """

        return self.nextEl != None
