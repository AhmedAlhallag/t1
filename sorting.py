class Sorting:
    def __init__(self):
        self.nums = None

    def set_list(self, nums):
        self.nums = nums

    def bubble_sort(self):
        for i in range(len(self.nums)):
            swap = False
            for j in range(len(self.nums)-i-1):
                if self.nums[j] > self.nums[j+1]:
                    temp = self.nums[j]
                    self.nums[j] = self.nums[j+1]
                    self.nums[j+1] = temp
                    swap = True
            if not swap:
                break

    def get_nums(self):
        return self.nums


# sort = Sorting()

# nums = [10, 20, 3, -1]
# sort.set_list(nums)
# sort.bubble_sort()
# print(sort.get_nums())
