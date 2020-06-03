class HashTableEntry:
    """
    Linked List hash table key/value pair
    """
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

    def __str__(self):
      return self.value



# Hash table can't have fewer than this many slots
MIN_CAPACITY = 8


class HashTable:
    """
    A hash table that with `capacity` buckets
    that accepts string keys

    Implement this.
    """

    def __init__(self, capacity = MIN_CAPACITY):
        self.buckets = [None] * capacity
        self.capacity = capacity


    def get_num_slots(self):
        """
        Return the length of the list you're using to hold the hash
        table data. (Not the number of items stored in the hash table,
        but the number of slots in the main list.)

        One of the tests relies on this.

        Implement this.
        """
        return len(self.buckets)


    def get_load_factor(self):
        """
        Return the load factor for this hash table.

        Implement this.
        """
        # Your code here


    def fnv1(self, key):
        """
        FNV-1 Hash, 64-bit

        Implement this, and/or DJB2.
        """
        # https://en.wikipedia.org/wiki/Fowler%E2%80%93Noll%E2%80%93Vo_hash_function#FNV-1_hash
        FNV_offset_basis = 14695981039346656037
        FNV_prime = 1099511628211
        
        hash = FNV_offset_basis

        for byte in key.encode():
          hash = hash * FNV_prime
          hash = hash ^ byte
        
        return hash

    def hash_index(self, key, capacity):
        return self.get_key_slot(key, capacity)

    def put(self, key, value):
        """
        Store the value with the given key.

        Hash collisions should be handled with Linked List Chaining.

        Implement this.
        """
        self.put_in_buckets(key, value, self.buckets, self.capacity)
        
    def delete(self, key):
        """
        Remove the value stored with the given key.

        Print a warning if the key is not found.

        Implement this.
        """
        self.put(key, None)

    def get(self, key):
      """
      Retrieve the value stored with the given key.

      Returns None if the key is not found.

      Implement this.
      """
      slot_num = self.get_key_slot(key, self.capacity)
      top_level_item = self.buckets[slot_num]
      
      if top_level_item == None:
        return None
      else:
        cur_item = top_level_item
        while cur_item:
          if cur_item.key == key:
            return cur_item.value
          cur_item = cur_item.next
        
        return None
        
    def resize(self, new_capacity):
        """
        Changes the capacity of the hash table and
        rehashes all key/value pairs.

        Implement this.
        """
        
        new_buckets = [None] * new_capacity

        for item in self.buckets:
          self.put_in_buckets(item.key, item.value, new_buckets, new_capacity, True)
          item = item.next
          while item:
            self.put_in_buckets(item.key, item.value, new_buckets, new_capacity, True)
            item = item.next
            
        self.buckets = new_buckets
        self.capacity = new_capacity

    def get_key_slot(self, key, capacity):
        return self.fnv1(key) % capacity

    def get_item_count(self):
      num_items = 0

      for item in self.buckets:
        if item != None:
          num_items += 1
          cur_item = item
          while cur_item:
            if cur_item.next:
              num_items += 1
            cur_item = cur_item.next

      return num_items

    def needs_resize(self):
      item_count = self.get_item_count()
      if item_count == 0:
        return False
      
      if (item_count / len(self.buckets)) >= 0.7:
        return True
      return False

    def put_in_buckets(self, key, value, buckets, capacity, no_resize_check = True):

      is_delete_operation = False
      if value == None:
        is_delete_operation = True

      if no_resize_check == False:
        if is_delete_operation == False:
          if self.needs_resize():
            self.resize(self.capacity * 2)
      
      item = HashTableEntry(key, value)
      slot_num = self.get_key_slot(key, capacity)
      top_level_item = buckets[slot_num]
      
      if top_level_item == None or top_level_item.key == key:
        if is_delete_operation:
          if top_level_item.next:
            buckets[slot_num] = top_level_item.next
          else:
            buckets[slot_num] = None
        else:
          buckets[slot_num] = item
      
      else:
        prev_item = None
        cur_item = top_level_item
        next_item = cur_item.next
        
        while cur_item:
          if cur_item.key == key:    # key is present #
            if is_delete_operation:
              prev_item.next = next_item
            else:
              cur_item.value = value
            break
          
          elif not next_item:
            cur_item.next = item
            break
          
          prev_item = cur_item
          cur_item = next_item
          next_item = cur_item.next

if __name__ == "__main__":

    ht = HashTable(8)

    ht.put("line_1", "'Twas brillig, and the slithy toves")
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