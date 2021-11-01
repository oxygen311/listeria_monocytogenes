import os
from Bio import Entrez
from Bio import SeqIO

IDs = []

Entrez.email = 'mikhail.nikitin@phytech.edu'
id_list_path = r'C:\Users\user\Desktop\VIGG\listeria_ids.txt'
fasta_folder = r"C:\Users\user\Desktop\VIGG\listeria"
rename_file = r'C:\Users\user\Desktop\VIGG\listeria_names.txt'
temp_gb_file = r"C:\Users\user\Desktop\VIGG\temp.gb"

with open(id_list_path) as f:
    for line in f.readlines():
        IDs.append(line.rstrip())

with open(rename_file, 'w') as names:
    for ID in IDs:
        with open(temp_gb_file, 'w') as tempfile:
            with open(os.path.join(fasta_folder, f'{ID}.fasta'), 'w') as outfile:
                handle = Entrez.efetch(db='nucleotide', id=ID, rettype='fasta',
                                       NCBI_API_KEY='fff9228935ae6c9205e24eec4edb795dc108')
                gb_handle = Entrez.efetch(db='nucleotide', id=ID, rettype='gb',
                                       NCBI_API_KEY='fff9228935ae6c9205e24eec4edb795dc108')
                outfile.write(handle.read())
                tempfile.write(gb_handle.read())
        with open(temp_gb_file, 'r') as f:
            genbank = SeqIO.parse(f, 'genbank')
            for object in genbank:
                print(f'{ID} -> {object.description}', file=names)