list1 = [1,2,3,4]

## m 은 map object 를 리턴
m = map(lambda x: x * 3, list1)

list2 = list(m)

print(list1)
print(list2)