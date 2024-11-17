def parse_fasta(fasta):
    """Parse FASTA input and return a list of sequences."""
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

def translate_rna_to_protein(rna):
    """Translate RNA to protein using the standard codon table."""
    codon_table = {
        'AUG': 'M', 'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',
        'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',
        'UAU': 'Y', 'UAC': 'Y', 'UAA': 'Stop', 'UAG': 'Stop',
        'UGU': 'C', 'UGC': 'C', 'UGA': 'Stop', 'UGG': 'W',
        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
        'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',
        'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',
        'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',
        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',
        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',
        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G'
    }
    
    protein = []
    for i in range(0, len(rna), 3):
        codon = rna[i:i+3]
        amino_acid = codon_table.get(codon, '')
        if amino_acid == 'Stop':
            break
        protein.append(amino_acid)
    return ''.join(protein)

def dna_to_protein(fasta_input):
    """Process the DNA string and introns to produce the protein string."""
    sequences = parse_fasta(fasta_input)
    dna = sequences[0]  # The first sequence is the main DNA string
    introns = sequences[1:]  # The rest are introns
    
    # Remove introns from the DNA
    for intron in introns:
        dna = dna.replace(intron, '')
    
    # Transcribe DNA to RNA
    rna = dna.replace('T', 'U')
    
    # Translate RNA to Protein
    protein = translate_rna_to_protein(rna)
    return protein

# Example Usage
with open("INPUT.TXT", "r") as file:
    fasta_input = file.read()

result = dna_to_protein(fasta_input)
print(result)
