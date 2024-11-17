def parse_fasta(fasta):
    """Parse FASTA input to return sequences."""
    sequences = []
    current_seq = []
    for line in fasta.strip().split('\n'):
        if line.startswith('>'):
            if current_seq:
                sequences.append(''.join(current_seq))
                current_seq = []
        else:
            current_seq.append(line)
    if current_seq:
        sequences.append(''.join(current_seq))
    return sequences

def calculate_transition_transversion_ratio(s1, s2):
    """Calculate the transition/transversion ratio for two DNA strings."""
    transitions = 0
    transversions = 0
    
    purines = {'A', 'G'}
    pyrimidines = {'C', 'T'}
    
    for base1, base2 in zip(s1, s2):
        if base1 != base2:  # Only consider mismatches
            if {base1, base2} <= purines or {base1, base2} <= pyrimidines:
                transitions += 1
            else:
                transversions += 1
    
    # Avoid division by zero
    if transversions == 0:
        return float('inf')  # Infinite ratio if no transversions
    return transitions / transversions

# Example Usage
with open("INPUT.TXT", "r") as file:
    fasta_input = file.read()

sequences = parse_fasta(fasta_input)
s1, s2 = sequences[0], sequences[1]

result = calculate_transition_transversion_ratio(s1, s2)
print(f"{result:.11f}")
