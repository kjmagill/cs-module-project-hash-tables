class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table with `capacity` buckets that accepts string keys
    """

    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        n = range(capacity)
        for i in n:
            self.storage.append(HashTableEntry(i, None))

    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list)
        """
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        used_storage = []
        load_factor = 0
        for i in self.storage:
            if i != None:
                used_storage.append(i)
                load_factor = len(used_storage) / self.capacity
        return load_factor


    def fnv1(self, key, seed=0):
        """
        Fowler-Noll-Vo (FNV-1) 64-bit hash function
        """
        FNV_prime = 1099511628211
        offset_basis = 14695981039346656037
        hash = offset_basis + seed
        for x in key:
            hash = hash * FNV_prime
            hash = hash ^ ord(x)
        return hash


    def djb2(self, key):
        """
        DJB2 32-bit hash function by Professor Daniel J. Bernstein
        * one of the most efficient hash functions ever published *
        """
        hash = 5381
        for x in key:
            hash = hash * 33 + ord(x)
        # return the hash with 0xFFFFFFFF masking
        return hash & 0xFFFFFFFF


    def hash_index(self, key):
        """
        Take an arbitrary key and return a valid integer index
        between within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        i = self.hash_index(key)
        self.storage[i].value = value
        return self.storage[i].value


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        self.put(key, None)


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        i = self.hash_index(key)
        element = self.storage[i]
        if element is not None:
            return element.value
        return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and rehashes all key/value pairs.
        """
        # TODO | THIS IS A DAY-2 EXERCISE, along with:
        # - setting up  get_load_factor(), which I've already completed
        # - setting up automatic hashtable size halving at <(0.2) & doubling at >(0.7)
        self.capacity = new_capacity
        # INCOMPLETE


if __name__ == "__main__":
    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
    ht.put("line_2", "Did gyre and gimble in the wabe:")
    ht.put("line_3", "All mimsy were the borogoves,")
    ht.put("line_4", "And the mome raths outgrabe.")
    ht.put("line_5", '"Beware the Jabberwock, my son!')
    ht.put("line_6", "The jaws that bite, the claws that catch!")
    ht.put("line_7", "Beware the Jubjub bird, and shun")
    ht.put("line_8", 'The frumious Bandersnatch!"')
    ht.put("line_9", "He took his vorpal sword in hand;")
    ht.put("line_10", "Long time the manxome foe he sought--")
    ht.put("line_11", "So rested he by the Tumtum tree")
    ht.put("line_12", "And stood awhile in thought.")

    print("")

    # Test storing beyond capacity
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    # # Test resizing
    # old_capacity = ht.get_num_slots()
    # ht.resize(ht.capacity * 2)
    # new_capacity = ht.get_num_slots()

    # print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # # Test if data intact after resizing
    # for i in range(1, 13):
    #     print(ht.get(f"line_{i}"))

    print("")
