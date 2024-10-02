# gene_finder_assignment

# Creating a Repository and Navigating to it
## Created a GitHub repository named gene_finder_assignment, then navigate to it

 ```bash
cd C:\Users\layan\Downloads\gene_finder_assignment
```

# Creating the Main Python File
## Created a new Python file called gene_finder.py using the following command:

 ```bash
echo "" > gene_finder.py
```


# Running the Python Script for Questions 1, 2, and 3
## Type the command with the path to the input FASTA file

 ```bash
 python gene_finder.py “C:\Users\layan\Downloads\ncbidata\ncbi_dataset\data\GCA_000006745.1\GCA_000006745.1_ASM674v1_genomic.fna” > question1.txt
```
 ```bash
 python gene_finder.py “C:\Users\layan\Downloads\ncbidata\ncbi_dataset\data\GCA_000006745.1\GCA_000006745.1_ASM674v1_genomic.fna” > question2.txt
```
 ```bash
 python gene_finder.py “C:\Users\layan\Downloads\ncbidata\ncbi_dataset\data\GCA_000006745.1\GCA_000006745.1_ASM674v1_genomic.fna” > question3.txt
```


# Question 4, 5, and 6

## Creating the bash script
 ```bash
Emacs q4.sh
```
## Bash Script:
 ```bash

#!/bin/bash

echo> question4.txt
for file in $(find ../data-bacteria-assignment/ncbi_dataset/data/ -name 'GCA*fna')
do

    echo $file
    echo $file >> question4.txt
    python gene_finder.py $file >> question4.txt
done
```
### Ctrl X + Ctrl S  to save. Ctrl X + Ctrl C  to exit.

## Run
```bash
Bash q4.sh
```

## Save
```bash
scp kazemlz@ilogin.ibex.kaust.edu.sa:~/gene_finder_assignment/question4.txt C:\Users\layan\Downloads\gene_finder_assignment\question4.txt
```
### Question 5 and 6 follow the same steps as 4.

#### This HW was with the help of Yazeed Alroogi, and the Python codes were written with the help of ChatGPT
