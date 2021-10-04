f = open('/Users/Guest/Documents/input.txt', 'r')
arr = f.readline()
arr = list(map(int, arr.split()))
v = f.readline()
v = int(v)
ind = []

def LinearSearch(arr, element):
    if abs(element) <= 10 ** 3:
        for i in range (len(arr)):
            if len(arr) >= 0 and len(arr) <= 10 ** 3:
                if arr[i] == element:
                    ind.append(i)
            else:
                print('ошибка')
        return -1
    else:
        print('ошибка')
    
LinearSearch(arr, v)
out = ' '.join(str(e) for e in ind)
a = open('/Users/Guest/Documents/output.txt', 'w')
a.write(out)
f.close()
a.close()
