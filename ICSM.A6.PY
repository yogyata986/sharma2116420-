#Given: A collection of kk (k≤100k≤100) DNA strings of length at most 1 kbp each in FASTA format.
#Return: A longest common substring of the collection. (If multiple solutions exist, you may return any single solution.)

def find_longest_common_substring(dna_sequences):
    # Function to check if a substring is common to all sequences
    def is_common_substring(substring):
        return all(substring in seq for seq in dna_sequences)

    # Start with the shortest DNA sequence
    shortest_seq = min(dna_sequences, key=len)
    left, right = 0, len(shortest_seq)
    longest_common_substring = ""

    # Binary search for the longest common substring
    while left <= right:
        mid = (left + right) // 2
        found = False

        # Check all substrings of length `mid`
        for start in range(len(shortest_seq) - mid + 1):
            substring = shortest_seq[start:start + mid]
            if is_common_substring(substring):
                found = True
                longest_common_substring = substring
                break

        # Adjust search range
        if found:
            left = mid + 1  # Try for a longer substring
        else:
            right = mid - 1  # Try for a shorter substring

    return longest_common_substring


# Read input file
with open("INPUT.TXT", "r") as f:
    data = f.read()

# Parse FASTA-like format
sequences = []
for line in data.split(">"):
    if line.strip():
        parts = line.split("\n", 1)
        sequences.append(parts[1].replace("\n", ""))

# Find and print the longest common substring
result = find_longest_common_substring(sequences)
print(result)
