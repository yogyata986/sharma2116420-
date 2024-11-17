from collections import defaultdict

def parse_fasta(file_path):
    """Parses a FASTA file and extracts DNA strings."""
    with open(file_path, 'r') as f:
        lines = f.readlines()
        dna_strings = []
        current_dna = []
        for line in lines:
            line = line.strip()
            if line.startswith('>'):
                if current_dna:
                    dna_strings.append(''.join(current_dna))
                    current_dna = []
            else:
                current_dna.append(line)
        if current_dna:
            dna_strings.append(''.join(current_dna))
    return dna_strings

def compute_profile_and_consensus(dna_strings):
    """Computes the profile matrix and consensus string."""
    n = len(dna_strings[0])  # Length of each DNA string
    profile = {'A': [0] * n, 'C': [0] * n, 'G': [0] * n, 'T': [0] * n}
    
    # Populate the profile matrix
    for dna in dna_strings:
        for i, nucleotide in enumerate(dna):
            profile[nucleotide][i] += 1
    
    # Generate the consensus string
    consensus = []
    for i in range(n):
        max_nucleotide = max(profile.keys(), key=lambda x: profile[x][i])
        consensus.append(max_nucleotide)
    
    return ''.join(consensus), profile

def format_profile(profile):
    """Formats the profile matrix for output."""
    formatted = []
    for nucleotide in 'ACGT':
        formatted.append(f"{nucleotide}: {' '.join(map(str, profile[nucleotide]))}")
    return '\n'.join(formatted)

# Example usage
file_path = "INPUT.TXT"  # Replace with the actual FASTA file path
dna_strings = parse_fasta(file_path)
consensus, profile = compute_profile_and_consensus(dna_strings)

# Print the results
print(consensus)
print(format_profile(profile))
