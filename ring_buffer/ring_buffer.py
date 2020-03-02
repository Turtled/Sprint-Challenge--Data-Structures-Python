from doubly_linked_list import DoublyLinkedList


class RingBuffer:

    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()
        for i in range(0, capacity):
            self.storage.add_to_tail(None)
        self.storage.tail.next = self.storage.head
        self.storage.head.prev = self.storage.tail

        #basically index 0, read_node will be the start of the ring, where we always start reading from
        self.read_node = self.storage.head

        #current index we're overwriting, this will loop around the ring
        self.write_node = self.storage.head

    def append(self, item):
        self.write_node.value = item
        self.write_node = self.write_node.next


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        next_node = self.read_node
        for i in range(0, self.capacity):
            if(next_node.value is not None):
                list_buffer_contents.append(next_node.value)
                next_node = next_node.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass
