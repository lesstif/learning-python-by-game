l1 = [1,2,3,4]

## m 은 map object 를 리턴
m = map(lambda x: x * 3, l1)

l2 = list(m)

print(l1)
print(l2)