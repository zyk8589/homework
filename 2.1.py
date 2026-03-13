from collections.abc import Sequence
from typing import Any

class MySet:
    def __init__(self, iterable: Sequence[Any]):
        
        self.data = []
        for item in iterable:
            self.insert(item)

    def query(self, element: Any) -> bool:
        
        for item in self.data:
            if item == element:
                return True
        return False

    def insert(self, element: Any) -> bool:
        
        if self.query(element):
            return False
        self.data.append(element)
        return True

    def delete(self, element: Any) -> bool:
        
        for index, item in enumerate(self.data):
            if item == element:
                self.data.pop(index)
                return True
        return False

    def __repr__(self):
        return f"MySet({self.data})"

fruits = ['apple', 'banana', 'cherry', 'orange', 'mango']
my_set = MySet(fruits)

print("初始集合:", my_set)


print("插入 apple (重复):", my_set.insert('apple'))
print("插入 grape (新):", my_set.insert('grape')) 


print("查询 banana 是否存在:", my_set.query('banana')) 

print("删除 cherry:", my_set.delete('cherry'))
print("删除后的集合:", my_set)