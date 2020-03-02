#!/home/student/.pyenv/shims/python
# task2

list1 = input().split(" ")
list2 = input().split(" ")
out = []
res = ""

for el in set(list1).intersection(set(list2)):
    out.append(int(el))

out.sort()

# Put elements into a single string
for i in out:
    res += str(i) + ' '

print(res)
