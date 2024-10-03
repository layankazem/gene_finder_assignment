"""
ChatGPT prompt:  Extend your tool to include the reverse complement and search
 in all six possible reading frames for genes. You could reuse the code you
 wrote in the first week’s assignments for generating reverse compliments
 of a string, or use BioPython to complete the assignment.
 Give me the Python code for the qustion
 """



import sys


# Function to find all open reading frames (ORFs) in a given genome sequence
def find_genes(sequence):
    """
    Find all open reading frames (ORFs) in the given genome sequence.
    Returns a list of found genes.
    """
    genes = []  # List to store found genes
    start_codon = 'ATG'  # Start codon
    stop_codons = ['TAA', 'TAG', 'TGA']  # Stop codons


    # Loop through the sequence to find start codons
    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == start_codon:  # Check for start codon
            # Look for stop codon
            for j in range(i, len(sequence) - 2, 3):
                if sequence[j:j+3] in stop_codons:
                    genes.append(sequence[i:j+3])  # Add gene to list
                    break  # Exit the loop after finding the first stop codon
    return genes  # Return the list of found genes


# Function to compute reverse complement of a DNA sequence
def reverse_complement(sequence):
    """
    Return the reverse complement of the given DNA sequence.
    Skip any ambiguous bases.
    """
    complement = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}  # Complementary base pairs
    reverse_seq = sequence[::-1]  # Reverse the sequence
    return ''.join([complement.get(base, 'N') for base in reverse_seq])  # Replace with 'N' if no complement found


# Function to find genes in all three reading frames
def find_genes_in_frames(sequence):
    """
    Find genes in all three reading frames of a given sequence.
    """
    all_genes = []
    for frame in range(3):  # Check the three reading frames
        all_genes.extend(find_genes(sequence[frame:]))  # Find genes in the current reading frame
    return all_genes


# Main function to handle command line arguments and read input file
def main():
    input_file = sys.argv[1]  # Get the input file from command line arguments
   
    try:
        codonMin = int(sys.argv[2])
    except:
        codonMin = 20  


    # Read the genome sequence from the input FASTA file
    with open(input_file, 'r') as file:
        sequence = ''  # Initialize an empty string for the genome sequence
        for line in file:
            if not line.startswith('>'):  # Ignore header lines
                sequence += line.strip()  # Append sequence lines to the genome sequence


    # Find genes in both forward and reverse complement
    forward_genes = find_genes_in_frames(sequence)
    reverse_genes = find_genes_in_frames(reverse_complement(sequence))


    # Combine genes from both forward and reverse strands
    all_genes = forward_genes + reverse_genes
   
    print("Found genes:", all_genes)  # Output the found genes
    print(len(all_genes))




# Entry point of the script
if __name__ == "__main__":
    main()  # Run the main function





