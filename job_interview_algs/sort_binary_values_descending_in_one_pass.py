def bin_sort(binary_list=None):
if not binary_list:
return list()

start = 0
end = len(binary_list) - 1

while start < end:
if binary_list[start] == 0 and binary_list[end] == 1:
binary_list[start] = 1
binary_list[end] = 0
start += 1
end -= 1
continue
elif binary_list[start] == 0 and binary_list[end] == 0:
end -= 1
continue
elif binary_list[start] == 1 and binary_list[end] == 1:
start += 1
else:
start += 1
end -= 1

return binary_list


if _name_ == '__main__':
b_list = [0, 1, 1, 0, 0, 0, 1, 1, 0]
print(bin_sort(b_list))
