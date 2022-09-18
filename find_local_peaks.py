
# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
# A comapny lots of time-series data.  Here is some represented by an array of integers, where the index indicates the time point (eg: minute 0 => value is 8):
# Please find the local peak for the array. 
# [ 8, 9, 10, 11, 12, 10, 9, 8, 7, 8, 6 ]
#.                lp               lp


def getLocalPeak(arr):
    out_lp = []
    
    arr_len = len(arr)
    
    if arr_len <= 1:
        return out_lp
        
    for i in range(arr_len):
        if i == 1 and arr[i]  > arr[i + 1]:
            out_lp.append(arr[i])
        if i == arr_len -1 and arr[i] > arr[i-1]:
            out_lp.append(arr[i])
        if i > 1 and i < arr_len -1 and arr[i-1] < arr[i] > arr[i+1]:
            out_lp.append(arr[i])
            
    return out_lp
    
inp =  [ 8, 9, 10, 11, 12, 10, 9, 8, 7, 8, 6 ]

print(getLocalPeak(inp))