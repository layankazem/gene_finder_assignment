# Question 1
### If given the amino acid sequence KVRMFTSELDIMLSVNGPADQIKYFCRHWT, what is the number of amino acids in the encoded peptide (not including the stop codon)? Additonally, how many bases are contained in the open reading frame of the DNA sequence encoding the amino acids (including the stop codon)
## PowerShell script:
```bash
$sequence = "KVRMFTSELDIMLSVNGPADQIKYFCRHWT"  # Excluding the stop codon (*)
$amino_acid_count = $sequence.Length
Write-Host "Number of amino acids: $amino_acid_count"
```
```bash
$amino_acid_count_with_stop = $amino_acid_count + 1  # Including stop codon (*)
$nucleotide_bases = $amino_acid_count_with_stop * 3
Write-Host "Number of bases: $nucleotide_bases"
```
## Answers: 
```bash
30
93
```

# Question 2
###  Run prodigal on one of the genomes you have previously downloaded. Using command line tools, count how many genes were annotated (you can use any of the output formats for this but some are easier than others)
