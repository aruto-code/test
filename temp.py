# str ='apple mango apple orange orange apple guava mango mango'

# lst = str.split(" ")

# dict = {}

# for e in lst:
#     if e in dict:
#         dict[e] = dict[e] + 1
#     else:
#         dict[e] = 1

# print(dict)


n = 2
nums = 30

count = 0
for i in range(1,nums+1):
    temp = str(i)
    lst = [int(a) for a in str(i)]
    for e in lst:
        if(e == n):
            count = count + 1

print(count)
