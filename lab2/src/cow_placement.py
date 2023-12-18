def cow_placement(n, c, free_sections): 
    if n < 2: 
        return 0 
    elif n < c: 
        return 0 
 
    free_sections = sorted(free_sections) 
    left = 0 
    right = free_sections[-1] - free_sections[0] 
    while left <= right: 
        mid = (left + right) // 2 
        number = 1 
        last_position = free_sections[0] 
 
        for i in range(1, len(free_sections)): 
            if free_sections[i] - last_position >= mid: 
                number += 1 
                last_position = free_sections[i] 
 
        if number >= c: 
            left = mid + 1 
        else: 
            right = mid - 1 
 
    return right
