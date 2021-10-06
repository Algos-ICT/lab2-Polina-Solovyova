f = open('/Users/Guest/Documents/input.txt', 'r')
n = f.readline()
n = int(n)
nums = f.readline()
nums = list(map(int, nums.split()))
x = open('/Users/Guest/Documents/output.txt', 'w')

def insertion_sort(nums):
    for i in range(1, n):
        item_to_insert = nums[i]
        j = i - 1
        if abs(nums[i]) <= 10 ** 9:
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = item_to_insert
        else:
            x.write('ошибка')
            exit()
    

if n >= 1 and n <= 10 ** 3:
    insertion_sort(nums)
    out = sorted(nums, reverse=True)
    out = ' '.join(str(e) for e in nums)
    x.write(out)
else:
    x.write('ошибка')
    
x.close()
f.close()
