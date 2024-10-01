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

## Prodigal Installation
```bash
module load prodigal
```
## Utilize command line tools to count the number of annotated genes
```bash
prodigal --help
input_file="/home/kazemlz/data-bacteria-assignment/ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.fna"
gff_file="${input_file%.fna}.gff"
prodigal -i "$input_file" -o "$gff_file" -q
cds_count=$(grep -c "CDS" "$gff_file")
echo "File: $gff_file, CDS Count: $cds_count"
```
## Answer: 
```bash
File: /home/kazemlz/data-bacteria-assignment/ncbi_dataset/data/GCA_000008725.1/GCA_000008725.1_ASM872v1_genomic.gff, CDS Count: 897
```
#### Zhang Helped with this problem's code

# Question 3
### Run prodigal on all of the genomes you have previously downloaded. Using command line tools, find which genome has the highest number of genes. Put all your code into a shell script, and put your code on the repository on Github where you keep your README with the solutions to this assignment.

## Shell Script
```bash
emacs question3--.sh
```
```bash
#!/bin/bash                                                                                                                                                                       

# Script to find the genome with the highest number of genes                                                                                                                      

max_gene_count=0
top_genome=""

# Loop through each genome directory                                                                                                                                              
for genome_folder in GCA_*; do
  genomic_file=$(find "$genome_folder" -name "*_genomic.fna")

  if [[ -f "$genomic_file" ]]; then
    output_genes="${genome_folder}_genes.gbk"
    output_proteins="${genome_folder}_proteins.faa"

    prodigal -i "$genomic_file" -o "$output_genes" -a "$output_proteins"

    cd_count=$(grep -c "CDS" "$output_genes")
    echo "Genome: $genomic_file - Number of genes: $cd_count"

    if (( cd_count > max_gene_count )); then
      max_gene_count=$cd_count
      top_genome=$genomic_file
    fi
  else
    echo "No genomic file found in $genome_folder"
  fi
done

# Display the genome with the highest number of genes                                                                                                                             
echo "Genome with the highest number of genes: $top_genome with $max_gene_count genes."

# ---------------------------                                                                                                                                                     

# Script to count the number of CDS entries in .gbk files                                                                                                                         

for genes_file in $(find . -name "*_genes.gbk"); do
  cds_total=$(grep -c "CDS" "$genes_file")
  echo "File: $genes_file - Number of CDS: $cds_total"
done
```
```bash
bash question3--.sh
```
## Answer: 
```bash
Genome with the highest number of genes: GCA_000006745.1/GCA_000006745.1_ASM674v1_genomic.fna with 3594 genes.
File: ./GCA_000006745.1_genes.gbk - Number of CDS: 3594
File: ./GCA_000006825.1_genes.gbk - Number of CDS: 2032
File: ./GCA_000006865.1_genes.gbk - Number of CDS: 2383
File: ./GCA_000007125.1_genes.gbk - Number of CDS: 3152
File: ./GCA_000008525.1_genes.gbk - Number of CDS: 1579
File: ./GCA_000008545.1_genes.gbk - Number of CDS: 1866
File: ./GCA_000008565.1_genes.gbk - Number of CDS: 3248
File: ./GCA_000008605.1_genes.gbk - Number of CDS: 1009
File: ./GCA_000008625.1_genes.gbk - Number of CDS: 1776
File: ./GCA_000008725.1_genes.gbk - Number of CDS: 897
File: ./GCA_000008745.1_genes.gbk - Number of CDS: 1063
File: ./GCA_000008785.1_genes.gbk - Number of CDS: 1505
File: ./GCA_000027305.1_genes.gbk - Number of CDS: 1748
File: ./GCA_000091085.2_genes.gbk - Number of CDS: 1063
```
#### Manal Helped with this problem's code


# Question 4
### Annotate all genomes you have previously downloaded using prokka instead of prodigal. Using shell commands, count the number of coding sequences (CDS) annotated by Prokka. Are the total number of genes the same as they were with prodigal? What are the differences?

