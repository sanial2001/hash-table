class HashTable:
    def __init__(self, size):
        self.size = size
        self.hash_table = [None] * self.size

    def get_index(self, key):
        result = 0
        for letter in key:
            ord_value = ord(letter)
            result = result + ord_value
        return result % self.size

    def set_value(self, key, value):
        hash_index = self.get_index(key)
        self.hash_table[hash_index] = (key, value)

    def get_value(self, key):
        hash_index = self.get_index(key)
        key_value = self.hash_table[hash_index]
        if key_value is None:
            return None
        else:
            key, value = key_value
            return value

    def list_all(self):
        return [kv for kv in self.hash_table if kv is not None]



hash_table = HashTable(10)
hash_table.set_value('sanial', 48)
print(hash_table.get_value('sanial'))
print(hash_table.list_all())
