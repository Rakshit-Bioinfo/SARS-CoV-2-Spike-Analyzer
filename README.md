# SARS-CoV-2 Spike Protein Analyzer

## Project Description
A bioinformatics pipeline built with Python and Linux that fetches the real reference sequence for the SARS-CoV-2 Spike protein from the NCBI database and performs fundamental sequence analysis.

## Biological Context
The Spike protein is critical for viral entry and is the primary target of current vaccines. This script calculates the total amino acid length and generates a composition report of all 20 standard amino acids.

## Results Summary
The script successfully validated the known length of the Spike protein:
* **Total Sequence Length:** 1,273 amino acids
* **Alanine (A) count:** 79
* **Cysteine (C) count:** 40
*(Full report is generated in the `results/` directory)*

## Repository Structure
* `data/`: Contains the raw downloaded FASTA file from NCBI.
* `scripts/`: Contains the Python code (`analyzer.py`).
* `results/`: Contains the generated text report (`analysis_report.txt`).

## Tools Used
* **Linux (WSL):** Used for downloading data via `curl` and running scripts.
* **Python 3:** Used for file parsing and string manipulation.

## How to Run
1. Clone the repository.
2. Navigate to the directory: `cd SARS-CoV-2-Spike-Analyzer`
3. Run the script: `python3 scripts/analyzer.py`