


class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single intrreger that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> []:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:

    def __init__(self, nestedList: [NestedInteger]):
        self.lst = []

        def generate(nestedList):
            for i in nestedList:
                if i.isInteger():
                    self.lst.append(i.getInteger())
                else:
                    generate(i.getList())

        generate(nestedList)


    def next(self) -> int:
        return self.lst.pop(0)

    def hasNext(self) -> bool:
        return len(self.lst) != 0






nested, v = NestedIterator([1,[2,3]]), []
while nested.hasNext():
    v.append(nested.next())

print(v)

