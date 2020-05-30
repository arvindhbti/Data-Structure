def bubbleSort(arr):
	iter=len(arr)
	for i in range(iter):
		for j in range(0,iter-i-1):
			if arr[j]>arr[j+1]:
				arr[j],arr[j+1]=arr[j+1],arr[j]
			else :
				pass
  
# Driver code to test above 
arr = [60, 30, 20, 10, 22, 11, 90] 
  
bubbleSort(arr) 
  
print ("Sorted array is:") 
for i in range(len(arr)): 
    print ("%d" %arr[i]),