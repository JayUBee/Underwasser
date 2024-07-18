def densest_interval(f, n, window_size):
    """
    Finds the densest interval in f(x) = y where y is 0 or 1.
    
    Parameters:
    - f: list of integers (0 or 1) representing f(x)
    - n: integer, the maximum value of x
    - window_size: integer, the size of the sliding window
    
    Returns:
    - tuple (start, end) representing the densest interval
    """
    max_sum = 0
    max_start = 0
    current_sum = sum(f[:window_size])
    
    for i in range(n - window_size + 1):
        if current_sum > max_sum:
            max_sum = current_sum
            max_start = i
        if i + window_size < n:
            current_sum = current_sum - f[i] + f[i + window_size]
    
    return max_start, max_start + window_size - 1

