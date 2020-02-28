from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    # Adds a new item
    def append(self, item):
        # Adds a completly new item to the storage if there's room.
        if self.storage.length < self.capacity:
            self.storage.add_to_tail(item)
            self.current = self.storage.tail # Sets current to the newest node

        # Replaces the oldest item with the new item
        else:
            if self.current == self.storage.tail:
                self.current = self.storage.head # Sets current to the oldest value

            else:
                self.current = self.current.next # Go to the next node

            self.current.value = item

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        current_node = self.storage.head

        # Loop through the entire storage while adding values to list_bugger_contents
        while current_node:
            list_buffer_contents.append(current_node.value)
            current_node = current_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
