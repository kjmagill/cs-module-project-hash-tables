import math

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
        self.storage = [None for i in range(capacity)]
        self.load = 0


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list)
        """
        # the number of slots in the hash table is represented by its capacity
        return self.capacity


    def get_load_factor(self):
        """
        Return the load factor for this hash table.
        """
        # the hash table's load factor is its load divided by its capacity
        return self.load / self.capacity


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
        within the storage capacity of the hash table.
        """
        # return self.fnv1(key) % self.capacity
        return self.djb2(key) % self.capacity


    def put(self, key, value):
        """
        Store the value with the given key.
        Hash collisions should be handled with Linked List Chaining.
        """
        i = self.hash_index(key)
        # if the slot at the specified index is empty (self.storage[i] doesn't exist)
        # create a linked list in this slot and increment the table's load by 1
        if not self.storage[i]:
            self.storage[i] = HashTableEntry(key, value)
            self.load += 1
        # otherwise, if a linked list already exists at the specified index
        else:
            current = self.storage[i]
            # move to the next entry if both: the input key doesn't match the current
            # entry's key and a next entry does exist
            while current.key != key and current.next:
                current = current.next

            # if we find the entry (the input key matches the current entry's key)
            # update the current value to the input value
            if current.key == key:
                current.value = value
            # otherwise, if we hit the end of the list without finding the entry
            # create a linked list in this slot and increment the table's load by 1
            else:
                current.next = HashTableEntry(key, value)
                self.load += 1

        # if the hash table's current load factor is greater than 0.7
        # resize it to double the capacity
        if self.get_load_factor() > 0.7:
            self.resize(self.capacity * 2)


    def delete(self, key):
        """
        Remove the value stored with the given key.
        Print a warning if the key is not found.
        """
        i = self.hash_index(key)
        current = self.storage[i]

        # if the slot at the specified index is empty, print an error message
        if not current:
            print('Error: there is no entry in the hash table with that key')
        # if the current entry is the head of the list (meaning it has no next entry)
        # set the current entry's value to None and decrement the table's load by 1
        elif not current.next:
            self.storage[i] = None
            self.load -= 1
        # otherwise, 
        else:
            # create a pointer for the current entry's previous entry
            previous = None
            # move to the next entry if both: the input key doesn't match the current
            # entry's key and a next entry does exist
            while current.key != key and current.next:
                previous, current = current, current.next
            # if the current entry is at the end of the list
            if not current.next:
                previous.next = None
                self.load -= 1
            # otherwise, if the current entry is somewhere in the middle of the list
            else:
                previous.next = current.next
                self.load -= 1

        # if the hash table's current load factor is less than 0.2
        # reduce the table's capacity by half
        # if the new capacity is less than 8, set the capacity to 8 (our minimum)
        if self.get_load_factor() < 0.2:
            if math.ceil(self.capacity / 2) < 8:
                self.resize(8)
            else:
                self.resize(math.ceil(self.capacity / 2))


    def get(self, key):
        """
        Retrieve the value stored with the given key.
        Returns None if the key is not found.
        """
        i = self.hash_index(key)
        current = self.storage[i]
        # if an entry exists at the specified index, return its value
        if current:
            return current.value
        # otherwise, return None
        else: 
            return None


    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and rehashes all key/value pairs.
        """
        # create a new hash table with the new input capacity
        new_table = HashTable(new_capacity)
        # check each slot in the current hash table and store it
        # in the new table if it is not None
        for entry in self.storage:
            current = entry
            while current:
                new_table.put(current.key, current.value)
                current = current.next
        # lastly, overwrite the current hash table with the new one
        self.capacity = new_table.capacity
        self.load = new_table.load
        self.storage = new_table.storage


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

    # Test resizing
    old_capacity = ht.get_num_slots()
    ht.resize(ht.capacity * 2)
    new_capacity = ht.get_num_slots()

    print(f"\nResized from {old_capacity} to {new_capacity}.\n")

    # Test if data intact after resizing
    for i in range(1, 13):
        print(ht.get(f"line_{i}"))

    print("")
