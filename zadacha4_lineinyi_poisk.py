f = open('/Users/Guest/Documents/input.txt', 'r')
arr = f.readline()
arr = list(map(int, arr.split()))
v = f.readline()
v = int(v)
ind = []
a = open('/Users/Guest/Documents/output.txt', 'w')

def LinearSearch(arr, element):
    if abs(element) <= 10 ** 3:
        for i in range (len(arr)):
            if arr[i] == element:
                ind.append(i)
        return -1
    else:
        x.write('ошибка')
        exit()
            
if len(arr) >= 1 and len(arr) <= 10 ** 3:
    LinearSearch(arr, v)
    out = ' '.join(str(e) for e in ind)
    a.write(out)
else:
    x.write('ошибка')
    
f.close()
a.close()
