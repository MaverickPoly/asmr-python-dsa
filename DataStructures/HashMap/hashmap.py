class HashMap:
    def __init__(self, capacity):
        self.capacity = capacity
        self.size = 0
        self.buckets = [[] for _ in range(self.capacity)]

    def _hash_key(self, key):
        str_key = str(key)
        hashed_key = 0
        for char in str_key:
            hashed_key = (hashed_key + ord(char)) % self.capacity
        return hashed_key

    def __contains__(self, key):
        hashed_key = self._hash_key(key)
        bucket = self.buckets[hashed_key]
        for k, v in bucket:
            if k == key:
                return True
        return False

    def put(self, key, value):
        hashed_key = self._hash_key(key)
        bucket = self.buckets[hashed_key]
        for i, (k, v) in enumerate(bucket):
            if k == hashed_key:
                bucket[i] = (key, value)
                break
        else:
            self.size += 1
            bucket.append((key, value))

    def remove(self, key):
        hashed_key = self._hash_key(key)
        bucket = self.buckets[hashed_key]
        for i, (k, v) in enumerate(bucket):
            if key == k:
                self.size -= 1
                del bucket[i]
                break
        else:
            raise KeyError("This key does not exist!")

    def __len__(self):
        return self.size

    def keys(self):
        return [k for bucket in self.buckets for k, _ in bucket]

    def values(self):
        return [v for bucket in self.buckets for _, v in bucket]

    def items(self):
        return [(k, v) for bucket in self.buckets for k, v in bucket]


if __name__ == '__main__':
    hash_map = HashMap(40)

    print(len(hash_map))
    print(hash_map.buckets)
    hash_map.put("Job", "Programmer")
    hash_map.put("Language", "English")
    hash_map.put("Clever", False)
    hash_map.put("Age", 42)
    hash_map.put("City", "Yakutsk")

    print(hash_map.items())
    print(hash_map.values())
    print(hash_map.keys())
    print(hash_map.buckets)
    print(hash_map)

    print("Job" in hash_map)
    hash_map.remove("Job")
    hash_map.remove("City")
    print("Job" in hash_map)
    print(hash_map.buckets)


