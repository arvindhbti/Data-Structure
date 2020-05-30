def insertionsort(arr):
	for j in range(1,len(arr)):
		key=arr[j]
		i=j-1
		while i>=0 and arr[i]>key:
			arr[i+1]=arr[i]
			i=i-1
		arr[i+1]=key
        
arr=[1,10,2,20,5]

insertionsort(arr)
print(arr)