## Shell Script
```bash
emacs question4.sh
```
```bash
#!/bin/bash
module load prokka
# Annotate genomes with Prokka
for genome_directory in GCA_*; do
  genomic_file=$(find "$genome_directory" -name "*_genomic.fna")

  if [[ -f "$genomic_file" ]]; then
    output_directory="${genome_directory}_prokka_results"
    prokka --outdir "$output_directory" --prefix "${genome_directory}" "$genomic_file"

    result_file="$output_directory/${genome_directory}.txt"

    if [[ -f "$result_file" ]]; then
      cds_annotation_count=$(grep -w "CDS" "$result_file" | awk '{print $2}')
      echo "Genome: $genomic_file - Annotated CDS count: $cds_annotation_count"
    else
      echo "Could not find Prokka output file for $genomic_file"
    fi
  else
    echo "Genomic file not found in $genome_directory"
  fi
done

# Collect CDS counts from Prokka output
for prokka_output in *_prokka_results; do
  text_file=$(find "$prokka_output" -name "*.txt")

  if [[ -f "$text_file" ]]; then
    cds_count_total=$(grep "CDS:" "$text_file" | awk '{print $2}')
    echo "Directory: $prokka_output - Total CDS count: $cds_count_total"
  else
    echo "No text file found in $prokka_output"
  fi
done
```
```bash
bash question4.sh
```
## Answer: 
```bash
Number of CDS (Prokka): 3589
Directory: GCA_000006745.1_prokka_results - Total CDS count: 3589
Directory: GCA_000006825.1_prokka_results - Total CDS count: 2028
Directory: GCA_000006865.1_prokka_results - Total CDS count: 2383
Directory: GCA_000007125.1_prokka_results - Total CDS count: 3150
Directory: GCA_000008525.1_prokka_results - Total CDS count: 1577
Directory: GCA_000008545.1_prokka_results - Total CDS count: 1861
Directory: GCA_000008565.1_prokka_results - Total CDS count: 3245
Directory: GCA_000008605.1_prokka_results - Total CDS count: 1001
Directory: GCA_000008625.1_prokka_results - Total CDS count: 1771
Directory: GCA_000008725.1_prokka_results - Total CDS count: 892
Directory: GCA_000008745.1_prokka_results - Total CDS count: 1058
Directory: GCA_000008785.1_prokka_results - Total CDS count: 1504
Directory: GCA_000027305.1_prokka_results - Total CDS count: 1748
Directory: GCA_000091085.2_prokka_results - Total CDS count: 1056
```
### The gene counts from Prokka and Prodigal differ slightly, with Prodigal identifying 3594 coding sequences compared to Prokka's 3589. This variation arises from their different algorithms: Prodigal focuses on sequence features, while Prokka uses a broader range of biological data for annotation, sometimes leading to the exclusion of certain predicted genes. Additionally, Prokka also annotates non-coding genes, unlike Prodigal, which targets only protein-coding sequences.

#### Manal Helped with this problem's code


# Question 5
### Extract and list all unique gene names annotated by Prokka using shell commands. Provide the command you used and the first five gene names from the list.

## PowerShell script:
```bash
#!/bin/bash

mkdir -p combined_output

# Loop through each directory and copy .gbk files
for dir in */; do
  if [[ -d "$dir" ]]; then
    cp "${dir}"*.gbk combined_output/ 2>/dev/null
  fi
done

echo "All .gbk files have been copied to combined_output."
```
```bash
grep -h 'gene=' *.gbk | cut -d'=' -f2 | tr -d '"' | sort -u > unique_genes.txt
```
```bash
grep -h 'gene=' *.gbk | cut -d'=' -f2 | tr -d '"' | sort -u > unique_genes.txt
```
## Answers: 
```bash
aaaT
aaeA
aaeA_1
aaeA_2
aaeB
```
