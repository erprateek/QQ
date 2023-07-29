'''
Question 1:
Given a list of DNA sequences (a string of characters containing only 'A', 'T', 'C', and 'G'), write a function that finds the sequence(s) with the highest GC content. The GC content of a DNA sequence is the percentage of bases that are either 'G' or 'C' in the sequence.

Example:
Input: ["ATGC", "CGTA", "ACGT", "TTAA"]
Output: ["ATGC", "CGTA", "ACGT"]
'''
def get_GC(seq: str):
    gc_sum = seq.count('G') + seq.count('C')
    seq_len = len(seq)
    return float(gc_sum*100/seq_len)

def get_highest_gc_seqs(list_of_seqs: list):
    # filter the list of sequences to a list containing sequences with max GC percent
    seq_gc_pct_list = [get_GC(item) for item in list_of_seqs]
    max_gc_pct = max(seq_gc_pct_list)
    filtered_list = []
    for seq, gc_pct in zip(list_of_seqs, seq_gc_pct_list):
        if gc_pct == max_gc_pct:
            filtered_list.append(seq)
    return filtered_list

input = ["ATGC", "CGTA", "ACGT", "TTAA"]
observed_output = get_highest_gc_seqs(input)
expected_output = ["ATGC", "CGTA", "ACGT"]

print(sorted(observed_output))
print(sorted(expected_output))