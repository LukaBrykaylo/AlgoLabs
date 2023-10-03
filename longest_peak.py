def longest_peak(arr):
    final_number = 0
    current_number = 0
    high_to_low = False
    from_low_to_high = False
    possible_start_pos = 0
    arr_length = len(arr)
    for i in range(1, arr_length):
        if arr[i] > arr[i-1]:
            if current_number == 0:
                current_number = current_number + 1
                from_low_to_high = True
            current_number = current_number + 1
        else:
            if arr_length - 1 > i:
                if arr[i+1] > arr[i]:
                    high_to_low = True
                    possible_start_pos = i
            else:
                high_to_low = True
            current_number = current_number + 1
            if current_number >= 3 and current_number > final_number and high_to_low == True and from_low_to_high == True:
                final_number = current_number
                current_number = 0
                high_to_low = False
                if possible_start_pos != 0:
                    possible_start_pos = 0
                    current_number = 1
    return final_number
