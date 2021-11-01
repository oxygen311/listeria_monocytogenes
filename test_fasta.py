from Bio import SeqIO


file = SeqIO.parse('data_1/listeria_aligned_10.fasta', 'fasta')

for record in file:
    print(record.id, len(record.seq))