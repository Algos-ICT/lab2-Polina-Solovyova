f = open('/Users/Guest/Documents/input.txt', 'r')
n = f.readline()
n = int(n)
nums = f.readline()
nums = list(map(int, nums.split()))
       
def insertion_bubble(A: list):
    if n >= 1 and n <= 10 ** 3:
        for j in range(0, n):
            for i in range(0, n - 1):
                if abs(nums[i]) <= 10 ** 9:
                    if A[i] > A[i + 1]:
                        A[i + 1], A[i] = A[i], A[i + 1]
                else:
                    print('ошибка')
        return A
    else:
        print('ошибка')
        
insertion_bubble(nums)
out = ' '.join(str(e) for e in nums)
x = open('/Users/Guest/Documents/output.txt', 'w')
x.write(out)
f.close()
x.close()

