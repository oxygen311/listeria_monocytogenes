from Bio import SeqIO


file = SeqIO.parse('bifidobact/fasta/merged.fasta', 'fasta')

for record in file:
    print(record.id, len(record.seq))