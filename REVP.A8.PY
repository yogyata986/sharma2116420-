def reverse_complement(dna):
    """Returns the reverse complement of a DNA string."""
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complement[base] for base in reversed(dna))

def find_reverse_palindromes(dna):
    """Finds all reverse palindromes of length 4 to 12 in the DNA string."""
    results = []
    n = len(dna)
    
    # Check substrings of lengths between 4 and 12
    for length in range(4, 13):
        for i in range(n - length + 1):
            substring = dna[i:i + length]
            if substring == reverse_complement(substring):
                # Add position (1-based) and length
                results.append((i + 1, length))
    
    return results

def parse_fasta(file_path):
    """Parses a FASTA file and extracts the DNA string."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
        # Remove header and join lines to get the DNA string
        dna = ''.join(line.strip() for line in lines if not line.startswith('>'))
    return dna

# Example usage
file_path = "INPUT.TXT"  # Replace with the actual FASTA file path
dna = parse_fasta(file_path)
palindromes = find_reverse_palindromes(dna)

# Print the results
for pos, length in palindromes:
    print(pos, length)
