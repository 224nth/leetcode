import queue


class LRUCache(object):

    capacity = None
    store = {}
    lst = []

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.store:
            val = self.store[key]
            self.lst.pop(val[1])
            self.lst.append(key)
            return val[0]

        return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """

        if len(self.store) == self.capacity:
            to_expire = self.lst.pop(0)
            self.store.pop(to_expire)

        self.lst.append(key)
        self.store[key] = [value,len(self.lst)-1]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)



# cache = LRUCache(2);
# print(cache.put(1, 1));
# print(cache.put(2, 2));
# print(cache.get(1));       #returns 1
# print(cache.put(3, 3));    # evicts key 2
# print(cache.get(2));       # returns -1 (not found)
# print(cache.put(4, 4));    # evicts key 1
# print(cache.get(1));       # returns -1 (not found)
# print(cache.get(3));       # returns 3
# print(cache.get(4));       # returns 4


cache = LRUCache(1);
print(cache.put(2, 1));
print(cache.get(2))
print(cache.put(3, 2));
print(cache.get(2))
print(cache.get(3))

