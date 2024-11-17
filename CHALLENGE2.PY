def maximumToys(prices, k):
    # Step 1: Sort the prices in ascending order
    prices.sort()
    
    # Step 2: Initialize variables
    count = 0  # Number of toys Mark can buy
    total_cost = 0  # Cumulative cost of toys
    
    # Step 3: Buy toys within the budget
    for price in prices:
        # Check if adding this toy's price stays within the budget
        if total_cost + price <= k:
            total_cost += price
            count += 1
        else:
            break  # Stop if we can't afford the next toy
    
    return count

# Input from user
if __name__ == "__main__":
    # Read inputs
    n, k = map(int, input().split())  # First line: number of toys and budget
    prices = list(map(int, input().split()))  # Second line: toy prices

    # Ensure correct input length
    if len(prices) != n:
        print("Error: The number of toy prices provided does not match the specified number.")
    else:
        # Compute and print the result
        result = maximumToys(prices, k)
        print(result)
