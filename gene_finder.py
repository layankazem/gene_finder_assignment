import sys

# Default RBS sequence and search parameters
RBS_SEQUENCE = "AGGAGG"
MIN_ORF_LENGTH = 100  # minimum ORF length in codons
UPSTREAM_WINDOW = 20   # window to search upstream of the start codon

def has_rbs(sequence, start_index, window=UPSTREAM_WINDOW, rbs_seq=RBS_SEQUENCE):
    """
    Check if the upstream region contains a ribosome binding site (RBS).
    
    :param sequence: full genome sequence
    :param start_index: index of the start codon
    :param window: number of bases to look upstream of the start codon
    :param rbs_seq: sequence of the ribosome binding site to search for
    :return: True if an RBS is found, False otherwise
    """
    # Ensure we don't go out of bounds
    upstream_start = max(0, start_index - window)
    upstream_region = sequence[upstream_start:start_index]
    
    # Check if the RBS sequence is in the upstream region
    return rbs_seq in upstream_region

def filter_orfs_by_rbs(orfs, genome_sequence):
    """
    Filter ORFs based on the presence of a Shine-Dalgarno sequence upstream.
    
    :param orfs: list of ORFs (start, end positions)
    :param genome_sequence: full genome sequence
    :return: list of ORFs with valid RBS
    """
    valid_orfs = []
    for orf in orfs:
        start, end = orf
        if has_rbs(genome_sequence, start):
            valid_orfs.append(orf)
    return valid_orfs

def find_orfs(genome_sequence):
    # Your logic for finding ORFs goes here
    # e.g., finding start codons (ATG) and stop codons (TAA, TAG, TGA)
    orfs = []
    # Example ORFs found (start, end positions)
    orfs.append((100, 600))  # Just an example
    return orfs

def main():
    genome_file = sys.argv[1]
    with open(genome_file, 'r') as f:
        genome_sequence = f.read()
    
    # Find ORFs
    orfs = find_orfs(genome_sequence)
    
    # Filter ORFs by length (default length is 100 codons, can be parameterized)
    orfs = [orf for orf in orfs if (orf[1] - orf[0]) / 3 >= MIN_ORF_LENGTH]
    
    # Filter ORFs based on the presence of an RBS
    valid_orfs = filter_orfs_by_rbs(orfs, genome_sequence)
    
    # Output the valid ORFs (could be printed or written to a file)
    for orf in valid_orfs:
        print(f"Valid ORF: Start: {orf[0]}, End: {orf[1]}")
    
if __name__ == '__main__':
    main()
