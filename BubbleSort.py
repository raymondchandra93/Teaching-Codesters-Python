def create_list():
    nums = []
    for i in range(10):
        nums.append( random.randint(-1000,1000) )
    return nums

def swap(l, i1, i2):
    temp = l[i1]
    l[i1] = l[i2]
    l[i2] = temp

def bubble_sort(l):
    for i in range(1, len(l)):
        for j in range(0, len(l)-i):
            if l[j] > l[j+1]:
                swap(l, j, j+1)

l = create_list()
print(l)
bubble_sort(l)
print(l)
