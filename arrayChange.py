def arrayChange(a):
    # Iterate through array
    # If not a[i+1] > a[i] then find unsigned difference b/w them + 1
    # Store it as ans, and replace a[i] with a[i]  + above generated val
    result = 0
    for i in range(0, len(a) - 1):
        if not a[i+1] > a[i]:
            diff  = abs(a[i+1] - a[i]) + 1
            print(diff)
            result += diff
            a[i+1] =a[i+1] + diff
    return result



print(arrayChange([1,1,1]))