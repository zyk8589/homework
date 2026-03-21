class HashTable:
    def __init__(self, size=101):
        self.size = size
        self.table = [None] * size

    def _hash(self, key):
        
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            k, _ = self.table[idx]
            if k == key:
                self.table[idx] = (key, value)
                return
            idx = (idx + 1) % self.size
            if idx == start_idx:
                raise Exception("HashTable is full")
        self.table[idx] = (key, value)

    def get(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            k, v = self.table[idx]
            if k == key:
                return v
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return None

    def remove(self, key):
        idx = self._hash(key)
        start_idx = idx
        while self.table[idx] is not None:
            k, _ = self.table[idx]
            if k == key:
                self.table[idx] = None
                return True
            idx = (idx + 1) % self.size
            if idx == start_idx:
                break
        return False