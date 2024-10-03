"""
ChatGPT statement: 
 Now you have Open Reading Frames, but not all of them will be
 genes. Implement a filter by length: discard short ORFs that are unlikely
 to be functional genes (e.g., less than 100 codons, but make the length a
 parameter of your tool).
 Give me the Python code for the problem
 """


import sys


# Genetic code dictionary for translating DNA sequences to protein
genetic_code = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGA':'_'
}


# Function to translate a DNA sequence to a protein
def translate_sequence(seq):
    protein = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i + 3]
        if len(codon) < 3:
            break
        protein.append(genetic_code.get(codon, 'X'))  # 'X' for unknown codon
        if protein[-1] == '_':  # Stop codon
            break
    return ''.join(protein)


# Function to find ORFs longer than the specified minimum length
def find_orfs(dna_sequence, min_length=100):
    orfs = []
    stop_codons = ['TAA', 'TAG', 'TGA']
   
    # Search in all 3 frames
    for frame in range(3):
        for i in range(frame, len(dna_sequence) - 2, 3):
            codon = dna_sequence[i:i + 3]
            if codon == 'ATG':  # Start codon
                for j in range(i, len(dna_sequence) - 2, 3):
                    stop_codon = dna_sequence[j:j + 3]
                    if stop_codon in stop_codons:
                        orf_length = (j - i + 3) // 3  # Calculate length in codons
                        if orf_length >= min_length:
                            orfs.append(translate_sequence(dna_sequence[i:j + 3]))
                        break
    return orfs


# Function to find ORFs from both strands
def find_orfs_in_both_strands(dna_sequence, min_length=100):
    # Complementary strand
    complement = {'A':'T', 'T':'A', 'C':'G', 'G':'C'}
    reverse_complement = ''.join([complement[base] for base in dna_sequence[::-1]])


    # Find ORFs in both the original and reverse complement strands
    orfs = find_orfs(dna_sequence, min_length) + find_orfs(reverse_complement, min_length)
    return orfs


# Main function to load DNA from a file and find ORFs
def main():
    if len(sys.argv) < 2:
        print("Usage: python gene_finder.py <input_file> [min_length]")
        sys.exit(1)


    input_file = sys.argv[1]
    min_length = int(sys.argv[2]) if len(sys.argv) > 2 else 100  # Default to 100 codons if not specified


    with open(input_file, 'r') as f:
        dna_sequence = ''.join([line.strip() for line in f if not line.startswith('>')])  # Ignore header lines


    orfs = find_orfs_in_both_strands(dna_sequence, min_length)
   
    for orf in orfs:
        print(orf)


if __name__ == "__main__":
    main()





