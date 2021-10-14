f = open('/Users/Guest/Documents/input.txt', 'r')
n = f.readline()
n = int(n)
nums = f.readline()
nums = list(map(int, nums.split()))
x = open('/Users/Guest/Documents/output.txt', 'w')

def insertion_bubble(A: list):
       for j in range(0, n):
              for i in range(0, n - 1):
                     if A[i] > A[i + 1]:
                            A[i + 1], A[i] = A[i], A[i + 1]
       return A

if n <= 1 and n >= 10 ** 3:
       x.write('ошибка')
       for i in nums:
              if abs(i) >= 10 ** 9:
                    x.write('ошибка')
else:
       insertion_bubble(nums)
       out = ' '.join(str(e) for e in nums)
       x.write(out)

f.close()
x.close()

