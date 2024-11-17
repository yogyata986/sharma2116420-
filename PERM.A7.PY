from itertools import permutations

def generate_permutations(n):
    """Generates all permutations of length n."""
    nums = list(range(1, n + 1))
    perms = list(permutations(nums))
    
    # Print total number of permutations
    print(len(perms))
    
    # Print each permutation
    for perm in perms:
        print(' '.join(map(str, perm)))

# Read input from a file
# 
with open("INPUT.TXT", "r") as file:
    n = int(file.read().strip())

# Generate and print permutations
generate_permutations(n)



    