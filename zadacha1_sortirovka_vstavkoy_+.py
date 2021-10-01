f = open('/Users/Guest/Documents/input.txt', 'r')
a = f.readline()
a = int(a)
nums = f.readline()
nums = list(map(int, nums.split()))
ind = [nums[0]]
       
def insertion_sort(nums):
    for i in range(1, a):
        item_to_insert = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > item_to_insert:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = item_to_insert
        ind.append(j + 2)
        
insertion_sort(nums)
indexes = ' '.join(str(k) for k in ind)
out = ' '.join(str(e) for e in nums)
x = open('/Users/Guest/Documents/output.txt', 'w')
x.write(indexes)
x.write('\n')
x.write(out)
f.close()
x.close()

