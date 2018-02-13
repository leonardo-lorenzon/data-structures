# Class for a heap base on max element unlike a minimum element like heapq Class in python
class HeapMax():
    def __init__(self):
        self.heap = []

    # Method for sort a array using heap in O(n log n)
    # Given an unsorted array its return a sorted array
    def heap_sort(self, arr):
        self.heap = []
        for i in arr:
            self.insert(i)
        for j in range(len(arr) - 1, -1, -1):
            arr[j] = self.extract_max()

        return arr

    # Turn a array into a heap
    def build_heap(self, arr):
        self.heap = arr
        for i in range(len(arr) - 1, -1, -1):
            self.sift_down(i)
        return self.heap

    # Get the max element without remove them
    def get_max(self):
        return self.heap[0]

    # return the parent position
    def parent(self, position):
        return (position - 1) // 2
    # return the left child
    def left_child(self, position):
        return 2 * position + 1
    # return the right child
    def righ_child(self, position):
        return 2 * position + 2

    # swap the problematic node with its parent until the property is satisfied
    def sift_up(self, position):
        while(position > 0 and self.heap[self.parent(position)] < self.heap[position]):
            self.heap[self.parent(position)], self.heap[position] = self.heap[position], self.heap[self.parent(position)]
            position = self.parent(position)

    # swap the problematic node with larger child until heap property is satisfied
    def sift_down(self, position):
        max_index = position
        left = self.left_child(position)
        right = self.righ_child(position)
        size = len(self.heap)
        if left < size:
            if(self.heap[left] > self.heap[max_index]):
                max_index = left
        if right < size:
            if(self.heap[right] > self.heap[max_index]):
                max_index = right

        if position != max_index:
            self.heap[position], self.heap[max_index] = self.heap[max_index], self.heap[position]
            self.sift_down(max_index)

    # insert a new element into the heap
    def insert(self, element):
        self.heap.append(element)
        self.sift_up(len(self.heap) - 1)


    # Extract the maximum element and replace the root with the last leaf
    def extract_max(self):
        max_element = self.heap[0]
        if len(self.heap) > 1:
            self.heap[0] = self.heap.pop()
            self.sift_down(0)
        return max_element

    # change the priority of an element and let the changed element sift up or down
    def change_priority(self, position, new_element):
        if (position < len(self.heap)):
            old_element = self.heap[position]
            self.heap[position] = new_element
            if (new_element > old_element):
                self.sift_up(position)
            else:
                self.sift_down(position)
        else:
            print('Index out of range. Impossible change priority.')

    # remove an element. Needed position of this element
    def remove(self, position):
        if (position < len(self.heap)):
            self.heap[position] = float('inf') #change the priority to infinit
            self.sift_up(position)
            self.extract_max()
        else:
            print('Index out of range. Impossible remove.')


# tests
h = HeapMax()
h.insert(74)
h.insert(9)
h.insert(1)
h.insert(98)
h.insert(167)
h.insert(8)
h.insert(75)
h.insert(4)
h.insert(10987)
print(h.heap)
print(h.get_max())

h.extract_max()
print(h.heap)

h.remove(1)
print(h.heap)

h.change_priority(2, 7)
print(h.heap)

arr = h.heap_sort([3,2,1,5,34,3,23,2,3,4,5,6,77,5,443,3,5342,535])
print(arr)
new_heap = [1,3,5,3,2,2,45,3,3,5,3,22]
HeapMax().build_heap(new_heap)
print(new_heap)