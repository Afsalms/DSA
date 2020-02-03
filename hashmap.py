
class HashTable:
    def __init__(self, bucket_size):
        self.bucket_size = bucket_size
        self.buckets = []
        self.create_buckets()

    def create_buckets(self):
        for _ in range(self.bucket_size):
            self.buckets.append([])

    def __str__(self):
        return str(self.buckets)

    def __repr__(self):
        return str(self.buckets)

    def hash_function(self, key):
        return abs(hash(key))%self.bucket_size

    def set_item(self, key, value):
        index = self.hash_function(key)
        if not self.buckets[index]:
            self.buckets[index].append((key, value))
        else:
            for bucket_index, item in enumerate(self.buckets[index]):
                if item[0] == key:
                    self.buckets[index][bucket_index] = (key, value)

    def get_item(self, key):
        index = self.hash_function(key)
        if not self.buckets[index]:
            print("Invalid key")
            return False
        if len(self.buckets[index]) == 1:
            return self.buckets[index][0]
        else:
            for item in self.buckets[index]:
                if item[0] == key:
                    return item


    def delete_item(self, key):
        index = self.hash_function(key)
        if not self.buckets[index]:
            print("Invalid key")
            return False
        if len(self.buckets[index]) == 1:
            del(self.buckets[index][0])
        else:
            for bucket_index, item in enumerate(self.buckets[index]):
                if item[0] == key:
                    del(self.buckets[index][bucket_index])


if __name__ == "__main__":
    a = HashTable(10)
    print("Initial: ", a)
    a.set_item("key1", "value1")
    a.set_item("key2", "value2")
    print("After setting 2 keys", a)
    print("Get item with key1 :", a.get_item("key1"))
    a.delete_item("key2")
    print("After Deleting key2", a)
