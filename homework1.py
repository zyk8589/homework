from typing import Iterable, Any

class DeleteItem:
    def __init__(self, iterable: Iterable[Any]):
        self.iterable = list(iterable)
    
    def delete(self, index_to_delete: int) -> list[Any]:
        length_of_iterable: int = len(self.iterable)
        
        deleted_element = self.iterable[index_to_delete]
        
        for i in range(index_to_delete, length_of_iterable - 1):
            self.iterable[i] = self.iterable[i + 1]
        
        self.iterable.pop()
        
        return self.iterable

if __name__ == "__main__":
    di = DeleteItem([1, 2, 3, 4])
    result = di.delete(1)
    print(result)  # Output: [1, 3, 4]