f = open('/Users/software/Documents/input.txt', 'r')
arr = f.readline()
arr = list(map(int, arr.split()))
ind = []

def LinearSearch(arr, element):
    for i in range (len(arr)):
        if arr[i] == element:
            ind.append(i)       
    return 'ашыбка э'
LinearSearch(arr, 1)
out = ' '.join(str(e) for e in ind)
a = open('/Users/software/Documents/output.txt', 'w')
a.write(out)
f.close()
a.close()
