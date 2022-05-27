# Find The Repeating And The Missing Elements
def printTwoElements( arr, size):
	for i in range(size):#Repeating Element Logic
		if arr[abs(arr[i])-1] > 0:
			arr[abs(arr[i])-1] = -arr[abs(arr[i])-1]
		else:
			print("The repeating element is ", abs(arr[i]))
			
	for i in range(size):
		if arr[i]>0:#Missing Element Logic
			print("and the missing element is ", i + 1)

# Driver program..
arr = [1,2,4,4,5,6,7,9,8,7]
n = len(arr)
printTwoElements(arr, n)
