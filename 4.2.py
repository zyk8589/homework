def three_way_quick_sort(arr, low=0, high=None):
    
    if high is None:
        high = len(arr) - 1
    
    if low < high:
       
        random_index = random.randint(low, high)
        arr[random_index], arr[low] = arr[low], arr[random_index]
        pivot = arr[low]
        
       
        lt = low      
        gt = high     
        i = low + 1
        
        while i <= gt:
            if arr[i] < pivot:
                
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1
                i += 1
            elif arr[i] > pivot:
               
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
               
            else:
            
                i += 1
      
        three_way_quick_sort(arr, low, lt - 1)
        three_way_quick_sort(arr, gt + 1, high)
    
    return arr