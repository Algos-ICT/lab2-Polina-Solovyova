f = open('/Users/Guest/Documents/input.txt', 'r')
n = f.readline()
n = int(n)
nums = f.readline()
nums = list(map(int, nums.split()))
ind = [nums[0]]
x = open('/Users/Guest/Documents/output.txt', 'w')
       
def insertion_sort(nums):
    for i in range(1, n):
        if abs(nums[i]) <= 10 ** 9:
            item_to_insert = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > item_to_insert:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = item_to_insert
            ind.append(j + 2)
        else:
            x = open('/Users/Guest/Documents/output.txt', 'w')
            x.write('ошибка')
            exit()
        
if n >= 1 and n <= 10 ** 3:
    insertion_sort(nums)
    indexes = ' '.join(str(k) for k in ind)
    out = ' '.join(str(e) for e in nums)
    x.write(indexes)
    x.write('\n')
    x.write(out)
else:
    x = open('/Users/Guest/Documents/output.txt', 'w')
    x.write('ошибка')

f.close()
x.close()
