from typing import Any
from collections.abc import Sequence

class OrderedArrayInsert:
    def __init__(self, iterable: Sequence[Any]):
        self.iterable = list(iterable)
        self.len = len(self.iterable)

    def insert(self, element: Any) -> None:
        
        insert_index = self.len 
        for index, value in enumerate(self.iterable):
            if element < value:
                insert_index = index
                break
        self.iterable.append("") 
        
        for i in range(self.len, insert_index, -1):
            self.iterable[i] = self.iterable[i-1]

        self.iterable[insert_index] = element
        
        self.len += 1
base_array = [1, 4, 21, 59]
ordered_array_insert = OrderedArrayInsert(base_array)
ordered_array_insert.insert(19)
ordered_array_insert.insert(100) 
print(ordered_array_insert.iterable) 
