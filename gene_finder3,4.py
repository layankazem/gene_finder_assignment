"""
ChatGPT Prompt: 
Problem: Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.
An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.
Given: A DNA string s of length at most 1 kbp in FASTA format.
Return: Every distinct candidate protein string that can be translated from ORFs of s Strings can be returned in any order.
Give me the Python code
"""


import sys


# Genetic code dictionary for translating codons into amino acids
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
    'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
    'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
}


# Function to translate a sequence of codons into a protein sequence
def translate_sequence(seq):
    protein = []
    for i in range(0, len(seq), 3):
        codon = seq[i:i+3]
        if codon in genetic_code:
            amino_acid = genetic_code[codon]
            if amino_acid == '_':  # Stop translation if a stop codon is found
                break
            protein.append(amino_acid)
    return ''.join(protein)


# Function to find ORFs in all six reading frames and translate them
def find_orfs(sequence):
    orfs = set()  # Use a set to store distinct protein sequences
    frames = [sequence, sequence[1:], sequence[2:]]  # Forward frames


    # Process each forward reading frame
    for frame in frames:
        orfs.update(find_orfs_in_frame(frame))


    # Process the reverse complement frames
    reverse_sequence = reverse_complement(sequence)
    reverse_frames = [reverse_sequence, reverse_sequence[1:], reverse_sequence[2:]]
    for frame in reverse_frames:
        orfs.update(find_orfs_in_frame(frame))


    return orfs


# Function to find ORFs in a single reading frame
def find_orfs_in_frame(frame):
    start_codon = 'ATG'
    stop_codons = ['TAA', 'TAG', 'TGA']
    orfs = set()


    for i in range(len(frame) - 2):
        if frame[i:i+3] == start_codon:
            for j in range(i, len(frame) - 2, 3):
                codon = frame[j:j+3]
                if codon in stop_codons:
                    # Translate the ORF and add it to the set
                    protein = translate_sequence(frame[i:j+3])
                    if protein:
                        orfs.add(protein)
                    break
    return orfs


# Function to generate the reverse complement of a DNA sequence
def reverse_complement(sequence):
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    reverse_seq = sequence[::-1]  # Reverse the sequence
    return ''.join([complement[base] for base in reverse_seq if base in complement])


# Main function to handle command line arguments and read input file
def main():
    input_file = sys.argv[1]  # Get the input file from command line arguments


    with open(input_file, 'r') as file:  # Open the input FASTA file
        sequence = ''  # Initialize an empty string for the genome sequence
        for line in file:
            if not line.startswith('>'):  # Ignore header lines
                sequence += line.strip()


    # Find and print all distinct ORFs (translated proteins)
    orfs = find_orfs(sequence)
    for protein in orfs:
        print(protein)


# Entry point of the script
if __name__ == "__main__":
    main()  # Run the main function






