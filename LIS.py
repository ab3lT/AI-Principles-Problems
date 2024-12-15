def LISdp(arr):
    """
    Computes the length of the Longest Increasing Subsequence (LIS) using dynamic programming.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The length of the LIS.

    Example:
    >>> LISdp([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [1, 2, 1, 3, 2, 4, 4, 5, 6]
    6
    """
    dp = [1 for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    # print(dp)
    return max(dp)

from bisect import bisect_left

def LISbs(arr):
    """
    Computes the length of the Longest Increasing Subsequence (LIS) using binary search.

    Parameters:
    arr (list): A list of integers.

    Returns:
    int: The length of the LIS.

    Example:
    >>> LISbs([10, 22, 9, 33, 21, 50, 41, 60, 80])
    [10, 22, 33, 50, 60, 80]
    6
    """
    sub = []

    for i in arr:
        pos = bisect_left(sub, i)
        if pos == len(sub):
            sub.append(i)
        else:
            sub[pos] = i
    print(sub)  # Debug: Prints the current subsequence
    return len(sub)

def main():
    """
    Main function to demonstrate the LIS algorithms.

    Prompts the user to input a sequence of integers and computes the LIS length
    using both dynamic programming and binary search methods.

    Example:
    Input: 10 22 9 33 21 50 41 60 80
    Output:
    LIS using DP: 6
    LIS using Binary Search: 6
    """
    print("Enter a sequence of integers separated by spaces:")
    user_input = input()
    arr = list(map(int, user_input.split()))

    print("\nResults:")
    print(f"LIS using Dynamic Programming: {LISdp(arr)}")
    print(f"LIS using Binary Search: {LISbs(arr)}")

if __name__ == "__main__":
    main()
