
def brute_force(arr):       # O(n^2)
    i = 0
    global_max = arr[i]
    while i < len(arr):
        j = i
        local_max = 1
        while j < len(arr):
            local_max *= arr[j]
            if local_max > global_max:
                global_max = local_max
            j += 1
        i += 1
    return global_max


def incremental(arr):       # O(n)
    max_at = arr[0]
    min_at = arr[0]
    max_value = max_at
    i = 1
    while i < len(arr):
        prev_max_at = max_at
        prev_min_at = min_at
        max_at = max(arr[i], arr[i]*prev_max_at, arr[i]*prev_min_at)
        min_at = min(arr[i], arr[i]*prev_max_at, arr[i]*prev_min_at)
        max_value = max(max_value, max_at)
        i += 1
    return max_value


def rec_incremental(arr):       # O(n)
    if len(arr) == 1:
        return arr[0], arr[0], arr[0]

    previous = rec_incremental(arr[:-1])
    prev_max_at = previous[0]
    prev_min_at = previous[1]
    last_element = arr[-1]
    
    max_at = max(last_element, last_element*prev_max_at, last_element*prev_min_at)
    min_at = min(last_element, last_element*prev_max_at, last_element*prev_min_at)
    max_value = max(previous[2], max_at)

    return max_at, min_at, max_value


def dumb_rec_incremental(arr):      # O(n)
    if len(arr) == 1:
        return arr[0], arr[0]

    previous = dumb_rec_incremental(arr[:-1])
    prev_max_at = previous[0]
    last_element = arr[-1]
    
    max_at = max(last_element, last_element*prev_max_at)
    max_value = max(previous[1], max_at)

    return max_at, max_value


def div_n_conq(arr, max_at, min_at, max_value):     # O(n)
    if len(arr) == 1:
        prev_max_at = max_at
        prev_min_at = min_at
        max_at = max(arr[0], arr[0]*prev_max_at, arr[0]*prev_min_at)
        min_at = min(arr[0], arr[0]*prev_max_at, arr[0]*prev_min_at)
        max_value = max(max_value, max_at)        
        return max_at, min_at, max_value
    
    mid = len(arr)//2

    left = div_n_conq(arr[:mid], max_at, min_at, max_value)
    right = div_n_conq(arr[mid:], left[0], left[1], left[2])
    
    return right[0], right[1], right[2]


def rec_with_index(arr):
    if len(arr) == 1:
        start = 0
        stop = 0
        return arr[0], arr[0], start, stop

    previous = rec_with_index(arr[:-1])
    prev_max_at = previous[0]
    start = previous[2]
    stop = previous[3]
    last_element = arr[-1]
    
    max_at = max(last_element, last_element*prev_max_at)
    if max_at == last_element:
        start = len(arr)-1

    max_value = max(previous[1], max_at)
    if max_value == max_at:
        stop = len(arr)-1

    return max_at, max_value, start, stop


def div_n_conq_indexes(arr, max_at, min_at, max_value, start, stop, counter):       # O(n)
    if len(arr) == 1:
        prev_max_at = max_at
        prev_min_at = min_at
        max_at = max(arr[0], arr[0]*prev_max_at, arr[0]*prev_min_at)
        if max_at == arr[0]:
            start = counter
        min_at = min(arr[0], arr[0]*prev_max_at, arr[0]*prev_min_at)
        max_value = max(max_value, max_at)
        if max_value == max_at:
            stop = counter
        return max_at, min_at, max_value, start, stop, counter+1
    
    mid = len(arr)//2
    left = div_n_conq_indexes(arr[:mid], max_at, min_at, max_value, start, stop, counter)
    right = div_n_conq_indexes(arr[mid:], left[0], left[1], left[2], left[3], left[4], left[5])
    
    return right[0], right[1], right[2], right[3], right[4], right[5]


arr = [1.202,0.74,0.807,1.269,0.421,1.085,1.574,1.233,0.939,0.796,1.049,0.092,0.367,1.413,1.453,1.543,1.624,0.509,0.519,0.856,1.406,1.245,1.731,1.081,0.845,1.5,1.124,1.479,0.701,1.24,0.587,1.184,0.282,0.888,1.245,1.616,1.174,0.393,1.035,0.95,1.082,1.264,1.762,0.867,1.141,1.002,1.421,1.244,1.527,1.057,0.592,0.272,0.684,1.672,0.508,1.421,1.363,0.863,0.606,0.989,0.489,0.853,1.14,1.451,0.177,1.575,0.929,1.967,1.242,1.734,0.681,1.764,1.396,0.392,0.97,0.803,0.924,0.764,1.096,0.514,1.498,0.673,0.818,0.72,1.079,0.665,0.943,0.989,0.698,0.982,0.824,1.044,1.209,0.382,1.34,0.916,0.705,0.396,1.066,1.544,0.988,1.338,1.108,1.465,0.637,1.232,0.521,0.963,1.31,0.173,0.85,0.221,0.899,0.024,1.101,1.457,0.826,0.953,1.405,0.631,1.882,0.624,1.129,1.399,1.82,0.659,0.263,1.203,1.499,1.724,0.209,1.289,1.578,0.162,0.213,1.26,0.349,1.035,1.14,0.829,1.47,1.245,1.445,1.115,0.881,1.064,1.211,1.504,1.338,1.146,0.778,1.798,0.328,1.036,0.79,0.76,0.044,0.229,1.028,0.886,0.93,1.724,0.833,0.156,0.791,0.946,0.834,1.817,1.636,1.187,0.208,1.453,0.791,1.722,1.297,0.979,1.692,0.948,1.073,0.772,0.994,1.11,1.193,0.164,1.471,0.718,1.775,0.947,0.403,1.133,0.145,1.801,1.187,0.769,1.053,0.877,1.268,0.962,0.804,0.036,1.476,1.767,1.852,0.925,0.854,0.227,0.892,1.438,0.928,1.535,1.061,1.147,1.299,1.264,0.823,0.974,1.697,0.673,0.51,1.103,0.746,1.26,1.633,0.827,0.817,0.401,0.695,1.505,0.785,1.04,1.347,0.457,1.113,1.132,1.172,0.299,1.631,1.023,0.997,1.453,1.257,1.575,1.394,1.154,1.187,1.425,0.995,0.468,0.995,0.942,1.17,1.29,0.708,1.349,1.162,0.774]
print('                          Brute Force:', brute_force(arr))
print('                          Incremental:', incremental(arr))
print('                Recursive Incremental:', rec_incremental(arr)[2])
print('           Dumb Recursive Incremental:', dumb_rec_incremental(arr)[1])
print()
print('                   Divide and conquer:', div_n_conq(arr, 1, 1, 0)[2])
print('      Divide and conquer return array:', arr[div_n_conq_indexes(arr, 1, 1, 0, 0, 0, 0)[3]:div_n_conq_indexes(arr, 1, 1, 0, 0, 0, 0)[4]+1])
print('        Divide and conquer with index:', div_n_conq_indexes(arr, 1, 1, 0, 0, 0, 0)[2:5])
print('Dumb Recursive Incremental with index:', rec_with_index(arr)[1:])
