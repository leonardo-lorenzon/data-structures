# Class for a heap base on maximum element unlike a minimum element like heapq Class in python
class HeapMax():

    # Method for sort a array using heap in O(n log n)
    # Given an unsorted array its return a sorted array
    def heap_sort(self, arr):
        sorted_arr = [0 for i in range(len(arr))]
        self.build_heap(arr)
        for j in range(len(arr) - 1, -1, -1):
            sorted_arr[j] = self.extract_max(arr)
        return sorted_arr

    # Turn a array into a heap
    def build_heap(self, arr):
        for i in range((len(arr) - 1) // 2, -1, -1):
            self.sift_down(i, arr)

    # Get the max element without remove them
    def get_max(heap):
        return heap[0]

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
    def sift_up(self, position, arr):
        while(position > 0 and arr[self.parent(position)] < arr[position]):
            arr[self.parent(position)], arr[position] = arr[position], arr[self.parent(position)]
            position = self.parent(position)

    # swap the problematic node with larger child until heap property is satisfied
    def sift_down(self, position, arr):
        max_index = position
        left = self.left_child(position)
        right = self.righ_child(position)
        size = len(arr)
        if left < size:
            if(arr[left] > arr[max_index]):
                max_index = left
        if right < size:
            if(arr[right] > arr[max_index]):
                max_index = right

        if position != max_index:
            arr[position], arr[max_index] = arr[max_index], arr[position]
            self.sift_down(max_index, arr)

    # insert a new element into the heap. Must be a heap for work
    def insert(self, element, heap):
        heap.append(element)
        self.sift_up(len(heap) - 1, heap)


    # Extract the maximum element and replace the root with the last leaf
    def extract_max(self, heap):
        max_element = heap[0]
        if len(heap) > 1:
            heap[0] = heap.pop()
            self.sift_down(0, heap)
        return max_element

    # change the priority of an element. Needed a position of element, the new value and the heap.
    def change_priority(self, position, new_element, heap):
        if (position < len(heap)):
            old_element = heap[position]
            heap[position] = new_element
            if (new_element > old_element):
                self.sift_up(position, heap)
            else:
                self.sift_down(position, heap)
        else:
            print('Index out of range. Impossible change priority.')

    # remove an element. Needed position of element and the heap
    def remove(self, position, heap):
        if (position < len(heap)):
            heap[position] = float('inf') #change the priority to infinit
            self.sift_up(position, heap)
            self.extract_max(heap)
        else:
            print('Index out of range. Impossible remove.')


# tests

new_heap = [1,57,5,3,2,2,45,9,30,5,39,22]
HeapMax().build_heap(new_heap)
print(new_heap)

HeapMax().insert(21, new_heap)
print(new_heap)

HeapMax().change_priority(12, 23, new_heap)
print(new_heap)

HeapMax().remove(5, new_heap)
print(new_heap)

max_e = HeapMax().extract_max(new_heap)
print(max_e)
print(new_heap)

any_arr = [4,5,79,7,34,5,3,1,4,5,65,7,67]
arr_sorted = HeapMax().heap_sort(any_arr)
print(arr_sorted)

