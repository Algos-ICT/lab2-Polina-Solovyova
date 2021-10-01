f = open('/Users/Guest/Documents/input.txt', 'r')
a = f.readline()
a = int(a)
nums = f.readline()
nums = list(map(int, nums.split()))
       
def insertion_bubble(A: list):
    for j in range(0, a):
        for i in range(0, a - 1):
            if A[i] > A[i + 1]:
                A[i + 1], A[i] = A[i], A[i + 1]
    return A
        
insertion_bubble(nums)
out = ' '.join(str(e) for e in nums)
x = open('/Users/Guest/Documents/output.txt', 'w')
x.write(out)
f.close()
x.close()

