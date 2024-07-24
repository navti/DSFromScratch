# General heap implementation in python
# Heaps are implemented as binary trees
# The root or parent is always smaller or larger than its children depending on what
# kind of the heap it is.

class CustomHeap:
    def __init__(self, arr: list[int] = None, mode: int = 1):
        # mode: 0 -> min heap, 1 -> max heap (default)
        self.__mode = mode
        self.__items = []
        self.__size = 0
        self.__root_idx = 0
        # if arr is given, build heap using arr
        if arr:
            self.__items = [*arr]
            self.__size = len(self.__items)
            for idx in range(self.__size-1, -1, -1):
                # use sift down to build heap in O(n) time.
                self.__sift_down(idx)
   
    def __repr__(self):
        mode = "max heap" if self.__mode else "min heap"
        return f'Heap type: {mode}\nHeap size: {self.__size}\nHeap items:{self.__items[:self.__size]}'

    def __len__(self):
        return self.__size
    
    # bubble up until heap property is restored
    def __sift_up(self, tidx):
         while (tidx-1)//2 >= self.__root_idx:
            pidx = (tidx-1)//2
            if self.__mode and self.__items[pidx] < self.__items[tidx]:
                self.__items[pidx], self.__items[tidx] = self.__items[tidx], self.__items[pidx]
                tidx = pidx
            elif not self.__mode and self.__items[pidx] > self.__items[tidx]:
                self.__items[pidx], self.__items[tidx] = self.__items[tidx], self.__items[pidx]
                tidx = pidx
            else:
                break
    
    # bubble down until heap property is restored
    def __sift_down(self, tidx):
        while 2*tidx + 1 < self.__size:
            max_child_idx = self.__max_child(tidx)
            min_child_idx = self.__min_child(tidx)
            if self.__mode and self.__items[max_child_idx] > self.__items[tidx]:
                self.__items[max_child_idx], self.__items[tidx] = self.__items[tidx], self.__items[max_child_idx]
                tidx = max_child_idx
            elif not self.__mode and self.__items[min_child_idx] < self.__items[tidx]:
                self.__items[min_child_idx], self.__items[tidx] = self.__items[tidx], self.__items[min_child_idx]
                tidx = min_child_idx
            else:
                break
    
    # return index of max child
    def __max_child(self, pidx):
        if 2*pidx + 2 < self.__size and self.__items[2*pidx+2] > self.__items[2*pidx+1]:
            return 2*pidx + 2
        else:
            return 2*pidx+1 if 2*pidx+1 < self.__size else pidx

    # return index of min child
    def __min_child(self, pidx):
        if 2*pidx + 2 < self.__size and self.__items[2*pidx+2] < self.__items[2*pidx+1]:
            return 2*pidx + 2
        else:
            return 2*pidx+1 if 2*pidx+1 < self.__size else pidx

    # push new key, put it at the end of the array and then sift up
    # to restore heap property
    def push(self, key):
        if self.__size < len(self.__items):
            self.__items[self.__size] = key
        else:
            self.__items.append(key)
        self.__size += 1
        self.__sift_up(self.__size-1)
    
    # replace root with last element in the array and then sift down
    # to restore heap property
    def pop(self):
        pop_item = self.__items[self.__root_idx]
        self.__items[self.__root_idx] = self.__items[self.__size-1]
        self.__size -= 1
        self.__sift_down(self.__root_idx)
        return pop_item
    
    def top(self):
        return self.__items[self.__root_idx]

    # change heap type
    def set_mode(self, m):
        self.__mode = m
        #self.__items = [*self.__items[:self.__size]]
        for idx in range(self.__size-1, -1, -1):
            self.__sift_down(idx)

if __name__ == '__main__':
    heap = CustomHeap(range(10))
    print(heap)
    print(f'length: {len(heap)}')
    print(f'top: {heap.top()}')
    heap.push(15)
    print(f'push: 15')
    print(f'length: {len(heap)}')
    heap.push(17)
    print(f'push: 17')
    print(f'length: {len(heap)}')
    print(f'top: {heap.top()}')
    print(f'pop: {heap.pop()}')
    print(f'length: {len(heap)}')
    print(f'pop: {heap.pop()}')
    print(f'length: {len(heap)}')
    heap.set_mode(0)
    print(f'Set heap type: min')
    print(heap)

