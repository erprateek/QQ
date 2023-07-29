'''
Question 2:
Design a function that identifies potential open reading frames (ORFs) within a given DNA sequence. An ORF is a sequence of DNA that has the potential to be translated into a protein. It starts with a start codon (ATG) and ends with a stop codon (TAA, TAG, or TGA). The function should take a DNA sequence as input and return a list of all identified ORFs.

Example:
Input: "TCAATGCGCATGATGCCCTAAATGGCTAG"
Output: ["ATGATGCCCTAAATGGCTAG"] -> [" ", " "]
# ATGTGA is a valid ORF

# ATG...TGA
# _ATG
# ___ATG
'''

def find_all_orfs_from_seq(s: str):
    window = 3
    start_codon = "ATG"
    stop_codons = ["TAA","TAG","TGA"]
    output_orfs = []
    for i in range(len(s)):
        triple = s[i:i+3] # TCA, CAA ...
        current_start_location = -1
        if triple in stop_codons and current_start_location == -1:
            continue
        if triple == start_codon:
            current_start_location = i
            for j in range(current_start_location,len(s[current_start_location+3:]), window):
                orf_triple = s[j:j+window]
                if len(orf_triple) != 3:
                    continue
                if orf_triple in stop_codons:
                    output_orfs.append(s[current_start_location:j+window])
            