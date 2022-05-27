
# The Maximum Water That Can Be Stored
def maxWater(arr, n) :
	res = 0;
	# For Every Element Of The array
	for i in range(1, n - 1):
		# Find The Maximum Element On Its Left
		left = arr[i];
		for j in range(i) :
			left = max(left, arr[j]);
		# Find The Maximum Element On Its Right
		right = arr[i];
		for j in range(i + 1 , n) :
			right = max(right, arr[j]);	
		# Update The Maximum Water
		res = res + (min(left, right) - arr[i]);
	return res;
# Driver code
if __name__ == "__main__" :

	arr = [0,2,2,1,0,2,1,1];
	n = len(arr);
	
	print(maxWater(arr, n));
	

