# Script: analyzer.py
# Purpose: To analyse the  SARS- CoV-2-spike protein sequence
# Author: Rakshit Sinha 

# 1. Read the spike protein sequence from the spike_protein.fasta file, data subfolder
with open("data/spike_protein.fasta", "r") as file:
    full_sequence = ""
    for line in file:
        clean_line = line.strip()

        # Skip the header lines(>)
        if not clean_line.startswith(">"):
            full_sequence = full_sequence + clean_line   # It glues the whole sequnce line by line

# 2. Generate the result in certain files
with open("results/analysis_report.txt", "w") as out_file:
    out_file.write(f"---SARS-CoV-2- Spike protein Analysis---\n")
    out_file.write(f"Total Length:{len(full_sequence)} amino acids\n")    # Get to know the total number of amino acids.
    out_file.write(f"Amino acids compositions-->\n")   # The number of each amino acid 

    # 3. Count the 20 standard amino acids.
    amino_acids = "ACDEFGHIKLMNPQRSTVWY"

    for aa in amino_acids:
        count = full_sequence.count(aa)
        out_file.write(f"{aa}: {count}\n")     # Python code to write the number of particular amino acid along with there name

