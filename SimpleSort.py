def create_list():
    nums = []
    for i in range(10):
        nums.append( random.randint(-1000, 1000) )
    return nums

myList = create_list()
print(myList)

def swap(list, i1, i2):

    temp = list[i1]
    list[i1] = list[i2]
    list[i2] = temp

def simple_sort(list):

    for i in range( len(list) ):
        # min = red arrow
        min = i

        # j = blue arrow
        for j in range( i, len(list) ):
            if list[j] < list[min]:
                min = j

        swap(list, min, i)

simple_sort(myList)
print(myList)
