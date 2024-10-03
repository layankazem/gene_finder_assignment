"""
ChatGPT prompt:  The tool you write needs to take command line parameters
 for the input file. The input file should consist of a single FASTA file
 containing a single genome.
 Your tool should read a FASTA file, and output any region between a
 start (‘ATG’) and stop codon (‘TAA’, ‘TAG’, ‘TGA’) in that FASTA file;
 you must consider three possible reading frames but may ignore reverse
 compliments
 Give me the Python code for the Question
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


# Main function to handle command line arguments and read input file
def main():
 
    input_file = sys.argv[1]  # Get the input file from command line arguments


    try:
        codonMin = sys.argv[2]


    except:
        CodonMin = 20


    with open(input_file, 'r') as file:  # Open the input FASTA file
        sequence = ''  # Initialize an empty string for the genome sequence
        for line in file:  # Read the file line by line
            if not line.startswith('>'):  # Ignore header lines
                sequence += line.strip()  # Append sequence lines to the genome sequence


    genes = find_genes(sequence)  # Call the function to find genes
    print("Found genes:", genes)  # Output the found genes
    print(len(genes))


# Entry point of the script
if __name__ == "__main__":
    main()  # Run the main function











