#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Sampoorna Saha
#
# Created:     04-07-2025
# Copyright:   (c) Sampoorna Saha 2025
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
def analyze_dna(seq):
    seq = seq.upper()
    a = seq.count('A')
    t = seq.count('T')
    g = seq.count('G')
    c = seq.count('C')
    total = len(seq)

    gc_content = round(((g + c) / total) * 100, 2)
    at_content = round(((a + t) / total) * 100, 2)

    print("Total length:", total)
    print("A:", a, "T:", t, "G:", g, "C:", c)
    print("GC Content (%):", gc_content)
    print("AT Content (%):", at_content)


dna_seq = "ATGCGTACGTAGCTAGCTAGCTAGCTAGCTAGCGCGCGCGTATATATATATAGCGC"
analyze_dna(dna_seq)