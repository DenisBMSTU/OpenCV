dct = {288: 'e', 323: 'e', 228: '[', 261: 'f', 134: 'o', 103: 'c', 359: 'd', 13: 'v', 175: 'm', 49: 'k'}
arr = dct.keys()
arr.sort()
print arr
print dct
arr2 = []
for i in range(0, len(arr)):
	if arr[i] in dct:
		arr2.append(dct[arr[i]])
print arr2
